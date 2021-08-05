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
    border-bottom: solid 2px #357EDD;
    color: #333;
  }
  .mode:hover {
    cursor: pointer;
  }
  .mode {
    margin-right: 14px;
  }
</style>

<div class="mode"
    class:unselected={mode !== value}
    class:selected={mode === value}
    on:click={() => mode = value}
  >{name}</div>
