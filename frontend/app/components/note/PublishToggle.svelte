<script>
  export let note;
</script>

<style>
  .toggle {
    padding: 4px 8px;
    padding-right: 12px;
    text-align: center;
    border-radius: 3px;
    display: flex;
    align-items: center;
    background-color: #ddd;
  }

  .toggle:hover {
    cursor: pointer;
  }

  .published {
    background-color: orangered;
    color: #fff;
  }

  .toggle div {
    margin-left: 10px;
  }

</style>

<div class="toggle" class:published={note.published}>
  <input type="checkbox" bind:checked={note.published} />
  <div title="Toggle to Publish / Unpublish" 
      on:click={() => note.published = !note.published} 
      class:draft={!note.published} 
      class:published={note.published}
      >
    {#if note.published} Published {:else} Draft {/if}
  </div>
</div>