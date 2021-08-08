<script>
  export let notes;
  //export let onRemove;
</script>

<div>
  <ul>
    {#each notes as note}
    <li>{note.title}</li>
    {/each}
  </ul>
</div>