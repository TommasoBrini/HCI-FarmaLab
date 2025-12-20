<template>
  <div class="flex h-screen bg-gray-100">
    <aside class="w-48 bg-white shadow-lg flex flex-col">
      <div class="p-6">
        <div class="flex items-center justify-center gap-2">
          <img :src="logo" alt="FarmaLab" class="w-20 h-20 rounded-lg object-cover" />
        </div>
      </div>

      <nav class="flex-1 p-4">
        <ul class="space-y-2">
          <li>
            <button class="w-full flex items-center gap-3 px-4 py-3 rounded-lg bg-purple-100 text-purple-600 font-medium">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
              </svg>
              Home
            </button>
          </li>
          <li>
            <button class="w-full flex items-center gap-3 px-4 py-3 rounded-lg text-gray-600 hover:bg-gray-100">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
              </svg>
              Aggiungi
            </button>
          </li>
          <li>
            <button class="w-full flex items-center gap-3 px-4 py-3 rounded-lg text-gray-600 hover:bg-gray-100">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              Info
            </button>
          </li>
          <li>
            <button class="w-full flex items-center gap-3 px-4 py-3 rounded-lg text-gray-600 hover:bg-gray-100">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
              </svg>
              Log
            </button>
          </li>
        </ul>
      </nav>

      <div class="p-4">
        <button @click="logout" class="w-full flex items-center gap-3 px-4 py-3 rounded-lg text-gray-600 hover:bg-gray-100">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
          </svg>
          Esci
        </button>
      </div>
    </aside>

    <main class="flex-1 overflow-auto">
      <header class="bg-gray-100 p-6">
        <div class="flex items-center justify-between mb-6">
          <h1 class="text-3xl font-bold">Filtri</h1>
          
          <div class="flex items-center gap-3">
            <img :src="profilo" 
                 alt="Profile" 
                 class="w-16 h-16 rounded-full" />
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
            class="bg-white rounded-2xl p-6 shadow-sm hover:shadow-md transition flex items-center justify-between"
          >
            <div class="flex items-center gap-6">
              <div class="w-16 h-16 bg-gray-100 rounded-lg flex items-center justify-center">
                <img :src="farmacoImg" alt="FarmaLab" class="max-w-full max-h-full object-cover" />
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import logo from '@/assets/images/logo.png'
import profilo from '@/assets/images/profilo.jpg'
import farmacoImg from '@/assets/images/foto-farmaco-esempio.jpg'

const router = useRouter()

const filters = ['Entro 1 mese', 'Entro 3 mesi', 'Entro 6 mesi', 'Entro 1 anno']
const activeFilter = ref('Entro 1 mese')
const searchQuery = ref('')

const products = ref([
  { id: 1, name: 'Lexil 20cp 10g', quantity: '30 pz', expiryDate: '1 gennaio 2025' },
  { id: 2, name: 'Lexil 20cp 10g', quantity: '30 pz', expiryDate: '1 gennaio 2025' },
  { id: 3, name: 'Lexil 20cp 10g', quantity: '30 pz', expiryDate: '1 gennaio 2025' },
  { id: 4, name: 'Lexil 20cp 10g', quantity: '30 pz', expiryDate: '1 gennaio 2025' },
  { id: 5, name: 'Lexil 20cp 10g', quantity: '30 pz', expiryDate: '1 gennaio 2025' },
  { id: 6, name: 'Lexil 20cp 10g', quantity: '30 pz', expiryDate: '1 gennaio 2025' },
])

const logout = () => {
  router.push('/login')
}
</script>