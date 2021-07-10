<script context='module'>
  export function load({session}) {
    // console.log('Used load:', session.token)
    // return {props: {token: session.token}};
    return {redirect: '/items/list', status: 302};
  }
</script>

<script>
  import {goto} from '$app/navigation';
  import * as cookie from "$lib/cookies";
  import {session} from '$app/stores';

  export let token;

  async function logout() {
    $session.token = null;
    cookie.del('token');
    goto('/users/signin');
  }
</script>

<svelte:head>
  <title>Профиль</title>
  <link rel="icon" href="data:image/svg+xml,
    <svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22>
    <text y=%22.9em%22 font-size=%2290%22>🧿</text>
    </svg>"
  >
</svelte:head>

<p>My token: {token}</p>


<button on:click={logout}>Выйти</button>