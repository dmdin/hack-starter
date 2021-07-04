<script>
  import {fly} from "svelte/transition"

  export let refresh = "";
  const timing = 400;
</script>

{#key refresh}
  <div in:fly={{  y:-5, duration: timing, delay: timing }}
       out:fly={{ y: 5, duration: timing             }}>
    <slot/>
  </div>
{/key}