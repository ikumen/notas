<script>
  import { afterUpdate, onDestroy } from 'svelte';
  
  import Editor from '../components/Editor.svelte';
  import LastUpdated from '../components/LastUpdated.svelte';
  import Mode from '../components/Mode.svelte';
  import PageLayout from '../components/PageLayout.svelte';
  import PrivacyToggle from '../components/PrivacyToggle.svelte';
  import Viewer from '../components/Viewer.svelte';
  import NoteService from '../services/NoteService';
  import { link } from 'svelte-routing';
  import '../components/note.css';
  import { makeDebouncer } from '../helpers';
  
  export let id;

  let mode = 2;
  let note;

  let saveTimer;
  let lastSavedNote;
  const debouncer = makeDebouncer(10000);

  let scrollables = {};
  
  function registerScrollable(refId, ref) {
    scrollables[refId] = ref;
    ref.onscroll = function (evt) {
      //TODO: sync scroll
    }
  }

  function onContentChange(content) {
    note.content = content;
  }

  /**
   * Capture current note attr values for later dirty checks to determine
   * if an auto save action is required.
   * @param note
   */
  function setLastSavedNote(note) {
    if (note) {
      lastSavedNote = {
        title: note.title,
        stringifiedTags: JSON.stringify(note.tags),
        content: note.content,
        ispublic: note.ispublic
      }
    }
  }

  /**
   * Return either an empty "new" note for editing or an existing note
   * from the server is it's a valid id.
   * @param id
   */
  async function getNote(id) {
    if (id === 'new') {
      note = {id, title: '', tags: [], ispublic: false, content: ''};
    } else {
      note = await NoteService.get(id);
    }
    // Capture note attr values, used to check if editor dirty and needs save
    setLastSavedNote(note);
  }

  /**
   * Returns boolean indicating if current note values differ since last save.
   * @param before
   * @param curr
   */
  function shouldSave(last, curr) {
    return (last && curr && (
      (last.title.trim() !== curr.title.trim())
        || (last.stringifiedTags !== JSON.stringify(curr.tags))
        || (last.content !== curr.content)
        || (last.ispublic !== curr.ispublic)));
  }

  async function save() {
    if (shouldSave(lastSavedNote, note)) {
      await NoteService.createOrUpdate(note)
        .then(newNote => {
          if (note.id === 'new') {
            window.history.replaceState(window.history.state, '', `/notes/${newNote.id}/edit`);
            note.id = newNote.id;
            note.created_at = newNote.created_at;
          }
          note.updated_at = newNote.updated_at;
          setLastSavedNote(newNote);
        });
    }
  }

  afterUpdate(() => {
    if (note) {
      saveTimer = debouncer(save);
    }
  })

  onDestroy(async () => {
    clearTimeout(saveTimer);
    await save();
  });

</script>

<style>
  .editor-viewer {
    display: flex;
    flex-direction: row;
    height: calc(100vh - 110px);
    background-color: #fff;
  }
  .editor-controls {
    height: 50px;
  }
</style>

<PageLayout enableFooter={false} fixedMain={true}>
<div slot="hdr-menu-lt" class="pv1 dib black-80">
  Editing Note
</div>
<div slot="hdr-menu-rt" class="pv1 dib black-80">
  <Mode bind:mode={mode} value={1} name="Edit" />
  <Mode bind:mode={mode} value={2} name="Split" />
  <Mode bind:mode={mode} value={3} name="Preview" />
  <a href="/" use:link class="link txtdark f6 ml3 pointer br1 pv2 ph2 dim bg-moon-gray">Done</a>
</div>
<div slot="main" class="main">
  {#await getNote(id)}
    ..loading
  {:then} 
    {#if note}
    <div class="editor-viewer">
      {#if mode < 3}
      <Editor bind:note={note} 
        scrollHandler={registerScrollable} 
        onChange={onContentChange}
      />
      {/if}
      {#if mode > 1}
      <Viewer bind:note={note}
        scrollHandler={registerScrollable} 
      />
      {/if}
    </div>
    <div class="editor-controls flex justify-between items-center f5 fw6">
      <div class="fl">
        <PrivacyToggle bind:ispublic={note.ispublic} />
      </div>
      <div class="fr gray f6 fw2">
        <LastUpdated updatedAt={note.updated_at} />
      </div>
    </div>
    {/if}
  {:catch}
    ..Oh noes
  {/await}
</div>
</PageLayout>
