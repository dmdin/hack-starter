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
  import PageTransition from '$lib/PageTransition.svelte'

  export let token;
  export let key;
</script>

<header>
  <a href="/"><h1 class="header-logo">Hack<span class="green">Masters</span></h1></a>
  <a href="/users/signin">Вход</a>
  <a href="/users/signup">Регистрация</a>
  <a class:disabled={!token} href={token ? "/items/list" : ""}>Каталог</a>
</header>

<main>
  <PageTransition refresh={key}>
    <slot/>
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
