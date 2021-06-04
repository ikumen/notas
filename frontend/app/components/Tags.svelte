<script>
  import { Link } from "svelte-routing";

  export let tags = [];
</script>

<style>
  .tags {
    display: flex;
    flex-wrap: wrap;
  }
  .tag {
    margin-right: 10px;
  }
</style>

<div class="tags">
{#each tags as tag}
  <span class="tag f5"><span class="silver">#</span><Link class="hover link" to={`/notes/tagged/${tag}`}>{tag}</Link></span>  
{/each}
&nbsp;
</div>  

