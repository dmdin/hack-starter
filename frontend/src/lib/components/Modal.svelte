<script>
  import {fade, fly} from 'svelte/transition'

  export let open;
  let component;
</script>

{#if open}
  <div bind:this={component}
       on:click={event => event.target === component ? open = false : undefined}
       transition:fade={{duration: 400}}
       class="background">
    <div class="window" transition:fly={{y: -20, duration: 700}}>
      <button class="cancel-button" on:click={() => open = false}>
        <svg width=16 height=16>
          <line x1=2 y1=2 x2=14 y2=14></line>
          <line x1=2 y1=14 x2=14 y2=2></line>
        </svg>
      </button>
      <div class="content">
        <slot/>
      </div>
    </div>
  </div>
{/if}

<style>
  .background {
    z-index: 1;
    top: 0;
    right: 0;
    position: fixed;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    filter: none;
  }

  .window {
    padding: 0 5px 20px 5px;
    background: white;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    margin-bottom: 300px;
    border-radius: 10px;
  }

  .cancel-button {
    width: 32px;
    height: 32px;
    margin-top: 5px;
    margin-right: 5px;
    background: transparent;
    border-color: transparent;
    cursor: pointer;
  }

  .content {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  line {
    stroke: #333333;
  }

</style>