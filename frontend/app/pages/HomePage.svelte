<script>
  import { onMount } from "svelte";
  import { Link } from "svelte-routing";
  
  import NoteList from "../components/NoteList.svelte";
  import PageLayout from "../components/PageLayout.svelte";
  import NoteService from "../services/NoteService";

  export let tags;

  let notes = [];

  async function allNotes(tags) {
    notes = await NoteService.all({tags}); 
  }

  async function onRemove(id) {
    NoteService.remove(id)
      .then(() => {
        notes = notes.filter(note => note.id !== id);
      });
  }

</script>

<PageLayout>
  <div slot="hdr-menu-lt" class="pv1 dib black-80">
  </div>
  <div slot="hdr-menu-rt" class="pv1 dib black-80">
    <Link to={"/notes/new"} class="link f6 br1 pv2 ph2 dim txtwhite bg-green">Create</Link>
  </div>
  <div slot="main" class="main">
    <h3 class="dark-gray fw5">All your notes 
      {#if tags}
        tagged "{tags}" <span class="gray f5">(<Link to="/notes" class="link">clear</Link>)</span>
      {/if}
    </h3>
    {#await allNotes(tags)}
      ...loading notes
    {:then} 
      <NoteList bind:notes={notes} {onRemove} />       
    {/await}
  </div>
</PageLayout>
