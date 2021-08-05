<script>
  import { link } from "svelte-routing";

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
    padding: 0 10px;
    max-width: 100%;
    margin: 0 auto;
    background-color: #eee;
  }

  header {
    height: 50px;
    display: flex;
    align-items: center;
    font-size: 1rem;
  }

  main {
    flex: 1;
    overflow: auto;
    display: flex;
    flex-direction: column;
    margin: 0 4rem;
  }

  footer {
    height: 50px;
    background-color: #eee;
    display: flex;
    align-items: center;
    margin: 0 4rem;
    font-size: 1rem;
  }
  
  .logo {
    flex-grow: 1;
  }
  .logo .notas {
    background-color: #000;
    color: #fff;
    font-size: 1.2rem;
    font-weight: 800;
    padding: 6px 6px 4px;
    border-radius: 3px;
  }

  .hdr-left, .hdr-right {
    flex-grow: 2;
  }

  @media (max-width: 1024px) {
    main, footer {
      margin: 0;
    }
  }
</style>

<div class="layout">
  {#if enableHeader}
  <header>
    <div class="logo">
      <a href="/" use:link><span class="notas">NOTAS</span></a> 
    </div>
    <div class="hdr-left">
      <slot name="hdr-left"></slot>
    </div>
    <div class="hdr-right">
      <slot name="hdr-right"></slot>
    </div>
  </header> 
  {/if}
  <main>
    <slot name="main"/>
  </main>

  {#if enableFooter}
  <footer>
    <slot name="footer"/>
  </footer>
  {/if}
</div>