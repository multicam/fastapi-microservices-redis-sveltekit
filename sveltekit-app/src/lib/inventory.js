const {log} = console

export async function fetchProducts() {
  const res = await fetch(`${import.meta.env.VITE_INVENTORY_SERVER}/products`)
  return res.json()
}

export async function deleteProduct(id) {
  await fetch(`${import.meta.env.VITE_INVENTORY_SERVER}/products/${id}`, {
    method: 'DELETE'
  })
}
