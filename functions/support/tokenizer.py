from typing import Dict
from pathlib import Path

class WordCount:
    """Class representing a word term and it's count within a note.
    """
    def __init__(self, word: str, count: int):
        self.word = word
        self.count = count

    def __str__(self):
        return f"word={self.word}, count={self.count}"

    def __eq__(self, other):
        return other and self.word == other.word


class WordTokenizer:
    def __init__(self, stop_words=None, min_word_len=3):
        if stop_words is None:
            basedir = Path(__file__).parent
            with open(basedir / 'stopwords.txt') as f:
                stop_words = list(filter(None, [s.strip() for s in f.readlines()]))
        
        self.stop_words = stop_words
        self.min_word_len = min_word_len

    def _handle_word(self, chars, words):
        """Helper for checking if current word is valid, and if so add
        it to list of words. A valid word should meet min length and not
        be part of stop words list.
        """
        if len(chars) >= self.min_word_len:
            word = ''.join(chars)
            if word not in self.stop_words:
                words[word] = words.get(word, WordCount(word, 0))
                words[word].count += 1

    def tokenize(self, s) -> Dict[str, WordCount]:
        """Break the given string s into list of Words
        """
        words = {}
        chars = []
        for ch in s:
            if ch.isspace():
                self._handle_word(chars, words)
            else:
                chars.append(ch.lower())
        self._handle_word(chars, words)
        return words