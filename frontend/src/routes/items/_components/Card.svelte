<script lang="ts">
  import {createEventDispatcher} from 'svelte';
  import LazyImage from '$lib/components/ImageLoader.svelte'

  export let id: string, name: string, pic: string, desc: string;
  export let editMode = false;
  const dispatch = createEventDispatcher();

</script>

<div class="component">
  <button on:click={() => dispatch('delete', id)}>x</button>
  <LazyImage src="https://via.placeholder.com/200" alt="{name}-picture"/>
  {#if editMode}
    <input class="title" bind:value={name}>
    <input class="desc" bind:value={desc}>
    <button on:click={() => {editMode = false; dispatch('edit', {id, name, pic, desc})}}>Save</button>
  {:else}
    <h1 class="title">{name}</h1>
    <p class="desc">{desc}</p>
    <button on:click={() => editMode = true}>Edit</button>
  {/if}
</div>

<style>
  .component {
    width: 300px;
    height: 350px;
    border: 1px solid transparent;
    border-radius: 20px;
    box-shadow: 0 0 10px 1px rgba(200, 200, 200, 0.3);
    background-color: #ffffff;
    display: flex;
    flex-direction: column;
    align-items: center;

  }

  input, h1, p {
    border: none;
    max-width: 280px;
    margin: 5px;
    color: #444444;
    text-align: center;
  }

  .title {
    font-size: 30px;
  }

  img {
    width: 200px;
  }

  .desc {
    margin: 5px;
  }

</style>