<script>
  export let title;
  export let placeholder = 'Note title here...';
</script>

<style>
  .title {
    display: block;
    font-size: 2rem;
    font-weight: 800;
    outline: none;
    border: none;
    margin: 1rem 0;
    width: 99%;
  }

</style>

<input bind:value={title} class="title" 
  placeholder={placeholder}
/>


