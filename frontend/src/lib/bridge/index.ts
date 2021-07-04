import {FetchParams, initValues, Methods, storeFetch} from './customFetch';
import {writable} from "svelte/store";
import {get as getCookie} from './cookies';

export class Bridge {
  baseUrl: string
  cookieName: string

  constructor(baseUrl, cookieName = 'token') {
    this.baseUrl = baseUrl;
    this.cookieName = cookieName;
  }

  get token() {
    return getCookie(this.cookieName);
  }

  createStore() {
    return writable(initValues())
  }

  get(params: FetchParams) {
    const {path} = params;
    return storeFetch({url: new URL(path, this.baseUrl), method: Methods.get, ...params, token: this.token})
  }

  post(params: FetchParams) {
    const {path} = params;
    return storeFetch({url: new URL(path, this.baseUrl), method: Methods.post, ...params, token: this.token})
  }

  put(params: FetchParams) {
    const {path} = params;
    return storeFetch({url: new URL(path, this.baseUrl), method: Methods.put, ...params, token: this.token})
  }

  delete(params: FetchParams) {
    const {path} = params;
    return storeFetch({url: new URL(path, this.baseUrl), method: Methods.delete, ...params, token: this.token})
  }
}