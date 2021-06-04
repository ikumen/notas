<script>
  import { isToLocaleStringSupported } from "../helpers";

  export let updatedAt;

  const localeOptions = { 
    year: 'numeric', month: 'short', 
    day: 'numeric', hour: 'numeric', 
    minute: 'numeric', second: 'numeric' 
  };

</script>

<div class="mr2">
  Updated:
  {#if updatedAt}
    {#if isToLocaleStringSupported()}
      {new Date(updatedAt).toLocaleString(navigator.languages[0], localeOptions)}
    {:else}
      {new Date(updatedAt).toLocaleString()}
    {/if}
  {:else}
    nothing to save
  {/if}
</div>
