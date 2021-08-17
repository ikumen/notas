<script>
  import { link } from "svelte-routing";

  export let enableFooter = true;
  export let showProfileInHeader = true;
</script>

<style>
  .layout {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-content: stretch;
    /* height: calc(100vh - 60px); */
    height: 100%;
    padding: 0;
    max-width: 100%;
    margin: 0 auto;
    background-color: #eee;
  }

  header {
    height: 50px;
    display: flex;
    align-items: center;
    font-size: 1rem;
    background-color: #eee;
    padding: 0 10px;
  }

  .profile-header {
    background-color: #fff;
  }

  main {
    flex: 1;
    overflow: auto;
    display: flex;
    flex-direction: column;
    margin: 0 4rem;
    padding: 0 10px;
  }

  footer {
    height: 50px;
    background-color: #eee;
    display: flex;
    align-items: center;
    margin: 0 4rem;
    font-size: 1rem;
  }
  
  .notas {
    flex-grow: 0;
    background-color: #000;
    color: #fff;
    font-size: 1.2rem;
    font-weight: 800;
    padding: 4px 6px;
    border-radius: 3px;
    text-decoration: none;
    margin: 0;
    line-height: 1.6rem;
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
  <header class:profile-header={showProfileInHeader}>
    <a class="notas" href="/" use:link>NOTAS</a> 
    <div class="hdr-left">
      <slot name="hdr-left"></slot>
    </div>
    <div class="hdr-right">
      {#if showProfileInHeader}
        <a href="/notes/new" use:link>Create Note</a>
      {:else}
        <slot name="hdr-right"></slot>
      {/if}
    </div>
  </header> 
  <main>
    <slot name="main"/>
  </main>

  {#if enableFooter}
  <footer>
    <slot name="footer"/>
  </footer>
  {/if}
</div>