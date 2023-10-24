<script context="module">
  export const load = async ({page, session}) => ({
    props: {
      key: page.path,
      token: session.token
    },
  })
</script>

<script lang="ts">
  import '../app.css';
  import PageTransition from '$lib/components/PageTransition.svelte';
  // import ErrorLabel from '$lib/components/ErrorLabel.svelte';
  import {session} from '$app/stores';
  import * as cookie from '$lib/cookies';
  import {goto} from '$app/navigation';

  export let token;
  export let key;

  async function logout() {
    $session.token = null;
    cookie.del('token');
    goto('/users/signin');
  }
</script>

<header>
  <a href="/"><h1 class="header-logo">Hack<span class="green">Masters</span></h1></a>
  <a href="/users/signin">Вход</a>
  <a href="/users/signup">Регистрация</a>
  <a class:disabled={!token} href={token ? "/items/list" : "#"}>Каталог</a>
  <button on:click={logout}>Выход</button>
</header>

<main>
  <PageTransition refresh={key}>
    <slot/>
    <!--    <ErrorLabel/>-->
  </PageTransition>
</main>


<style>
  main {
    width: 100%;
    max-width: 1440px;
    margin: 0 auto;
  }

  header {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
  }

  a {
    margin: 0 10px;
    color: #5b5b5b;
    transition: color 0.4s ease;
  }

  a:hover {
    color: black;
    text-decoration: none;
  }

  .disabled {
    color: #b1b1b1;
    cursor: default;
  }

  .disabled:hover {
    color: #b1b1b1;
  }

  button {
    margin-left: 10px;
    padding: 7px;
    background-color: transparent;
    color: black;
    border-color: black;
  }

  button:hover {
    background-color: black;
    color: white;
  }

  .header-logo {
    font-size: 20px;
    width: 150px;
  }

  h1 {
    font-weight: 700;
  }

  .green {
    color: #43DFA8;
  }
</style>
