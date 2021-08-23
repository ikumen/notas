<script language="typescript">
  import Content from "./Content.svelte";
  import Tags from "./Tags.svelte";
  import Title from "./Title.svelte";
  
  export let note;
</script>

<style>
  .rendered {
    flex: 1;
    margin: 0;
    padding: 0;
    background-color: #fff;
    overflow: auto;
  }

</style>

<div class="rendered">
  <Title bind:title={note.title} />
  <Tags bind:tags={note.tags} />
  <slot name="meta" />
  <Content bind:content={note.content}  />
</div>
