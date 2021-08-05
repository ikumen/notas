<script>
  import { onMount, text } from "svelte/internal";
  
  export let content;

  let textAreaEl;

  onMount(() => {
    textAreaEl.onkeydown = (evt) => {
      /* Already explicitly handled */
      if (evt.defaultPrevented) return;

      let handled = false;
      if (evt.key == 'Tab') {
        handled = true;
      }

      if (handled) {
        evt.preventDefault();
      }
    }

    /* Force textarea to resize if needed */
    textAreaEl.dispatchEvent(new Event("input"));
  });
</script>

<style>
  /* auto-resize idea from: https://css-tricks.com/auto-growing-inputs-textareas/ */
  .grow-wrap {
    display: grid;
  }
  .grow-wrap::after {
    /* Note the weird space! Needed to preventy jumpy behavior */
    content: attr(data-replicated-value) " ";
    white-space: pre-wrap;
    /* white-space: normal; */
    /* Hidden from view, clicks, and screen readers */
    visibility: hidden;
  }
  .grow-wrap > textarea {
    /* You could leave this, but after a user resizes, then it ruins the auto sizing */
    resize: none;
    /* Firefox shows scrollbar on growth, you can hide like this. */
    overflow: hidden;
  }
  .grow-wrap > textarea,
  .grow-wrap::after {
    font: inherit;
    /* Place on top of each other */
    grid-area: 1 / 1 / 2 / 2;
  }

  textarea {
    width: 100%;
    height: 100%;    
    margin: 0;
    padding: 0;
    border: 0;
    outline: none;
  }  
</style>

<div class="grow-wrap">
  <textarea id="text"
    bind:this={textAreaEl}
    bind:value={content}
    placeholder="Write your note here..."
    onInput="this.parentNode.dataset.replicatedValue = this.value" 
    name="text" />
</div>
