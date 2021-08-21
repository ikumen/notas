<script>
import HtmlRenderer from "../components/note/HtmlRenderer.svelte";

import NoteService from "../NoteService";
import PageLayout from "../support/PageLayout.svelte";


  export let id;

  async function loadNote() {
    return await NoteService.get(id);
  }
</script>

<PageLayout enableFooter={true}>
  <div slot="main" class="container">
  {#await loadNote()}
    ..loading
  {:then note} 
    <HtmlRenderer {note}/>  
  {/await}
  </div>
</PageLayout>