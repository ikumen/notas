<script>
  import PageLayout from "../support/PageLayout.svelte";
  import NoteService from "../NoteService";
  import NotesList from "../components/NotesList.svelte";

  let notes = [];
  
  async function listNotes() {
    notes = await NoteService.list();
  }

  async function deleteNote(id) {
    NoteService.remove(id).then(() => {
      notes = notes.filter(note => note.id !== id);
    });
  }

</script>


<PageLayout>
  <div slot="main">
    {#await listNotes()}
      ...loading notes
    {:then} 
      <h2>Notes</h2>
      <NotesList bind:notes={notes} onDeleteNote={deleteNote} />
    {/await}
  </div>
</PageLayout>