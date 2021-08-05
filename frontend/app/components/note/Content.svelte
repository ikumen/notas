<script>
  import micromark from "micromark";
  import gfmSyntax from "micromark-extension-gfm";
  import gfmHtml from "micromark-extension-gfm/html";
  
  export let content;

  $: rendered = micromark(content, {
    allowDangerousHtml: true,
    extensions: [gfmSyntax()],
    htmlExtensions: [gfmHtml]
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
