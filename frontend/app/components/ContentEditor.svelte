<script lang="ts">
  import { onDestroy, onMount } from 'svelte';

  import CodeMirror from 'codemirror';
  import 'codemirror/mode/markdown/markdown';
  import 'codemirror/mode/python/python';
  import 'codemirror/mode/javascript/javascript';
  import 'codemirror/mode/shell/shell';
  import 'codemirror/addon/display/placeholder';
  import './codemirror.css';

  import { makeDebouncer } from '../helpers';

  export let lineNumbers = false;
  export let content = '';
  export let onChange;

  let timer;
  let editor: CodeMirror;

  const debouncer = makeDebouncer(500);

  function createEditor(options) {
    if (!editor) {
      editor = CodeMirror.fromTextArea(document.getElementById('cmeditor'), options);
      editor.on('change', (cm, ch) => {
        timer = debouncer(() => onChange(cm.getValue()));
      });
    }
  }

  onMount(() => {
    createEditor({
      lineNumbers,
      scrollbarStyle: null,
      lineWrapping: true,
      extraKeys: {Tab: false, "Shift-Tab": false},
      mode: {
        name: 'markdown', 
        fencedCodeBlockDefaultMode: 'javascript'
      },
      // viewportMargin: Infinity
    });
  });

  onDestroy(() => clearTimeout(timer));
</script>

<textarea id="cmeditor" style="display: none;" placeholder="Write content here...">{content}</textarea>
