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
            <router-link
              to="/home"
              class="w-full flex items-center gap-3 px-4 py-3 rounded-lg text-gray-600 hover:bg-gray-100"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
              </svg>
              Home
            </router-link>
          </li>
          <li>
            <button class="w-full flex items-center gap-3 px-4 py-3 rounded-lg bg-purple-100 text-purple-600 font-medium">
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

      <div class="p-4 border-t">
        <button @click="logout" class="w-full flex items-center gap-3 px-4 py-3 rounded-lg text-gray-600 hover:bg-gray-100">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
          </svg>
          Esci
        </button>
      </div>
    </aside>

    <main class="flex-1 overflow-auto p-6 flex justify-center">
      <div class="max-w-2xl">
        <h1 class="text-4xl font-bold mb-8">NOME</h1>

        <input
          v-model="medicineName"
          type="text"
          placeholder="Digita il nome del farmaco oppure scannerizzalo tramite il lettore"
          class="w-full px-4 py-3 bg-white border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 mb-8"
        />

        <div class="mb-8">
          <h2 class="text-2xl font-bold mb-4">QUANTITA'</h2>
          <div class="flex items-center gap-4">
            <button 
              @click="decreaseQuantity"
              class="w-16 h-16 bg-white rounded-lg shadow-sm hover:shadow-md transition flex items-center justify-center text-2xl font-bold"
            >
              −
            </button>
            <input
              v-model.number="quantity"
              type="number"
              class="w-32 text-center px-4 py-3 bg-white border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 text-xl"
            />
            <button 
              @click="increaseQuantity"
              class="w-16 h-16 bg-white rounded-lg shadow-sm hover:shadow-md transition flex items-center justify-center text-2xl font-bold"
            >
              +
            </button>
          </div>
        </div>

        <div class="mb-8">
          <h2 class="text-2xl font-bold mb-4">SCADENZA</h2>
          <div class="flex gap-4">
            <input
              v-model="expiryDay"
              type="text"
              placeholder="Giorno"
              maxlength="2"
              class="flex-1 px-4 py-3 bg-white border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 text-center"
            />
            <input
              v-model="expiryMonth"
              type="text"
              placeholder="Mese"
              maxlength="2"
              class="flex-1 px-4 py-3 bg-white border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 text-center"
            />
            <input
              v-model="expiryYear"
              type="text"
              placeholder="Anno"
              maxlength="4"
              class="flex-1 px-4 py-3 bg-white border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 text-center"
            />
          </div>
        </div>

        <div class="fixed bottom-8 left-48 right-0 flex justify-center px-6">
            <button
                @click="addMedicine"
                class="bg-purple-600 hover:bg-purple-700 text-white font-semibold py-4 px-8 rounded-xl transition duration-200 transform hover:scale-[1.02] shadow-lg flex items-center justify-center gap-2"
            >
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
                Aggiungi Farmaco
            </button>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import logo from '@/assets/images/logo.png'

const router = useRouter()

const medicineName = ref('')
const quantity = ref(10)
const expiryDay = ref('')
const expiryMonth = ref('')
const expiryYear = ref('')

const increaseQuantity = () => {
  quantity.value++
}

const decreaseQuantity = () => {
  if (quantity.value > 0) {
    quantity.value--
  }
}

const addMedicine = () => {
  const medicine = {
    name: medicineName.value,
    quantity: quantity.value,
    expiryDate: `${expiryDay.value}/${expiryMonth.value}/${expiryYear.value}`
  }
  
  console.log('Farmaco aggiunto:', medicine)
  alert('Farmaco aggiunto con successo!')
  
  router.push('/home')
}

const logout = () => {
  router.push('/login')
}
</script>