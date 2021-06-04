<script>
  import Viewer from '../components/Viewer.svelte';
  import PageLayout from '../components/PageLayout.svelte';
  import NoteService from '../services/NoteService';

  export let id; 
</script>

<style>
  .viewer {
    display: flex;
    flex-direction: row;
    background-color: #fff;
  }
</style>

<PageLayout>
  <div class="pv1" slot="hdr-menu-lt">
  </div>
  <div class="viewer mt2" slot="main">
      {#await NoteService.get(id)}
        ...loading note
      {:then note} 
        <Viewer {note} />
      {:catch}
        <h3>Doh, looks like we're having some issues please try again later</h3>
      {/await}
  </div>
</PageLayout>
