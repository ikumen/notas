<script>
  import { Router, Route } from "svelte-routing";
  import UserPage from "./pages/UserPage.svelte";
  import HomePage from "./pages/HomePage.svelte";
  import NotePage from "./pages/NotePage.svelte";
  import NoteEditPage from "./pages/NoteEditPage.svelte";
</script>

<Router>
  <Route path="/@:user" component={UserPage} />
  <Route path="/notes/new">
    <NoteEditPage id="new" />
  </Route>
  <Route  path="/notes/tagged/:tags" let:params>
    <HomePage tags={params.tags} />
  </Route>
  <Route path="/notes/:id/edit" let:params>
    <NoteEditPage id={params.id} />
  </Route>
  <Route path="/notes/:id" let:params>
    <NotePage id={params.id} />
  </Route>
  <Route path="*" component={HomePage} />
</Router>

