<script>
  export let enableFooter = true;
  export let enableHeader = true;
</script>

<style>
  .container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-content: stretch;
    height: calc(100vh - 60px);
  }

  header {
    height: 60px;
    background-color: #ddd;
  }

  main {
    padding-top: 60px;
    display: flex;
    flex-direction: column;
    background-color: tan;
  }

  footer {
    height: 50px;
    background-color: #eee;
  }
</style>

<div class="container">
  {#if enableHeader}
  <header>
    header
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