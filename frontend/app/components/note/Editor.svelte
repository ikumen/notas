<script>
  import ContentEditor from "./ContentEditor.svelte";
  import TagsEditor from "./TagsEditor.svelte";
  import TitleEditor from "./TitleEditor.svelte";

  export let note;
</script>

<style>
  .editor {
    margin: 0;
    padding: 0 4px;
    border-radius: 6px;
    border: 1px solid #ddd;
    background-color: #fff;
    flex: 1;
    overflow: auto;
  }
</style>

<div class="editor">
  <TitleEditor bind:title={note.title} />
  <TagsEditor bind:tags={note.tags} />
  <ContentEditor bind:content={note.content} />
</div>