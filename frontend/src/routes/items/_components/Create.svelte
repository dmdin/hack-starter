<script>
  import Modal from '$lib/components/Modal.svelte'
  import {createEventDispatcher} from 'svelte';

  export let showModal = false;
  const dispatcher = createEventDispatcher();
  let name, pic = 'https://source.unsplash.com/random', desc = '';

</script>
<Modal bind:open={showModal}>
  <div class="card">
    <div class="edit-image"
         style="background: url('{pic}') no-repeat;
                  background-size: contain;
                  background-position: center;
                  border-radius: 10px;
                  ">
      <h2>Ссылка на картинку: <input placeholder="ссылка" class="edit-image-input" bind:value={pic}></h2>
    </div>
    <input class="title" placeholder="Название" bind:value={name}>
    <textarea placeholder="Описание..." bind:value={desc}></textarea>
    <button disabled={!name} on:click={() => {dispatcher('create', {name, pic, desc}); showModal=false}}>Создать
    </button>
  </div>
</Modal>

<style>
  .card {
    padding: 0 100px;
    max-width: 300px;
    height: 380px;
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

  h2 {
    text-align: center;
    background: rgba(255, 255, 255, 0.6);
    width: 100%;
    padding: 5px 0;
  }

  textarea {
    resize: none;
  }

  textarea {
    height: 70px;
    hyphens: auto;
    font-family: Arial sans-serif;
    line-height: 1.3;
  }

  textarea, input {
    padding: 0;
    border: none;
    width: 100%;
    margin: 7px 0;
    color: #444444;
    text-align: center;
    overflow: hidden;
  }

  .title {
    font-size: 30px;
  }

  button {
    margin: 10px 0;
  }

  /*img {*/
  /*  width: 200px;*/
  /*}*/


</style>