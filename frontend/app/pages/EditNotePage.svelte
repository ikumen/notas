<script>
  import PageLayout from "../support/PageLayout.svelte";
  import AutoResizeTextArea from "../components/AutoResizeTextArea.svelte";
  import HtmlView from "../components/HtmlView.svelte";

  let content = '';
</script>

<style>
  .container {
    display: flex;
    flex-direction: row;
    height: 100%;
    overflow:hidden;
    padding: 0;
    margin: 0;
  }

  .preview {
    flex: 1;
    background-color: lightskyblue;
    margin: 0;
    padding: 0;
    overflow: auto;
  }

  .editor {
    margin: 0;
    padding: 0 10px;
    flex: 1;
    background-color: #eee;
    overflow: auto;
  }
</style>

<PageLayout>
  <div slot="main" class="container">
    <div class="editor">
      <h1>some test</h1>
      <AutoResizeTextArea bind:content />
    </div>
    <div class="preview">
      <HtmlView bind:content  />
    </div>
  </div>
</PageLayout>