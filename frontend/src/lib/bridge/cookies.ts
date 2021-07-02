export function del(name: string): void {
  set(name, '', {
    'max-age': -1
  })
}

export function get(name: string): string | undefined {
  const matches = document.cookie.match(new RegExp(
    '(?:^|; )' + name.replace(/([.$?*|{}()[\]\\/+^])/g, '\\$1') + '=([^;]*)'
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

export function set(name: string, value: string, options: any = {}): void {
  options = {
    path: '/',
    ...options
  };
  if (options.expires instanceof Date) {
    options.expires = options.expires.toUTCString();
  }
  let updatedCookie = encodeURIComponent(name) + '=' + encodeURIComponent(value);
  for (const optionKey in options) {
    updatedCookie += '; ' + optionKey;
    // noinspection JSUnfilteredForInLoop
    const optionValue = options[optionKey];
    if (optionValue !== true) {
      updatedCookie += '=' + optionValue;
    }
  }
  document.cookie = updatedCookie;
}
