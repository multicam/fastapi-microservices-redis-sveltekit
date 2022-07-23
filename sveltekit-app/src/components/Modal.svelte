<script>
  import { isModalOpen } from '$lib/stores.js'
  import { fade } from 'svelte/transition'

  export let title
</script>

{#if $isModalOpen}
  <div transition:fade class="fixed inset-0 z-40 overflow-y-auto p-4 pt-[10vh]">
    <div
      on:click={() => ($isModalOpen = false)}
      class="fixed inset-0 bg-black/70 backdrop-blur-sm"
    />

    <div class="relative mx-auto max-w-4xl rounded-lg bg-white px-6 py-10 shadow">
      <h2 class="mb-10 font-mono text-3xl tracking-tight text-gray-700">
        {title}
      </h2>

      <button
        on:click={() => ($isModalOpen = false)}
        class="absolute top-5 right-6 grid place-items-center rounded-full p-2 hover:bg-gray-100"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6 text-gray-400"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="2"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <slot />
    </div>
  </div>
{/if}
