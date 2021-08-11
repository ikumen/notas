<script>
import { Link } from "svelte-routing";

  export let notes;
  //export let onRemove;
</script>

<style>
  .note-item {
    display: flex;
    justify-content: space-between;
  }
</style>

<div>
  <ul>
    {#each notes as note}
    <li class="note-item">
      <Link to={`/notes/${note.id}`}>{note.title}</Link>
      <div>
        <span>Delete</span>
        <span>edit</span>
      </div>
    </li>
    {/each}
  </ul>
</div>