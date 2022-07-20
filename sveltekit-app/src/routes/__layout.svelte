<script>
  import '$styles/app.css'
  import Header from '$components/Header.svelte'
  import Sidebar from '$components/Sidebar.svelte'
</script>

<svelte:head>
  <title>-- powered by microbot --</title>
</svelte:head>

<Header />
<Sidebar />

<div class="pl-52">
  <main class="px-6">
    <slot />
  </main>
</div>
