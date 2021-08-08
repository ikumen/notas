<script>
  import PageLayout from "../support/PageLayout.svelte";
  import NoteService from "../NoteService";
  import NotesList from "../components/NotesList.svelte";

  let notes = [];
  
  async function listNotes() {
    notes = await NoteService.list();
  }

</script>


<PageLayout>
  <div slot="main">
    {#await listNotes()}
      ...loading notes
    {:then} 
      <NotesList bind:notes={notes} />
    {/await}
  </div>
</PageLayout>