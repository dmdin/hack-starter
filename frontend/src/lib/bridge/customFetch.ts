import {Writable, writable} from 'svelte/store';


export const apiUrl = 'http://localhost:8000/';

export interface FetchParams {
  path?: string
  query?: any
  json?: any
  token?: string
  cache?: boolean
  store?: Writable<any>
}

export enum Methods {
  get = 'get', post = 'post', put = 'put', delete = 'delete'
}

export const fetches = {
  get: (params: FetchParams): Writable<any> => {
    const {path} = params;
    return storeFetch({url: new URL(path, apiUrl), method: Methods.get, ...params})
  },
  post: (params: FetchParams): Writable<any> => {
    const {path} = params;
    return storeFetch({url: new URL(path, apiUrl), method: Methods.post, ...params})
  },
  put: (params: FetchParams): Writable<any> => {
    const {path} = params;
    return storeFetch({url: new URL(path, apiUrl), method: Methods.put, ...params})
  },
  delete: (params: FetchParams): Writable<any> => {
    const {path} = params;
    return storeFetch({url: new URL(path, apiUrl), method: Methods.delete, ...params})
  },
}

export interface StoreFetchParams extends FetchParams {
  url: URL
  method: Methods
}

export interface StoreFetchResult {
  savedResolve: undefined
  promise: Promise<any>
  data: any
  loading: boolean
  ready: boolean
}

export function initValues(): StoreFetchResult {
  // Save Resolve, because Promise.resolve creates new Promise, that lags with js await
  let savedResolve;
  const promise = new Promise((resolve) => savedResolve = resolve);
  return {savedResolve, promise, data: undefined, loading: true, ready: false}
}

interface Request {
  method: Methods,
  headers: { Accept, Authorization?: string | undefined, 'Content-Type' },
  body?: string
}

export function storeFetch(params: StoreFetchParams): Writable<StoreFetchResult> {
  const {url, token, method, path, json = {}, store = writable(), cache = true} = params;
  // TODO add query params
  store.set(initValues());
  const saved = localStorage.getItem(url.href);
  const cached = saved && JSON.parse(saved);
  if (cache && cached) {
    // @ts-ignore
    store.update(obj => {
      obj.data = cached;
      obj.ready = true;
      obj.promise = obj.savedResolve(cached);
      return obj;
    });
  }

  async function load() {
    const headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    }
    if (token) {
      headers['Authorization'] = 'Bearer ' + token;
    }
    const request: Request = {
      method,
      headers
    };

    if (method !== Methods.get) {
      request.body = JSON.stringify(json);
    }
    const response = await fetch(url.href, request);
    const data = await response.json().catch(e => console.warn(`Exception during fetch ${path}: ${e}`));
    if (cache) {
      localStorage.setItem(url.href, JSON.stringify(data));
    }
    return data;
  }

  load().then(data => {
    // @ts-ignore
    store.update(obj => {
      obj.data = data;
      obj.ready = true;
      obj.promise = obj.savedResolve(data);
      obj.loading = false;
      return obj;
    });
  });
  return store;
}

