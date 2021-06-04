import type { Note } from '../note';

async function remove(id) {
  fetch(`/api/notes/${id}`, {
    method: 'DELETE'
  }).then(res => {
    if (res.ok)
      return res.json();
    throw new Error(`Unable to remove note: ${id}`);
  })
}

async function all({tags}) {
  return fetch(`/api/notes${tags ? `?tags=${tags}` : ''}`)
    .then(res => {
      if (res.ok)
        return res.json();
      throw new Error(`Unable to get all notes.`);
    });
}

async function get(id: string) {
  return fetch(`/api/notes/${id}`)
    .then(res => {
      if (res.ok)
        return res.json();
      throw new Error(`Unable to load note: ${id}`);
    });
}

async function createOrUpdate(note: Note) {
  // Default url for creating new Note
  let url = '/api/notes';
  let method = 'POST';

  // Looks like an existing id, let's do an update instead
  if (note.id && note.id !== 'new') {
    url = `${url}/${note.id}`;
    method = 'PUT';
  }

  return fetch(url, {
      method, 
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(note)
    }).then(res => {
      if (res.ok)
        return res.json();
      throw new Error(`Unable to create or update note: method=${method}, url=${url}, note=${note}`);
    });
}

export default {
  all,
  createOrUpdate,
  get,
  remove
}
