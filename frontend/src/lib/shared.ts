import {Bridge} from '$lib/bridge';
import {writable} from "svelte/store";
import {browser} from "$app/env";

import * as cookie from './bridge/cookies'

export const bridge = new Bridge('http://localhost:8000', 'token')
export const token = writable(browser ? cookie.get('token') : null);

token.subscribe(v => {
  if (v) {
    browser ? cookie.set('token', v, {SameSite: 'Strict'}) : null;
  } else {
    browser ? cookie.del('token') : null;
  }
});
