<script context='module'>
  export function load({session}) {
    // console.log('Used load:', session.token)
    // return {props: {token: session.token}};
    return {redirect: '/items/list', status: 302};
  }
</script>

<script>
  import {goto} from '$app/navigation';
  import {token as tokenStore} from '$lib/shared';

  export let token;

  async function logout() {
    $tokenStore = undefined;
    goto('/users/signin');
  }
</script>

<svelte:head>
  <title>Профиль</title>
</svelte:head>

<p>My token: {token}</p>
<p>My token: {$tokenStore}</p>

<button on:click={logout}>Logout</button>