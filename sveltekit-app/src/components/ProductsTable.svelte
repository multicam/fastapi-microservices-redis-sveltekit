<script>
  import { deleteProduct } from '$lib/inventory.js'

  export let products = []

  const onDelete = async (/** @type {string} */ id) => {
    if (window.confirm('Are you sure to delete this record?')) {
      await deleteProduct(id)
      products = products.filter(p => p.id !== id)
    }
  }
</script>

<div class="pt-10">
  <table class="w-full max-w-4xl table-auto border-collapse rounded-lg border border-slate-400">
    <thead>
      <tr class="bg-zinc-100">
        <th class="w-48 border border-slate-300 p-2 text-left text-lg font-semibold text-gray-800"
          >#</th
        >
        <th class="border border-slate-300 p-2 text-left text-lg font-semibold text-gray-800"
          >Name</th
        >
        <th class="border border-slate-300 p-2 text-left text-lg font-semibold text-gray-800"
          >Price</th
        >
        <th class="border border-slate-300 p-2 text-left text-lg font-semibold text-gray-800"
          >Quantity</th
        >
        <th class="border border-slate-300 p-2 text-left text-lg font-semibold text-gray-800"
          >Actions</th
        >
      </tr>
    </thead>

    <tbody>
      {#each products as p (p.id)}
        <tr class="hover:bg-zinc-50">
          <td class="border border-slate-300 p-2 text-gray-600">{p.id}</td>
          <td class="border border-slate-300 p-2 text-gray-600">{p.name}</td>
          <td class="border border-slate-300 p-2 text-gray-600">{p.price}</td>
          <td class="border border-slate-300 p-2 text-gray-600">{p.quantity}</td>
          <td class="border border-slate-300 p-2 text-gray-600">
            <button
              class="rounded px-2 py-1 text-red-700 hover:bg-red-200"
              on:click={() => onDelete(p.id)}
            >
              Delete
            </button>
          </td>
        </tr>
      {/each}
    </tbody>
  </table>
</div>
