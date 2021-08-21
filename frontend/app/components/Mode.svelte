<script>
  export let mode;
  export let name;
  export let value;
</script>

<style>
  .unselected {
    color: #aaa;
  }

  .selected, .unselected:hover {
    border-bottom: solid 2px rgb(0, 0, 238);
    color: #111;
  }

  .mode:hover {
    cursor: pointer;
  }

  .mode {
    font-size: 1rem;
    padding: 2px 0;
    margin-right: 14px;
  }
</style>

<div class="mode"
    class:unselected={mode !== value}
    class:selected={mode === value}
    on:click={() => mode = value}
  >{name}</div>
