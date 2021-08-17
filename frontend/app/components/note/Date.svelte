<script>
  import { toLocaleStringSupported } from "../../utils";

  export let value;
  export let shortFormat = true;
  export let placeholder = "";

  const localeOptions = {month: 'short', day: '2-digit', year: 'numeric'}
  if (!shortFormat) {
    localeOptions.day = 'numeric';
    localeOptions.hour = 'numeric';
    localeOptions.minute = 'numeric';
    localeOptions.second = 'numeric';
  }
</script>

<style>
  .date {
    font-size: 1rem;
    color: #666;
  }
</style>

<div class="date">
  {#if value}
    {#if toLocaleStringSupported()}
      {new Date(value).toLocaleString(navigator.languages[0], localeOptions)}
    {:else}
      {new Date(value).toLocaleString()}
    {/if}
  {:else}
    {placeholder}
  {/if}
</div>
