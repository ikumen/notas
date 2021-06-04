<script>
  import { link } from "svelte-routing";

  export let enableFooter = true;
  export let fixedMain = false;

</script>

<style>
  header {
    height: 60px;
  }

  .layout {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-content: stretch;
    height: calc(100vh - 60px);
  }

  main {
    padding-top: 60px;
    display: flex;
    flex-direction: column;
  }

  footer {
    height: 50px;
  }

</style>

<div class="pa0 ma0 sans-serif layout">
  <header class="ph1 ph4-m ph6-ns fixed w-100 ma0 f5 tracked flex items-center bg-light-gray">
    <div class="fl dib">
      <a href="/" use:link class="txtwhite ph2 link br1 pv1 dib bg-black f4 fw8 mr2">NOTAS</a>
    </div>
    <div class="fl w-50 pl1 dib black-80">
      <!-- requires pv1 dib for children -->
      <slot name="hdr-menu-lt"></slot>
    </div>
    <div class="fl w-50 dib tr black-80">
      <!-- requires pv1 dib for children -->
      <slot name="hdr-menu-rt"></slot>
    </div>
  </header>
  
  <main class="ma0 ph1 ph4-m ph6-ns" class:pb4={!fixedMain}>
    <slot name="main"></slot>
  </main>

{#if enableFooter}
  <footer class="ph1 ph4-m ph6-ns f5 flex flex-column">
    <div class="bt b--moon-gray">
    </div>
    <div class="flex justify-between pv4">
      <span class="f6">
        &copy; {new Date().getFullYear()} <a class="link" href="//github.com/ikumen">ikumen</a>
      </span>
      <span>
        <a class="link" href="//github.com/komyuniti/notas">about</a>
      </span>  
    </div>
  </footer>  
{/if}
</div>
