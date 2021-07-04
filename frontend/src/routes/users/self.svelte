<script context='module'>
  import {token} from '$lib/shared';

  export function load({session}) {
    return {props: session};
  }
</script>

<script>
  import {goto} from '$app/navigation';

  async function logout() {
    $token = undefined;
    goto('/users/signin');
  }
</script>
<p>My token: {$token}</p>
<button on:click={logout}>Logout</button>