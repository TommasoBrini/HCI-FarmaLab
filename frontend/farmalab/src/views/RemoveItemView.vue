<template>
  <div class="flex h-screen bg-gray-100">
    <Sidebar />

    <main class="flex-1 overflow-hidden flex flex-col h-screen">
    <div class="flex items-center justify-between p-4">
        <button @click="goBack" class="p-2 hover:bg-gray-200 rounded-lg transition">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        </button>

        <button @click="goToDetails" class="p-2 hover:bg-gray-200 rounded-full transition">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        </button>
    </div>

    <div class="flex-1 flex flex-col items-center justify-center px-6 py-4">
        <div class="w-48 h-60 bg-white rounded-2xl shadow-lg flex items-center justify-center mb-2 overflow-hidden">
          <img
            v-if="medicine.image"
            :src="medicine.image"
            alt="Medicine image"
            class="max-w-full max-h-full object-cover"
          />
          <svg v-else class="w-24 h-24 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
          </svg>
        </div>
        

        <div class="w-full max-w-xl space-y-3 mb-6">
        <div class="bg-white rounded-xl p-3 shadow-sm">
            <span class="font-bold">Nome:</span>
            <span class="ml-2">{{ medicine.name }}</span>
        </div>

        <div class="bg-white rounded-xl p-3 shadow-sm">
            <span class="font-bold">Quantità:</span>
            <span class="ml-2">{{ medicine.quantity }}</span>
        </div>

        <div class="bg-white rounded-xl p-3 shadow-sm">
            <span class="font-bold">Scadenza:</span>
            <span class="ml-2">{{ medicine.expiryDate }}</span>
        </div>
        </div>

        <div class="flex items-center gap-3 mb-6">
        <button 
            @click="decreaseQuantity"
            class="w-12 h-12 bg-white rounded-lg shadow-md hover:shadow-lg transition flex items-center justify-center text-xl font-bold"
        >
            −
        </button>
        <input
            v-model.number="quantityToRemove"
            type="number"
            class="w-24 text-center px-3 py-2 bg-white border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 text-lg no-spinner"
        />
        <button 
            @click="increaseQuantity"
            class="w-12 h-12 bg-white rounded-lg shadow-md hover:shadow-lg transition flex items-center justify-center text-xl font-bold"
        >
            +
        </button>
        </div>

        <div class="w-full max-w-xl space-y-3">
        <button
            @click="updateQuantity"
            class="w-full bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 rounded-xl transition duration-200 shadow-lg"
        >
            Aggiorna Quantità
        </button>

        <button
            @click="removeEntireBatch"
            class="w-full bg-white hover:bg-gray-50 text-purple-600 font-semibold py-3 rounded-xl transition duration-200 border-2 border-purple-600"
        >
            Rimuovi Intero Lotto
        </button>
        </div>
    </div>
    </main>

  </div>
</template>
<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import Sidebar from '@/components/Sidebar.vue'
import { confirmAlert, successAlert, errorAlert } from '@/utils/sweetalert'

const router = useRouter()
const route = useRoute()

const rawId = route.params.idMedicine
const id = Number(Array.isArray(rawId) ? rawId[0] : rawId ?? 1)

const rawExpire = route.params.expireDate
const expireDate: string = Array.isArray(rawExpire) ? (rawExpire[0] ?? '2026-01-01') : (rawExpire ?? '2026-01-01')
const arrayDate = expireDate.split(' ')
const padDay = (v: string) => v.toString().padStart(2, '0')
const rawDay = arrayDate[0] ?? '1'
const dayForModel = padDay(rawDay.replace(/[^0-9]/g, ''))
const dateModel = arrayDate.length === 3 ? `${arrayDate[2]}-${convertMonth(arrayDate[1] || 'Gennaio')}-${dayForModel}` : '2026-01-01'
console.log('dateModel:', dateModel)
function convertMonth(monthStr: string): string {
  const months: Record<string, string> = {
    'gennaio': '01',
    'febbraio': '02',
    'marzo': '03',
    'aprile': '04',
    'maggio': '05',
    'giugno': '06',
    'luglio': '07',
    'agosto': '08',
    'settembre': '09',
    'ottobre': '10',
    'novembre': '11',
    'dicembre': '12'
  }
  return months[monthStr.toLowerCase()] || '01'
}

const medicine = ref({
  id: id,
  name: 'Lexil 20cp 10g',
  quantity: '30 unità',
  expiryDate: '1 Gennaio 2026',
  image: ''
})

const quantityToRemove = ref(10)

onMounted(async () => {
  try {
    const url = `http://localhost:8000/inventary/${id}/${dateModel}`
    const res = await fetch(url)

    if (res.ok) {
      const data = await res.json()
      console.log('Dati inventario caricati:', data)
      medicine.value = {
        id: data.id_medicine,
        name: data.medicine_name,
        quantity: `${data.quantity} unità`,
        expiryDate: expireDate,
        image: data.image
      }
      quantityToRemove.value = data.quantity
    }
  } catch (err) {
    console.error('Errore caricamento dati:', err)
  }
})

const increaseQuantity = () => {
  quantityToRemove.value++
}

const decreaseQuantity = () => {
  if (quantityToRemove.value > 0) {
    quantityToRemove.value--
  }
}

const updateQuantity = async () => {
  const result = await confirmAlert({
    title: 'Aggiorna quantità?',
    text: `Stai per aggiornare ${quantityToRemove.value} unità`,
    confirmButtonText: 'Sì, aggiorna',
    cancelButtonText: 'Annulla'
  })

  if (result.isConfirmed) {
    try {
      const url = `http://localhost:8000/inventary/${id}/${dateModel}`
      const res = await fetch(url, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ quantity: quantityToRemove.value })
      })

      if (res.ok) {
        await successAlert('Quantità aggiornata!', `${quantityToRemove.value} unità sono state aggiornate`)
        router.push('/home')
      } else {
        const errBody = await res.json().catch(() => null)
        const message = errBody?.detail || errBody?.message || res.statusText || 'Errore durante l\'aggiornamento'
        await errorAlert('Errore', message)
      }
    } catch (err: any) {
      console.error('Errore updateQuantity:', err)
      await errorAlert('Errore', err.message || 'Si è verificato un errore')
    }
  }
}

const removeEntireBatch = async () => {
  const result = await confirmAlert({
    title: 'Rimuovere intero lotto?',
    text: 'Questa azione non può essere annullata',
    confirmButtonText: 'Sì, elimina tutto',
    cancelButtonText: 'Annulla'
  })

  if (result.isConfirmed) {
    try {
      const url = `http://localhost:8000/inventary/${id}/${dateModel}`
      const res = await fetch(url, { method: 'DELETE' })
      if (res.status === 204 || res.ok) {
        await successAlert('Lotto rimosso!', 'L\'intero lotto è stato eliminato')
        router.push('/home')
      } else {
        const errBody = await res.json().catch(() => null)
        const message = errBody?.detail || errBody?.message || res.statusText || 'Errore durante la cancellazione'
        await errorAlert('Errore', message)
      }
    } catch (err: any) {
      console.error('Errore removeEntireBatch:', err)
      await errorAlert('Errore', err.message || 'Si è verificato un errore')
    }
  }
}

const goBack = () => {
  router.push('/home')
}

const goToDetails = () => {
  router.push(`/item-details/${medicine.value.id}`)
}

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