<script context="module" lang="ts">
  import {bridge} from "$lib/shared";
  import {get} from 'svelte/store';

  export async function load({session}) {
    const {token} = session;
    const resp = get(bridge.get({path: '/items/read', token: token}));
    const data = await resp.promise;
    return {props: {data, token}};
  }
</script>

<script>
  import Card from "./_components/Card.svelte";
  import Create from './_components/Create.svelte';
  import plus from './_assets/plus.svg';

  export let data;
  export let token;

  let showModal = false;

  function deleteItem(i) {
    let item = data[i];
    data = data.filter(i => i !== item);
    bridge.delete({path: '/items/delete', json: item, token: token, query: {id: item.id}});
  }

  async function editItem(i, item) {
    console.log(item);
    bridge.put({path: '/items/update', json: item, token: token, query: {id: item.id}});
    data[i] = item;
  }

  async function createItem(item) {
    let newItem = await get(bridge.post({path: '/items/create', json: item, token: token})).promise;
    data = data.concat(newItem);
  }

  let windowWidth;

</script>

<svelte:head>
  <title>Каталог</title>
  <link rel="icon" href="data:image/svg+xml,
    <svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22>
    <text y=%22.9em%22 font-size=%2290%22>📃</text>
    </svg>"
  >
</svelte:head>
<svelte:window bind:innerWidth={windowWidth}/>

<Create bind:showModal on:create={(event) => createItem(event.detail)}/>

<div class="page" style="--columns: repeat(min(4, {Math.round(windowWidth / (300 + 120))}), auto)">
  {#each data as card, i (card.id)}
    <Card {...card} on:delete={() => deleteItem(i)} on:edit={(event) => editItem(i, event.detail)}/>
  {/each}
  <button class="create-button" on:click={() => {showModal = true}}>
    <img class="create-icon" src={plus} alt="Создать">
  </button>
</div>

<style>
  :root {
    background-color: #fdfdfd;
  }

  .page {
    display: grid;
    place-items: center;
    grid-template-columns: var(--columns);
    grid-row-gap: 20px;
    width: 100%;
    margin: 60px 0;
  }

  .create-button {
    width: 300px;
    height: 360px;
    padding: 7px;
    border-radius: 20px;
    box-shadow: 0 0 10px 1px rgba(200, 200, 200, 0.3);
    background: white;
    border: none;
    transition: box-shadow 0.7s ease;
    cursor: pointer;
  }

  .create-button:hover {
    box-shadow: 0 0 20px 1px rgba(200, 200, 200, 0.5);
  }

  .create-icon {
    width: 30%;
  }

</style>