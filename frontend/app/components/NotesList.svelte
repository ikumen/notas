<script>
  import { link } from "svelte-routing";

  export let notes;
  export let onDeleteNote;

  async function deleteNote(evt, note) {
    evt.preventDefault();
    if (confirm(`Delete "${note.title}"?`)) {
      onDeleteNote(note.id);
    }
  }
</script>

<style>
  .note-list {
    padding: 0;
  }
  .note-item {
    display: flex;
    justify-content: space-between;
  }
</style>

<div>
  <ul class="note-list">
    {#each notes as note}
    <li class="note-item">
      <a href={`/notes/${note.id}`} use:link>{note.title}</a>
      <div>
        <a href={`/notes/${note.id}/delete`} on:click={(evt) => deleteNote(evt, note)}>Delete</a>
        <a href={`/notes/${note.id}/edit`} use:link>Edit</a>
      </div>
    </li>
    {/each}
  </ul>
</div>