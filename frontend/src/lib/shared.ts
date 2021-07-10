import {Bridge} from '$lib/bridge';
import {writable} from 'svelte/store';


// export const bridge = new Bridge('http://localhost:8000')
export const bridge = new Bridge('https://b.hackmasters.tech/')
export const errorLabel = writable(null);
errorLabel.subscribe(v => {
  if (v) {
    setTimeout(() => errorLabel.set(null), 4000)
  }
});