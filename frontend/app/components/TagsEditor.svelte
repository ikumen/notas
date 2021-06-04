<script>
  export let tags = [];
  export let placeholder = 'Add up to 5 tags...';

  let joinedTags = tags.join(', ');

  function parseInputToTags(evt) {
    tags = evt.target.innerText
      .split(',')         // separate into individual tags
      .map(t => t.trim()) // cleanup
      .filter(t => t !== '') // cleanup
      .map(t => t.replaceAll(/[^a-zA-Z0-9]/g,'')) // only alphanumeric chars allowed
      .reduce((tags, t) => {
        if (!tags.includes(t))
          tags.push(t);
        return tags;
      }, []);
  }

</script>

<style>
  .tags[contenteditable]:empty::before {
    content: attr(data-placeholder);
    color: gray;
  }
  .tags {
    /* hack to bump codemirror down a note */
    width: 100%;
    display: block;
  }
</style>

<span role="textbox" class="tags" contenteditable 
  on:input={parseInputToTags} 
  bind:textContent={joinedTags} 
  data-placeholder={placeholder}
/>

