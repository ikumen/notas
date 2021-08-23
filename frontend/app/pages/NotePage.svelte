<script>
  import Date from "../components/note/Date.svelte";
  import HtmlRenderer from "../components/note/HtmlRenderer.svelte";
  import NoteService from "../NoteService";
  import PageLayout from "../support/PageLayout.svelte";


  export let id;

  async function loadNote() {
    return await NoteService.get(id);
  }
</script>

<style>
  .meta {
    display: flex;
    justify-content: flex-start;
    margin: 30px 0;
  }

  .meta span {
    margin-right: 10px;
  }
</style>

<PageLayout enableFooter={true}>
  <div slot="main" class="container">
  {#await loadNote()}
    ..loading
  {:then note} 
    <HtmlRenderer {note}>
      <div slot="meta" class="meta">
        <span><a href={`/@${note.user}`}>@{note.user}</a></span>
        <span>&middot;</span>
        <span><Date value={note.createdate} /></span>
        <span>
          {#if note.published} 
            published 
          {:else}
            draft
          {/if}
        </span>
        <span><a href={`/notes/${note.id}/edit`}>edit</a></span>
      </div>
    </HtmlRenderer>  
  {/await}
  </div>
</PageLayout>