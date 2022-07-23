<script>
  import clsx from 'clsx'
  import { isModalOpen, mutated } from '$lib/stores.js'

  let name
  let price
  let quantity

  const handleSubmit = async e => {
    try {
      await fetch(`${import.meta.env.VITE_INVENTORY_SERVER}/products`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name,
          price,
          quantity
        })
      })
      e.target.reset()
      $isModalOpen = false
      $mutated = true
    } catch (error) {
      console.error(error)
    }
  }
</script>

<form on:submit|preventDefault={handleSubmit} class="flex flex-col justify-between">
  <div class="flex flex-col space-y-6">
    <div class="">
      <label for="name" class="sr-only">Name</label>
      <input
        bind:value={name}
        type="text"
        placeholder="Name"
        class={clsx(
          'w-full rounded-md border-gray-400 px-4 placeholder-gray-400 focus:shadow-md focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2',
          false && 'border-2 border-red-500'
        )}
      />
    </div>
    <div class="">
      <label for="price" class="sr-only">Price</label>
      <input
        bind:value={price}
        type="number"
        placeholder="Price"
        class={clsx(
          'w-full rounded-md border-gray-400 px-4 placeholder-gray-400 focus:shadow-md focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2',
          false && 'border-2 border-red-500'
        )}
      />
    </div>
    <div class="">
      <label for="quantity" class="sr-only">Quantity</label>
      <input
        bind:value={quantity}
        type="number"
        placeholder="Quantity"
        class={clsx(
          'w-full rounded-md border-gray-400 px-4 placeholder-gray-400 focus:shadow-md focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2',
          false && 'border-2 border-red-500'
        )}
      />
    </div>
  </div>

  <div class="pt-10">
    <button
      type="submit"
      class="w-full rounded-lg bg-gradient-to-r from-blue-500 to-pink-400 py-2 px-4 font-mono text-xl font-medium text-white hover:opacity-90"
    >
      Create
    </button>
  </div>
</form>
