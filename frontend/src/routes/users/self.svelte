<script context='module'>
  export function load({session}) {
    return {
      props: session
    }
  }
</script>

<script>
  export let token;
</script>
<p>My token: {token}</p>
