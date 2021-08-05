function makeDebouncer(delay) {
  let timer;
  return function(fn) {
    clearTimeout(timer);
    timer = setTimeout(fn, delay);
    return timer;
  }
}

function setHistoryState({state = window.history.state, title = '', url}, replace = true) {
  if (replace) {
    window.history.replaceState(state, '', url);
  } else {
    window.history.pushState(state, title, url);
  }
}

function toLocaleStringSupported() {
  try { new Date().toLocaleString('i'); } 
  catch (e) { return e.name === 'RangeError';}
  return false;
}

export { 
  makeDebouncer, 
  toLocaleStringSupported,
  setHistoryState
};
