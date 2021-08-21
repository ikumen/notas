<script>
  import { link } from "svelte-routing";

  export let enableFooter = true;
  export let showProfileInHeader = true;
</script>

<style>
  .layout {
    display: flex;
    flex-direction: column;
    align-items: center;
    align-content: stretch;
    justify-content: space-between;
    height: 100%;
    padding: 0;
    max-width: 1100px;
    margin: 0 auto;
  }

  header, main, footer {
    width: 100%;
  }

  header, footer {
    height: 50px;
    font-size: .9rem;
    display: flex;
    align-content: center;
  }

  footer section, header section {
    display: flex;
    width: 100%;
    align-items: center;
    justify-content: space-between;
  }

  header {
    border-bottom: 1px solid #ddd;
  }

  .branding {
    flex-grow: 0;
    padding: 2px 0px;
    margin: 0;
  }

  .branding a {
    line-height: 1.6rem;
    text-decoration: none;
    color: #111;
    font-size: 1.2rem;
    font-weight: 600;
    padding: 2px 0;
    border-bottom: solid 3px rgb(0, 0, 238);
  }

  main {
    padding-top: 20px;
    flex: 1;
    overflow: auto;
    display: flex;
    flex-direction: column;
  }
  
  .hdr-left, .hdr-right {
    flex-grow: 2;
  }

  @media (max-width: 1110px) {
    .layout {
      padding: 0 14px;
    }
  }
</style>

<div class="layout">
  <header>
    <section>
    <div class="branding"><a href="/" use:link>NOTAS</a></div>
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
    </section>
  </header> 
  <main>
    <slot name="main"/>
  </main>

  {#if enableFooter}
  <footer>
    <section>
      <slot name="footer">
        <div>
        </div>
        <div>
          <a href="https://github.com/komyuniti/notas">about</a>
        </div>
      </slot>
    </section>
  </footer>
  {/if}
</div>