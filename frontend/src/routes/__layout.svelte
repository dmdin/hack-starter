<script lang="ts">
	import '../app.css';
</script>

<!--<Header/>-->

<main>
	<slot/>
</main>

<!--<footer>-->
<!--	<p>visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to learn SvelteKit</p>-->
<!--</footer>-->

<style>
	main {
		width: 100%;
		max-width: 1440px;
		margin: 0 auto;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 40px;
	}

	footer a {
		font-weight: bold;
	}

	@media (min-width: 480px) {
		footer {
			padding: 40px 0;
		}
	}
</style>
