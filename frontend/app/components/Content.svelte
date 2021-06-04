<script>
  import micromark from "micromark";
  import gfmSyntax from "micromark-extension-gfm";
  import gfmHtml from "micromark-extension-gfm/html";
  import hljs from 'highlight.js'
  //import 'highlight.js/styles/stackoverflow-dark.css';
  import 'highlight.js/styles/sunburst.css';
  //import 'highlight.js/styles/tomorrow-night-bright.css';
  import { afterUpdate } from "svelte";

  export let content;

  $: rendered = micromark(content, {
    allowDangerousHtml: true,
    extensions: [gfmSyntax()],
    htmlExtensions: [gfmHtml]
  });

  afterUpdate(() => {
    hljs.highlightAll();
  });
</script>

<style>
  .content {
    margin: 0;
    padding: 0;
    max-width: 100%;
    overflow-wrap: break-word;
  }
</style>

<div class="content">
  {@html rendered}
</div>
