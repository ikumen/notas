const notes_base_uri = '/api/notes';

async function handleResponse(res: Response) {
  if (res.ok) {
    try {
      return await res.json();
    } catch (err) {
      // Handle 204
      return Promise.resolve();
    }
  }

  let errorMessage = 'Sorry we could not complete request, please try again.'
  if (res.status === 404)
    errorMessage = `Note not found`;
  if (res.status < 500)
    errorMessage = `Invalid request`;
  throw new Error(errorMessage);
}

async function remove(id: string) {
  return fetch(`${notes_base_uri}/${id}`, {
      method: 'DELETE'
    }).then(handleResponse);
}

async function list() {
  return fetch(`${notes_base_uri}`)
    .then(handleResponse);
}

async function get(id: string) {
  return fetch(`${notes_base_uri}/${id}`)
    .then(handleResponse);
}

async function createOrUpdate(note) {
  const [ url, method ] = (!note.id || note.id === 'new') 
    ? [notes_base_uri, 'POST']
    : [`${notes_base_uri}/${note.id}`, 'PUT'];

  return fetch(url, {
      method,
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        title: note.title,
        content: note.content,
        tags: note.tags,
        published: note.published
      })})
    .then(handleResponse);
}

export default {
  get,
  list,
  createOrUpdate,
  remove
}