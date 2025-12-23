<template>
  <div class="flex h-screen bg-gray-100">
    <Sidebar />

    <main class="flex-1 overflow-auto">
      <header class="bg-gray-100 p-6">
        <div class="flex items-center justify-between mb-6">
          <h1 class="text-3xl font-bold">Filtri</h1>
          
          <div class="flex items-center gap-3">
            <img :src="profilo" 
                 alt="Profile" 
                 class="w-16 h-16 rounded-full object-cover" />
            <span class="font-medium">Alex Testa</span>
          </div>
        </div>

        <div class="flex gap-3 mb-6">
          <button 
            v-for="filter in filters" 
            :key="filter"
            @click="activeFilter = filter"
            :class="[
              'px-6 py-2 rounded-full font-medium transition',
              activeFilter === filter 
                ? 'bg-purple-600 text-white' 
                : 'bg-white text-gray-700 hover:bg-gray-50'
            ]"
          >
            {{ filter }}
          </button>
        </div>

        <div class="pr-12">
        <div class="relative max-w-5xl">
            <svg class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
            <input
            type="text"
            placeholder="Cerca Farmaco...."
            v-model="searchQuery"
            class="w-full pl-12 pr-4 py-3 bg-white border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
            />
        </div>
        </div>
      </header>

      <div class="p-6 pr-12">
        <h2 class="text-2xl font-bold mb-6">In Magazzino</h2>
        
        <div class="max-w-5xl space-y-4">
          <div 
            v-for="product in products" 
            :key="product.id"
            @click="router.push(`/remove-item/${product.id}/${product.expiryDate}`)"
            class="bg-white rounded-2xl p-6 shadow-sm hover:shadow-md transition flex items-center justify-between cursor-pointer"
          >
            <div class="flex items-center gap-6">
              <div class="w-16 h-16 bg-gray-100 rounded-lg flex items-center justify-center">
                <img :src="product.image" alt="FarmaLab" class="max-w-full max-h-full object-cover" />
              </div>

              <div>
                <p class="text-sm text-gray-500 mb-1">Nome</p>
                <p class="font-semibold">{{ product.name }}</p>
              </div>
            </div>

            <div class="flex items-center gap-12">
              <div class="text-center">
                <p class="text-sm text-gray-500 mb-1">Quantità</p>
                <p class="font-semibold">{{ product.quantity }}</p>
              </div>

              <div class="text-center">
                <p class="text-sm text-gray-500 mb-1">Data di scadenza</p>
                <p class="font-semibold">{{ product.expiryDate }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import profilo from '@/assets/images/profilo.jpg'
import farmacoImg from '@/assets/images/foto-farmaco-esempio.jpg'
import Sidebar from '@/components/Sidebar.vue'

const router = useRouter()

const filters = ['Entro 1 mese', 'Entro 3 mesi', 'Entro 6 mesi', 'Entro 1 anno']
const activeFilter = ref('Entro 1 mese')
const searchQuery = ref('')

const products = ref<any[]>([])

const formatDateIT = (iso: string) => {
  try {
    const d = new Date(iso)
    return d.toLocaleDateString('it-IT', { year: 'numeric', month: 'long', day: 'numeric' })
  } catch (e) {
    return iso
  }
}

const loadInventary = async () => {
  try {
    const res = await fetch('http://localhost:8000/inventary')
    if (!res.ok) throw new Error(res.statusText)
    const data = await res.json()
    console.log('Inventary data:', data.map((r: any) => r.image))
    products.value = data.map((r: any) => ({
      id: r[0] ?? r.id_medicine,
      name: r[1] ?? r.medicine_name,
      quantity: `${r[5] ?? r.quantity} pz`,
      expiryDate: formatDateIT(r[4] ?? r.expire_date),
      image: r[3] ?? r.image
    }))
  } catch (err) {
    console.error('Errore caricamento inventario:', err)
  }
}

onMounted(loadInventary)

</script>