<script>
  import { toLocaleStringSupported } from "../../utils";

  export let note;

  const localeOptions = { 
    year: 'numeric', month: 'short', 
    day: 'numeric', hour: 'numeric', 
    minute: 'numeric', second: 'numeric' 
  };

</script>

<div class="mr2">
  Updated:
  {#if note}
    {#if toLocaleStringSupported()}
      {new Date(note.updatedate).toLocaleString(navigator.languages[0], localeOptions)}
    {:else}
      {new Date(note.updatedate).toLocaleString()}
    {/if}
  {:else}
    nothing saved
  {/if}
</div>
