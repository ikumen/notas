<script>
  import { Router, Route } from "svelte-routing";
import EditNotePage from "./pages/EditNotePage.svelte";
  import HomePage from "./pages/HomePage.svelte";

</script>

<Router>
  <Route path="/edit" component={EditNotePage} />
  <Route path="*" component={HomePage} />
</Router>