<script context='module'>
  export function load({session}) {
    if (session.token && session.role) {
      return {redirect: '/users/self', status: 301}
    }
    return {}
  }
</script>

<script>
  import {fetches, storeInitValues} from '$lib/api';
  import {writable} from 'svelte/store';
  import {get} from 'svelte/store';
  import {goto} from '$app/navigation';

  let username = '';
  let password = '';
  let confirm = '';
  let errorMessage = null;
  let errors = {username: false, password: false, confirm: false}
  let rsp = writable(storeInitValues);

  // rsp.subscribe(v => console.log(v.loading))

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
    if (confirm === '') {
      errorMessage = 'Введите пароль для подтверждения';
      errors.confirm = true;
      return false;
    }
    if (password !== confirm) {
      errorMessage = 'Пароли не совпадают';
      errors.password = true;
      errors.confirm = true;
      return false;
    }
    return true;
  }

  async function submit() {
    if (!validate()) return;
    rsp = fetches.post({path: 'users/create', json: {username, password}, cache: false, store: rsp});
    console.log('lala', await $rsp.promise, $rsp.loading, $rsp.data);
    // goto('/users/self')
  }

</script>

<svelte:head>
  <title>Регистрация</title>
</svelte:head>

<div class='main-block'>

  <!-- svelte-ignore a11y-missing-attribute -->
  <img src='https://static.tildacdn.com/tild6362-3166-4430-b466-346266653936/reg.svg' alt='reg-photo'/>
  <div class='reg-wrapper'>
    <h1>Регистрация в наш <span class='green'>сервис</span></h1>
    <div class='inputs'>

      <input on:focus={() => errors.username = false} class:error={errors.username} bind:value={username}
             placeholder='E-mail' type='email'>
      <input on:focus={() => errors.password = false} class:error={errors.password} bind:value={password}
             placeholder='Пароль' type='password'>
      <input on:focus={() => errors.confirm = false} class:error={errors.confirm} bind:value={confirm}
             placeholder='Подтверждение пароля' type='password'>

      {#if (errorMessage != null)}
        <h3>{errorMessage}</h3>
      {/if}
      <button on:click={submit}>Зарегистрироваться</button>
      {#await $rsp.promise}
        <h1>Loading</h1>
      {:then ready}
        <h1>{JSON.stringify(ready)}</h1>
      {/await}
    </div>
  </div>
</div>

<style>

  .main-block {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    height: 100vh;
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
  }

  .green {
    color: #43DFA8;
  }


  .inputs {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  input {
    max-width: 300px;
    width: 70%;
    height: 48px;
    margin-bottom: 0.5em;
    border-radius: 8px;
    padding: 0 2em;
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

  button {
    background-color: #131313;
    color: #fff;
    font-weight: 500;
    border: none;
    border-radius: 5px;
    padding: 0.75em 2em;
    transition: all 0.6s ease;
  }

  button:hover {
    background-color: #43DFA8;
    color: #131313;
  }

  button:focus {
    outline: none;
  }

  @media (max-width: 1000px) {

    .main-block {
      flex-direction: column;
    }

    h1 {
      text-align: center;
    }
  }

</style>