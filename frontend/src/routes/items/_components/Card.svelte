<script lang="ts">
  import {createEventDispatcher} from 'svelte';
  import {scale} from "svelte/transition";
  import LazyImage from '$lib/components/ImageLoader.svelte'

  import trash from './trash.svg';
  import edit from './edit.svg';
  import save from './save.svg';

  export let id: string, name: string, pic: string, desc: string;
  export let editMode = false;

  const dispatch = createEventDispatcher();
  let hovered = false;

</script>

<div class="component"
     on:mouseover={() => hovered = true}
     on:mouseout={() => hovered = false}
     transition:scale>
  <div class="content">
    {#if editMode}
      <div class="edit-image"
           style="background: url('{pic}') no-repeat;
                  background-size: contain;
                  background-position: center;
                  border-radius: 10px;
                  ">
        <h2>Ссылка на картинку: <input class="edit-image-input" bind:value={pic}></h2>
      </div>
      <input class="title" bind:value={name}>
      <textarea class="desc" bind:value={desc}></textarea>
    {:else}
      <div class="image-wrapper">
        <LazyImage src={pic} alt="{name}-picture"/>
      </div>
      <h1 class="title">{name}</h1>
      <p class="desc">{desc}</p>
    {/if}
  </div>
  <div class="buttons">
    <button class="button-icon" class:visible={hovered} on:click={() => dispatch('delete', id)}>
      <img class="icon delete-icon" src={trash} alt="Delete">
    </button>
    {#if editMode}
      <button class="visible button-icon" on:click={() => {editMode = false; dispatch('edit', {id, name, pic, desc})}}>
        <img class="icon save-icon" src={save} alt="Save">
      </button>
    {:else}
      <button class="button-icon" class:visible={hovered} on:click={() => editMode = true}>
        <img class="icon edit-icon" src={edit} alt="Edit">
      </button>
    {/if}
  </div>
</div>

<style>
  .component {
    width: 300px;
    height: 360px;
    border: 1px solid transparent;
    padding: 7px;
    border-radius: 20px;
    box-shadow: 0 0 10px 1px rgba(200, 200, 200, 0.3);
    background-color: #ffffff;
    /*display: flex;*/
    /*flex-direction: column;*/
    /*align-items: center;*/
  }

  .content {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .edit-image {
    border-radius: 10px;
    margin: 0 auto;
    width: 100%;
    height: 200px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
  }

  .edit-image-input {
    background: transparent;
  }

  .image-wrapper {
    margin: 0 auto;
    width: 100%;
    height: 200px;
    display: grid;
    place-items: center;
  }

  h2 {
    text-align: center;
    background: rgba(255, 255, 255, 0.6);
    width: 100%;
    padding: 5px 0;
  }


  button {
    transition: opacity 0.7s ease;
  }

  .buttons {
    width: 100%;
    display: flex;
    justify-content: space-between;
  }

  .button-icon {
    opacity: 1;
    padding: 3px 3px 0;
    background-color: transparent;
    box-shadow: none;
    border-color: transparent;
    border-radius: 5px;
    transition: background-color 0.7s ease;
  }

  .button-icon:hover {
    background: #e0e0e0;
  }

  .icon {
    width: 20px;
  }

  /*textarea {*/
  /*}*/
  textarea, input, h1, p {
    padding: 0;
    border: none;
    width: 100%;
    margin: 5px;
    color: #444444;
    text-align: center;
    overflow: hidden;
  }

  textarea {
    resize: none;
  }

  textarea, p {
    height: 70px;
    hyphens: auto;
    font-family: Arial sans-serif;
    line-height: 1.3;
  }

  .title {
    font-size: 30px;
  }

  .visible {
    opacity: 1;
  }

  img {
    width: 200px;
  }

  .desc {
    margin: 5px;
  }

</style>