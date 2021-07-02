<script>
  import { Router, Route } from "svelte-routing";
  import HomePage from "./pages/HomePage.svelte";

</script>

<Router>
  <Route path="*" component={HomePage} />
</Router>