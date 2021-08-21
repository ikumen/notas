<script>
  import { toLocaleStringSupported } from "../../utils";

  export let note;

  const localeOptions = { 
    year: 'numeric', month: 'short', 
    day: 'numeric', hour: 'numeric', 
    minute: 'numeric', second: 'numeric' 
  };

</script>

<style>
  .lastupdated {
    color: #aaa;
  }
</style>

<div class="lastupdated">
  Last updated:
  {#if note && note.updatedate}
    {#if toLocaleStringSupported()}
      {new Date(note.updatedate).toLocaleString(navigator.languages[0], localeOptions)}
    {:else}
      {new Date(note.updatedate).toLocaleString()}
    {/if}
  {:else}
    New
  {/if}
</div>
