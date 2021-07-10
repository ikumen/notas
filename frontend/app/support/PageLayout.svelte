<script>
  export let enableFooter = true;
  export let enableHeader = true;
</script>

<style>
  .layout {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-content: stretch;
    /* height: calc(100vh - 60px); */
    height: 100%;
  }

  header {
    height: 60px;
    background-color: #ddd;
  }

  main {
    flex: 1;
    overflow: auto;
    /* padding-top: 60px; */
    display: flex;
    flex-direction: column;
    background-color: tan;
  }

  footer {
    height: 50px;
    background-color: #eee;
  }
</style>

<div class="layout">
  {#if enableHeader}
  <header>
    notas
  </header> 
  {/if}

  <main>
    <slot name="main"/>
  </main>

  {#if enableFooter}
  <footer>

  </footer>
  {/if}
</div>