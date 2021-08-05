const notes_base_uri = '/api/notes';

function handleResponse(res: Response) {
  if (res.ok)
    return res.json();

  let errorMessage = 'Sorry we could not complete request, please try again.'
  if (res.status === 404)
    errorMessage = `Note not found`;
  if (res.status < 500)
    errorMessage = `Invalid request`;
  throw new Error(errorMessage);
}

export async function remove(id: string) {
  return fetch(`${notes_base_uri}/${id}`, {
      method: 'DELETE'
    }).then(handleResponse);
}

export async function list() {
  return fetch(`${notes_base_uri}`)
    .then(handleResponse);
}

export async function get(id: string) {
  return fetch(`${notes_base_uri}/${id}`)
    .then(handleResponse);
}

export async function createOrUpdate(note) {
  let url = notes_base_uri;
  let method = 'POST';

  // if existing note, do update
  if (note.id && note.id !== 'new') {
    url = `${url}/${note.id}`;
    method = 'PUT';
  }

  return fetch(url, {
      method,
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(note)
    })
    .then(handleResponse);
}
