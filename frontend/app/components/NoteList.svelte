<script>
  import { Link } from 'svelte-routing'; 
  import Tags from './Tags.svelte';

  export let notes;
  export let onRemove;

</script>

<style>
  .bbtm {border-bottom: solid 1px #ddd;}
  .btop {border-top: solid 1px #ddd;}
</style>

<div class="ma0 pa0">
  <ul class="list ma0 pa0 bbtm">
    {#each notes as note}
      <li class="w-100 bg-white hover-bg-near-white ph2 pv3 btop">
        <div class="flex justify-between w-100 items-center">
          <div>
            <Link class="hover link f4 fw7" to={`/notes/${note.id}`}>{note.title}</Link>
            <Tags tags={note.tags} />    
          </div>
          <div class="f5 nowrap">
            <Link to={`/notes/${note.id}/edit`} class="br2 link pv2 pr2 pointer">Edit</Link>
            <span class="red br2 pv2 pl2 dim pointer" on:click={() => onRemove(note.id)}>Delete</span>
          </div>
        </div>
      </li>    
    {/each} 
  </ul>
</div>
