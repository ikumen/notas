<script>
  import { Router, Route } from "svelte-routing";
  import EditNotePage from "./pages/NoteEditorPage.svelte";
  import HomePage from "./pages/HomePage.svelte";

</script>

<Router>
  <Route path="/notes/new">
    <EditNotePage id="new" />
  </Route>
  <Route path="*" component={HomePage} />
</Router>