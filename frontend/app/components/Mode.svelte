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
</style>

<div class="link dib pointer pv1 mh1"
    class:unselected={mode !== value}
    class:selected={mode === value}
    on:click={() => mode = value}
  >{name}</div>
