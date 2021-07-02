<script>
  export let notes;
  //export let onRemove;
</script>

<div>
  <ul>
    {#each notes as note}
    <li>{notes.title}</li>
    {/each}
  </ul>
</div>