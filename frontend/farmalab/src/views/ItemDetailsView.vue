<template>
  <div class="flex h-screen bg-gray-100">
    <!-- Sidebar Component -->
    <Sidebar />

    <main class="flex-1 flex flex-col overflow-hidden">
      <div class="p-4 flex-shrink-0">
        <button @click="goBack" class="p-2 hover:bg-gray-200 rounded-lg transition">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
          </svg>
        </button>
      </div>

      <div class="flex-1 flex flex-col items-center justify-center px-8 pb-24">
        <div class="w-48 h-60 bg-white rounded-2xl shadow-lg flex items-center justify-center mb-8">
          <svg class="w-24 h-24 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
          </svg>
        </div>

        <div class="grid grid-cols-4 gap-6 w-full max-w-6xl">
          <div class="bg-white rounded-2xl p-5 shadow-sm">
            <h3 class="text-xl font-bold mb-4">Generali</h3>
            <div class="space-y-2 text-sm">
              <div>
                <p class="font-semibold">Nome:</p>
                <p class="text-gray-700">{{ medicine.name }}</p>
              </div>
              <div>
                <p class="font-semibold">Principio Attivo:</p>
                <p class="text-gray-700">{{ medicine.activeIngredient }}</p>
              </div>
              <div>
                <p class="font-semibold">Produttore:</p>
                <p class="text-gray-700">{{ medicine.manufacturer }}</p>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-2xl p-5 shadow-sm">
            <h3 class="text-xl font-bold mb-4">Conservazione</h3>
            <p class="text-sm text-gray-700 leading-relaxed">
              {{ medicine.storage }}
            </p>
          </div>

          <div class="bg-white rounded-2xl p-5 shadow-sm">
            <h3 class="text-xl font-bold mb-4">Controindicazioni</h3>
            <p class="text-sm text-gray-700 leading-relaxed">
              {{ medicine.contraindications }}
            </p>
          </div>

          <div class="bg-white rounded-2xl p-5 shadow-sm">
            <h3 class="text-xl font-bold mb-4">Effetti Collaterali</h3>
            <ul class="text-sm text-gray-700 space-y-1">
              <li v-for="effect in medicine.sideEffects" :key="effect">• {{ effect }}</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="flex-shrink-0 bg-red-500 text-black py-4 px-6 flex items-center justify-center gap-3">
        <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
        </svg>
        <span class="font-bold text-lg">Farmaco soggetto a prescrizione medica</span>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import Sidebar from '@/components/Sidebar.vue'

const router = useRouter()
const route = useRoute()

const medicine = ref({
  id: route.params.id || 1,
  name: 'Lexil 20cp 10g',
  activeIngredient: 'propantelina bromuro e bromazepam',
  manufacturer: 'Teofarma',
  storage: 'Conservare in un luogo asciutto, con temperatura che si aggira tra i 16 e i 30 C°',
  contraindications: 'Non somministrare lexil a soggetti cardiopatici o con forti disfunzioni cardiache. È vietata la somministrazione a soggetti con età inferiore ai 12 anni',
  sideEffects: ['Nausea', 'Vomito', 'Dolore addominale', 'Spasmi', 'Colite', 'Diarrea']
})

const goBack = () => {
  router.back()
}
</script>