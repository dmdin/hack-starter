<script context='module'>
  export function load({session}) {
    // if (session.token) {
    //   return {redirect: '/users/self', status: 302}
    // }
    return {}
  }
</script>

<script>
  import {goto} from '$app/navigation';
  import {bridge} from "$lib/shared";
  import {slide} from 'svelte/transition';
  import {session} from '$app/stores';
  import * as cookie from '$lib/cookies'

  let username = '';
  let password = '';

  let errorMessage = null;
  let errors = {username: false, password: false}
  let rsp = bridge.createStore();

  function validate() {
    if (username === '') {
      errorMessage = 'Введите E-mail';
      errors.username = true;
      return false;
    }
    // if (!/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(username)){
    //   errorMessage = 'Введите валидный E-mail'
    //   errors.username = true;
    //   return false;
    // }
    if (password === '') {
      errorMessage = 'Введите пароль';
      errors.password = true;
      return false;
    }

    return true;
  }

  async function submit() {
    if (!validate()) return;
    bridge.post({path: 'users/login', json: {username, password}, store: rsp});
    // eslint-disable-next-line @typescript-eslint/no-empty-function
    const data = await $rsp.promise;
    if (data.detail === 'Incorrect username or password') {
      errorMessage = 'Указана неверная почта или пароль'
      errors.username = true;
      errors.password = true;
    } else if (!data.access_token) {
      errorMessage = 'Произошла непредвиденная ошибка'
    } else {
      $session.token = data.access_token;
      cookie.set('token', data.access_token);
      goto('/users/self');
    }
  }

</script>

<svelte:head>
  <title>Вход</title>
  <link rel="icon" href="data:image/svg+xml,
    <svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22>
    <text y=%22.9em%22 font-size=%2290%22>🔐</text>
    </svg>"
  >
</svelte:head>

<div class='main-block'>

  <!-- svelte-ignore a11y-missing-attribute -->
  <img src="https://static.tildacdn.com/tild3232-6435-4164-b565-313266623131/space.svg" alt="auth"/>
  <div class='wrapper'>
    <h1>Зайти в <span class="green">пространство</span></h1>
    <div class='form'>

      <input on:focus={() => errors.username = false} class:error={errors.username} bind:value={username}
             placeholder='E-mail' type='email'>
      <input on:focus={() => errors.password = false} class:error={errors.password} bind:value={password}
             placeholder='Пароль' type='password'>
      {#if (errorMessage != null)}
        <h3 transition:slide|local>{errorMessage}</h3>
      {/if}
      <div class="buttons">
        <button on:click={submit}>Войти</button>
        <a href="/users/signup">Зарегистрироваться</a>
      </div>
    </div>
  </div>
</div>

<style>

  .main-block {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    height: 90vh;
  }

  img {
    max-width: 90%;
  }

  h1 {
    font-weight: 700;
  }

  h3 {
    color: #E84855;
    font-weight: 500;
    text-align: center;
  }

  .green {
    color: #43DFA8;
  }

  .wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 90%;
    max-width: 360px;
  }

  .form {
    display: flex;
    flex-direction: column;
    max-width: 360px;
    width: 100%;
  }

  input {
    width: 90%;
    height: 48px;
    margin-bottom: 0.5em;
    border-radius: 8px;
    padding: 0 5%;
    border: 1px solid #E1E3E6;
    transition: all 0.6s ease;
  }

  input:focus {
    outline: none;
    border: 1px solid #43DFA8;
    box-shadow: 0 0 10px rgba(67, 223, 168, 0.5);
  }

  .error {
    border-color: #ff2121;
    box-shadow: 0 0 10px rgb(253, 47, 47);
  }

  a {
    padding: 0.75em 2em;
    background: transparent;
    border: 1px solid #131313;
    border-radius: 5px;
    color: #131313;
    transition: all 0.6s ease;
  }

  a:hover {
    outline: none;
    text-decoration: none;
    background-color: #43DFA8;
    border-color: transparent;
  }

  .buttons {
    display: flex;
    width: 100%;
    justify-content: space-between;
  }

  @media (max-width: 1000px) {

    .main-block {
      flex-direction: column;
      height: 100%;
    }

    h1 {
      text-align: center;
    }
  }

  @media (max-width: 360px) {
    button, a {
      padding: 10px;
      font-size: 15px;
    }
  }

</style>