<template>
  <div class="flex h-screen bg-gray-100">
    <Sidebar />
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
import Sidebar from '@/components/Sidebar.vue'
import { successAlert, errorAlert } from '@/utils/sweetalert'


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

const addMedicine = async () => {
  if (!medicineName.value) {
    await errorAlert('Errore', 'Inserisci il nome del farmaco')
    return
  }

  const medicine = {
    name: medicineName.value,
    quantity: quantity.value,
    expiryDate: `${expiryDay.value}/${expiryMonth.value}/${expiryYear.value}`
  }
  
  console.log('Farmaco aggiunto:', medicine)
  await successAlert('Farmaco aggiunto!', `${medicineName.value} è stato aggiunto al magazzino`)
  router.push('/home')
}
</script>