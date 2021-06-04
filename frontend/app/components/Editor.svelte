<script>
  import { onMount } from "svelte";

  import TagsEditor from "./TagsEditor.svelte";
  import TitleEditor from "./TitleEditor.svelte";
  import ContentEditor from "./ContentEditor.svelte";

  export let note;
  export let scrollHandler;
  export let onChange;

  onMount(() => {
    scrollHandler('editor', document.getElementById('editor_scroller'));
  });
  
</script>

<style>
  #editor_scroller {
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    flex: 1 1 0px;
    border-right: solid 2px #eee;
  }
</style>

<div id="editor_scroller" class="pa2 pa3-m pa4-ns">
  <div class="editor note">
    <TitleEditor bind:title={note.title} />
    <TagsEditor bind:tags={note.tags} />
    <ContentEditor
      {onChange}
      lineNumbers={false}
      content={note.content}
    />
  </div>
</div>
