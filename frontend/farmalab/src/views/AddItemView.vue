<template>
  <div class="flex h-screen bg-gray-100">
    <Sidebar />
    <main class="flex-1 overflow-auto p-6 flex justify-center">
      <div class="max-w-2xl">
        <h1 class="text-4xl font-bold mb-8">NOME</h1>

        <div class="relative mb-8">
          <input
            v-model="medicineName"
            @input="onMedicineNameInput"
            @focus="showSuggestions = true"
            @blur="hideSuggestions"
            type="text"
            placeholder="Digita il nome del farmaco oppure scannerizzalo tramite il lettore"
            class="w-full px-4 py-3 bg-white border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
          />

          <div
            v-if="showSuggestions && suggestions.length > 0"
            class="absolute z-10 w-full mt-1 bg-white border border-gray-300 rounded-lg shadow-lg max-h-60 overflow-y-auto"
          >
            <button
              v-for="medicine in suggestions"
              :key="medicine.id"
              @mousedown.prevent="selectMedicine(medicine)"
              class="w-full px-4 py-3 text-left hover:bg-purple-50 transition border-b border-gray-100 last:border-b-0"
            >
              <div class="font-semibold">{{ medicine.name }}</div>
              <div class="text-xs text-gray-500">{{ medicine.active_ingredient }}</div>
            </button>
          </div>

          <!-- Loading indicator -->
          <div v-if="loading" class="absolute right-3 top-1/2 -translate-y-1/2">
            <svg class="animate-spin h-5 w-5 text-purple-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
          </div>
        </div>

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
              class="w-32 text-center px-4 py-3 bg-white border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 text-xl no-spinner"
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
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import Sidebar from '@/components/Sidebar.vue'
import { successAlert, errorAlert } from '@/utils/sweetalert'

const router = useRouter()

const medicineName = ref('')
const quantity = ref(10)
const expiryDay = ref('')
const expiryMonth = ref('')
const expiryYear = ref('')
const idMedicine = ref<number | null>(null)

// Autocomplete
const suggestions = ref<any[]>([])
const showSuggestions = ref(false)
const loading = ref(false)
let debounceTimer: number | null = null

const increaseQuantity = () => {
  quantity.value++
}

const decreaseQuantity = () => {
  if (quantity.value > 0) {
    quantity.value--
  }
}

const fetchSuggestions = async (query: string) => {
  if (!query || query.length < 2) {
    suggestions.value = []
    return
  }

  loading.value = true
  try {
    const res = await fetch(`http://localhost:8000/medicines?starts_with=${encodeURIComponent(query)}`)
    if (res.ok) {
      const data = await res.json()
      suggestions.value = data
    } else {
      suggestions.value = []
    }
  } catch (err) {
    console.error('Errore fetch suggerimenti:', err)
    suggestions.value = []
  } finally {
    loading.value = false
  }
}

const onMedicineNameInput = () => {
  if (debounceTimer) {
    clearTimeout(debounceTimer)
  }
  
  debounceTimer = window.setTimeout(() => {
    fetchSuggestions(medicineName.value)
  }, 300)
}

const selectMedicine = (medicine: any) => {
  medicineName.value = medicine.name
  idMedicine.value = medicine.id
  suggestions.value = []
  showSuggestions.value = false
  console.log('Farmaco selezionato:', medicine)
}

const hideSuggestions = () => {
  setTimeout(() => {
    showSuggestions.value = false
  }, 200)
}

const addMedicine = async () => {
  if (!medicineName.value) {
    await errorAlert('Errore', 'Inserisci il nome del farmaco')
    return
  }

  if (!idMedicine.value) {
    await errorAlert('Errore', 'Seleziona un farmaco dai suggerimenti')
    return
  }

  if (!expiryDay.value || !expiryMonth.value || !expiryYear.value) {
    await errorAlert('Errore', 'Inserisci la data di scadenza (giorno, mese, anno)')
    return
  }

  const pad = (v: string) => v.toString().padStart(2, '0')
  const dd = pad(expiryDay.value)
  const mm = pad(expiryMonth.value)
  const yyyy = expiryYear.value.toString()

  const isoDate = `${yyyy}-${mm}-${dd}`

  const payload = {
    id_medicine: idMedicine.value,
    expire_date: isoDate,
    quantity: quantity.value
  }

  try {
    const res = await fetch('http://localhost:8000/inventary', {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })

    if (!res.ok) {
      const errBody = await res.json().catch(() => null)
      const message = errBody?.detail || errBody?.message || res.statusText || 'Errore durante l\'operazione'
      throw new Error(message)
    }

    const data = await res.json().catch(() => null)
    console.log('Server response:', data)
    await successAlert('Farmaco aggiunto!', `${medicineName.value} è stato aggiunto al magazzino`)
    router.push('/home')
  } catch (err: any) {
    console.error('Errore addMedicine:', err)
    await errorAlert('Errore', err.message || 'Si è verificato un errore')
  }
}

const fillDemo = async () => {
  medicineName.value = 'Tachipirina'
  quantity.value = 120
  expiryDay.value = '30'
  expiryMonth.value = '06'
  expiryYear.value = '2026'
  idMedicine.value = 1
  await successAlert('Scannerizzato', 'Scannerizzazione completata con successo!')
}

const onKeyDown = (e: KeyboardEvent) => {
  const isSelectAll = (e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'a'
  if (isSelectAll) {
    e.preventDefault()
    fillDemo()
  }
}

onMounted(() => window.addEventListener('keydown', onKeyDown))
onBeforeUnmount(() => window.removeEventListener('keydown', onKeyDown))
</script>

<style scoped>
input.no-spinner::-webkit-outer-spin-button,
input.no-spinner::-webkit-inner-spin-button {
  -webkit-appearance: none;
  appearance: none;
  margin: 0;
}
input.no-spinner {
  -webkit-appearance: textfield;
  -moz-appearance: textfield;
  appearance: textfield;
}
</style>