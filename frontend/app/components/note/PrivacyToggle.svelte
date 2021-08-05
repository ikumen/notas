<script>
  export let ispublic;
</script>

<div title="Toggle Privacy" 
    on:click={() => ispublic = !ispublic} 
    class:bg-blue={!ispublic} 
    class:bg-orange={ispublic}>
  {#if ispublic} Public {:else} Private {/if}
</div>
