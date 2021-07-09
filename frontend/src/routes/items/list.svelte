<script context="module" lang="ts">
  import {bridge} from "$lib/shared";
  import {get} from 'svelte/store'

  export async function load({session}) {
    const {token} = session
    const resp = get(bridge.get({path: '/items/read', token: token}));
    const data = await resp.promise;
    return {props: {data, token}}
  }
</script>

<script>
  import Card from "./_components/Card.svelte";

  export let data;
  export let token;

  // console.log(data);
  function deleteItem(i) {
    data = [...data.slice(0, i), ...data.slice(i + 1)];
  }

  function editItem(i, item) {
    console.log(item)
    bridge.put({path: '/items/update', json: item, token: token, query: {id: item.id}, cache: false})
    data[i] = item;
  }

  function createItem() {
    bridge.put()
  }

  let windowWidth;

</script>

<svelte:window bind:innerWidth={windowWidth}/>
<div class="page" style="--columns: repeat(min(4, {Math.round(windowWidth / (300 + 120))}), auto)">
  {#each data as card, i (card.id)}
    <Card {...card} on:delete={() => deleteItem(i)} on:edit={(event) => editItem(i, event.detail)}/>
  {/each}
  <button on:click={createItem}>Create</button>
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
    margin-top: 60px;
  }

</style>