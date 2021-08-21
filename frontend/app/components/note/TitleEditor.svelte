<script>
  export let title;
  export let placeholder = 'Note title here...';
</script>

<style>
  .title[contenteditable]:empty::before {
    content: attr(data-placeholder);
    color: gray;
  }

  .title {
    font-size: 2rem;
    font-weight: 800;
    border: none;
    width: 99%;
    outline: none;
  }

</style>

<h1 role="textbox" class="title" 
  contenteditable="true"
  bind:textContent={title} 
  data-placeholder={placeholder}
/>


