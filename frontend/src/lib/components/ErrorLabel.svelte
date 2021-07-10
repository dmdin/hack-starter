<script>
  import {errorLabel} from "$lib/shared";
  import {fade} from 'svelte/transition';
</script>

{#if $errorLabel}
  <div transition:fade>
    <p>{$errorLabel}</p>
  </div>
{/if}
<style>
  div {
    position: absolute;
    bottom: 100px;
    left: 0;
    right: 0;
    margin-left: auto;
    margin-right: auto;
    max-width: 400px;
    border-radius: 10px;
    background-color: #f8858b;
    box-shadow: 0 0 20px 1px #f57e7f;
    display: grid;
    place-items: center;
  }

  p {
    color: white;
    width: 90%;
    text-align: center;
    text-shadow: 0 0 7px rgba(255, 255, 255, 0.7);
  }
</style>