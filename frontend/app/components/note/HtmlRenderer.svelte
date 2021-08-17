<script language="typescript">
  import Content from "./Content.svelte";
  import Date from "./Date.svelte";
  import Tags from "./Tags.svelte";
  import Title from "./Title.svelte";
  
  export let note;
</script>

<style>
  .preview {
    flex: 1;
    background-color: lightskyblue;
    margin: 0;
    padding: 0 14px;
    border-radius: 6px;
    border: 1px solid #ddd;
    background-color: #fff;
    overflow: auto;
  }
</style>

<div class="preview">
  <Title bind:title={note.title} />
  <Tags bind:tags={note.tags} />
  <div>
    <Date value={note.createdate} />
  </div>
  <Content bind:content={note.content}  />
</div>
