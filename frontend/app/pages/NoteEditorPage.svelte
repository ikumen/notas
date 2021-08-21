<script language="typescript">
  import PageLayout from "../support/PageLayout.svelte";
  import NoteService from "../NoteService";
  import { Editor, HtmlRenderer } from "../components/note";
  import Mode from "../components/Mode.svelte";
  import PublishToggle from "../components/note/PublishToggle.svelte";
  import LastUpdated from "../components/note/LastUpdated.svelte";
import { link } from "svelte-routing";

  export let id;

  let mode = 2;

  $: note = (async () => {
    if (id === 'new') {
      note = await Promise.resolve({id, title: '', tags: [], published: false, content: ''});
    } else {
      note = await NoteService.get(id);
    }
  })();   
  

</script>

<style>
  .container {
    display: flex;
    flex-direction: row;
    height: 100%;
    overflow:hidden;
    padding: 0;
    margin: 0;
  }
  
  .meta {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .modes {
    display: flex;
    justify-content: flex-end;
    align-items: center;
  }

  .divider {
    width: 14px;
    border-left: 1px solid #ccc;
    margin-left: 1px;
    margin-right: 1px;
    background-color: #fff;
  }

  .done {
    text-decoration: none;
    margin-left: 10px;
    border: none;
    color: #111;
    font-weight: 400;
    font-size: 1.1rem;
    padding: 4px 10px;
    background-color: #eee;
  }
</style>

<PageLayout enableFooter={true} showProfileInHeader={false}>
  <div class="modes" slot="hdr-right">
    <Mode bind:mode={mode} value={1} name="Edit" />
    <Mode bind:mode={mode} value={2} name="Split" />
    <Mode bind:mode={mode} value={3} name="Preview" />

    <a href="/" use:link class="done">X</a>
  </div>
  <div slot="main" class="container">
  {#await note}
    ..loading
  {:then} 
    {#if mode < 3} <Editor bind:note={note} /> {/if}
    {#if mode == 2} <div class="divider"></div> {/if}
    {#if mode > 1} <HtmlRenderer bind:note={note} /> {/if}
  {/await}
  </div>
  <div slot="footer" class="meta">
    {#await note then note}
      <div><PublishToggle {note} /></div>
      <div><LastUpdated {note} /></div>
    {/await}
  </div>
</PageLayout>