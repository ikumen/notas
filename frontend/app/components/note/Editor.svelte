<script language="typescript">
  import { makeDebouncer } from "../../utils";
  import ContentEditor from "./ContentEditor.svelte";
  import TagsEditor from "./TagsEditor.svelte";
  import TitleEditor from "./TitleEditor.svelte";
  import NoteService from "../../NoteService";
  import { afterUpdate, onDestroy, onMount } from "svelte";

  export let note;
  let saveTimer;
  let prevNote;
  
  const debouncer = makeDebouncer(10000);

  function setPreviousNote(n) {
    if (n) {
      prevNote = {
        title: n.title.trim(),
        stringifiedTags: JSON.stringify(n.tags),
        content: n.content.trim()
      }
    }
  }

  function isNoteModified() {
    return prevNote == null 
      || prevNote.title !== note.title.trim()
      || prevNote.stringifiedTags !== JSON.stringify(note.tags)
      || prevNote.content !== note.content.trim();
  }

  async function save() {
    if (!isNoteModified())
      return;

    await NoteService.createOrUpdate(note)
      .then(_note => {
        if (note.id === 'new') {
          window.history.replaceState(window.history.state, '', `/notes/${_note.id}/edit`);
          note.id = _note.id;
          note.createdate = _note.createdate;
        }
        note.updatedate = _note.updatedate;
        setPreviousNote(_note);
      });
  }

  onMount(() => {
    setPreviousNote(note);
  });

  afterUpdate(() => {
    if (note) {
      saveTimer = debouncer(save);
    }
  });

  onDestroy(async () => {
    clearTimeout(saveTimer);
    await save();
  });

</script>

<style>
  .editor {
    margin: 0;
    padding: 0 14px;
    border-radius: 6px;
    border: 1px solid #ddd;
    background-color: #fff;
    flex: 1;
    overflow: auto;
  }
</style>

<div class="editor">
  <TitleEditor bind:title={note.title} />
  <TagsEditor bind:tags={note.tags} />
  <ContentEditor bind:content={note.content} />
</div>