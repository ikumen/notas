<script>
  export let title;
  export let placeholder = 'Add title here...';
</script>

<style>
  .title[contenteditable]:empty::before {
    content: attr(data-placeholder);
    color: gray;
  }
  .title {
    display: block;
  }
</style>

<span contenteditable class="title" 
  bind:textContent={title} 
  data-placeholder={placeholder}
/>


