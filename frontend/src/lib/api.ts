import {Writable, writable} from 'svelte/store';
import {get as getCookie} from './cookies';

export const apiUrl = 'http://localhost:8000/';
const cookieTokenName = 'token';

interface FetchParams {
  path?: string
  query?: any
  json?: any
  token?: string
  cache?: boolean
  store?: Writable<any>
}

enum Methods {
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

interface Request {
  method: Methods,
  headers: { Accept, Authorization?: string | undefined, 'Content-Type' },
  body?: string
}

interface StoreFetchParams extends FetchParams {
  url: URL
  method: Methods
}

interface StoreFetchResult {
  promise: Promise<any>
  data: any
  loading: boolean
  ready: boolean
}

export const storeInitValues: StoreFetchResult = {
  // eslint-disable-next-line @typescript-eslint/no-empty-function
  promise: new Promise(() => {
  }),
  data: undefined,
  loading: true,
  ready: false
}

export function storeFetch(params: StoreFetchParams): Writable<StoreFetchResult> {
  const {url, method, path, json = {}, store = writable(), cache = true} = params;
  let {token = undefined} = params;
  // TODO add query params
  store.set(storeInitValues);
  const saved = localStorage.getItem(url.href);
  const cached = saved && JSON.parse(saved);
  if (cache && cached) {
    // @ts-ignore
    store.update(obj => {
      obj.data = cached;
      obj.ready = true;
      obj.promise = Promise.resolve(cached);
      return obj;
    });
  }

  async function load() {
    const headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    }
    if (!token) {
      token = getCookie(cookieTokenName);
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
      obj.promise = Promise.resolve(data);
      obj.loading = false;
      return obj;
    });
  });
  return store;
}

