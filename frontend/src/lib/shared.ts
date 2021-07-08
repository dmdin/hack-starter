import {Bridge} from '$lib/bridge';
import {writable} from "svelte/store";
import {browser} from "$app/env";

import * as cookie from './bridge/cookies'

export const bridge = new Bridge('http://localhost:8000', 'token')

// FIXME fix problem with updating the token
export const token = writable(browser ? cookie.get('token') : null);
const tokenExpiration = 1000 * 60 * 30;
export let tokenTimer;

token.subscribe(v => {
  if (v) {
    const now = new Date();
    now.setTime(now.getTime() + tokenExpiration);
    browser ? cookie.set('token', v, {SameSite: 'Strict', expires: now.toUTCString()}) : null;
  } else {
    browser ? cookie.del('token') : null;
  }
});
