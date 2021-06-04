<script>
  import { onMount } from "svelte";

  import Tags from "./Tags.svelte";
  import Title from "./Title.svelte";
  import Content from "./Content.svelte";

  export let note;
  export let scrollHandler;

  onMount(() => {
    if (scrollHandler) {
      scrollHandler('preview', document.getElementById('preview_scroller'));
    }
  });

</script>

<style>
  #preview_scroller {
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    overflow-wrap: break-word;
    flex: 1 1 0px;
    background-color: #fff;
  }
  .preview {
    padding-bottom: 30px;
  }
</style>

<div id="preview_scroller" class="pa2 pa3-m pa4-ns">
  <div class="preview note">
    <Title title={note.title} />
    <Tags tags={note.tags} />
    <Content content={note.content} />
  </div>
</div>
