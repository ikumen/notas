<script>
  export let ispublic;
</script>

<div class="dib dim pointer white pv2 ph3 br1 f7 fw4 mr2" title="Toggle Privacy" 
    on:click={() => ispublic = !ispublic} 
    class:bg-blue={!ispublic} 
    class:bg-orange={ispublic}>
  {#if ispublic} Public {:else} Private {/if}
</div>
