import {FetchParams, initValues, Methods, storeFetch} from './customFetch';
import {writable} from "svelte/store";

export class Bridge {
  baseUrl: string
  cookieName: string

  constructor(baseUrl) {
    this.baseUrl = baseUrl;
  }

  createStore() {
    return writable(initValues())
  }

  get(params: FetchParams) {
    const {path} = params;
    return storeFetch({url: new URL(path, this.baseUrl), method: Methods.get, ...params})
  }

  post(params: FetchParams) {
    const {path} = params;
    return storeFetch({url: new URL(path, this.baseUrl), method: Methods.post, ...params})
  }

  put(params: FetchParams) {
    const {path} = params;
    return storeFetch({url: new URL(path, this.baseUrl), method: Methods.put, ...params})
  }

  delete(params: FetchParams) {
    const {path} = params;
    return storeFetch({url: new URL(path, this.baseUrl), method: Methods.delete, ...params})
  }
}