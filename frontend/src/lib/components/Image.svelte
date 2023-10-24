<script>
  import {onMount} from 'svelte'

  export let src, alt;

  let loaded = false;
  let thisImage;

  onMount(() => {
    thisImage.onload = () => {
      loaded = true;
    };
  });

</script>

<style>
  img {
    max-width: 100%;
    max-height: 100%;
    opacity: 0;
    transition: opacity 1200ms ease-out;
    border-radius: 10px;
  }

  img.loaded {
    opacity: 1;
  }
</style>

<img {src} {alt} class:loaded bind:this={thisImage}/>