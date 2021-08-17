<script>
  import { Router, Route } from "svelte-routing";
  import HomePage from "./pages/HomePage.svelte";
  import NoteEditorPage from "./pages/NoteEditorPage.svelte";
  import NotePage from "./pages/NotePage.svelte";
</script>

<Router>
  <Route path="/notes/new">
    <NoteEditorPage id="new" />
  </Route>
  <Route path="/notes/:id/edit" let:params>
    <NoteEditorPage id={params.id} />
  </Route>
  <Route path="/notes/:id/delete" let:params>
    <HomePage id={params.id} />
  </Route>
  <Route path="/notes/:id" let:params>
    <NotePage id={params.id} />    
  </Route>
  <Route path="*" component={HomePage} />
</Router>