<script>
  export let note;
</script>

<style>
  .published {
    background-color: limegreen;
  }
  .draft {
    background-color: cornflowerblue;
  }
</style>

<div title="Toggle Privacy" 
    on:click={() => note.published = !note.published} 
    class:draft={!note.published} 
    class:published={note.published}
    >
  {#if note} Published {:else} Draft {/if}
</div>
