import os
import dotenv
import redis
import json

from pathlib import Path
from .tokenizer import WordTokenizer


basedir = Path(__file__).parent
dotenv.load_dotenv(basedir.parent / '.env')


class NoteIndexer:
    def __init__(self, tokenizer=None, redisdb=None):
        self.init(tokenizer, redisdb)

    def init(self, tokenizer=None, redisdb=None):
        if redisdb is None:
            password = os.environ['REDIS_PASSWORD']
            host = os.environ['REDIS_HOST']
            port = os.environ['REDIS_PORT']
            redisdb = redis.Redis(host=host, port=port, 
                password=password, decode_responses=True)
        
        if tokenizer is None:
            tokenizer = WordTokenizer()

        self.tokenizer = tokenizer
        self.redisdb = redisdb

    def tokenize(self, title='', content='', tags=None, **kwargs):
        """Flatten a notes indexable content (title, content, tags)
        and tokenize into words.
        """
        tags_str = ' '.join(tags or [])
        return self.tokenizer.tokenize(' '.join([title, content, tags_str]))

    def add(self, note):
        """Tokenize a given note into list of words and count of their occurrences,
        then add the word to our reverse index"""
        if not (note and note.id):
            return
        
        # Pipeline the redis commands to reduce round trip time (rtt)
        pipe = self.redisdb.pipeline()

        # Store info about each note, after search results, resolve each result 
        # to this info
        pipe.hset(name='notes', key=note.id, 
            value=json.dumps(dict(id=note.id, title=note.title, tags=note.tags)))
        words = self.tokenize(**note)
        for word in words.values():
            # Our reverse index is just a word -> {note.id, word count} stored
            # in a redis sorted set.
            #  - naively, word count is uses as a score, indicating how relevant 
            #    the word is in context of a note
            #  - words are search using ZINER, unfortunately ZINTER orders asc but
            #    we need words to return by desc (higher word counts first), so 
            #    we negate each score as a hack to get the words ordered correctly
            pipe.zadd(name=f'_{word.word}', mapping={note.id: -word.count})
        pipe.execute()

    def delete(self, note):
        """Remove all words for the given note from our reverse index. 
        """
        if not (note and note.id):
            return

        words = self.tokenize(**note)
        pipe = self.redisdb.pipeline()

        pipe.hdel('notes', note.id)

        for word in words.values():
            pipe.zrem(f'_{word.word}', note.id)
        pipe.execute()