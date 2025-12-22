<template>
  <div class="min-h-screen bg-gray-900 flex items-center justify-center p-4">
    <div class="w-full max-w-md">
      <div class="text-center mb-8">
        <h1 class="text-5xl font-bold text-purple-500 mb-2">FarmaLab</h1>
      </div>

      <div class="bg-white rounded-2xl p-8 shadow-xl">
        <div class="flex items-center mb-6">
          <button @click="goBack" class="mr-4 hover:bg-gray-100 p-2 rounded-lg transition">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
          </button>
          <h2 class="text-2xl font-bold">Registrazione</h2>
        </div>

        <form @submit.prevent="handleRegister" class="space-y-4">
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium mb-1">Nome</label>
              <input
                v-model="form.nome"
                type="text"
                placeholder="Mario"
                required
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
              />
            </div>
            <div>
              <label class="block text-sm font-medium mb-1">Cognome</label>
              <input
                v-model="form.cognome"
                type="text"
                placeholder="Rossi"
                required
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
              />
            </div>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium mb-1">Email</label>
              <input
                v-model="form.email"
                type="email"
                placeholder="mario.rossi@example.com"
                required
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
              />
            </div>
            <div>
              <label class="block text-sm font-medium mb-1">Password</label>
              <input
                v-model="form.password"
                type="password"
                placeholder="******"
                required
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
              />
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium mb-1">Ruolo</label>
            <div class="relative">
              <select
                v-model="form.ruolo"
                required
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 appearance-none"
              >
                <option value="">Seleziona ruolo</option>
                <option value="farmacista">Farmacista</option>
                <option value="utente">Infermiera/e</option>
              </select>
              <div class="absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none">
                <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </div>
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium mb-1">Luogo di lavoro</label>
            <div class="relative">
              <select
                v-model="form.luogoLavoro"
                required
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 appearance-none"
              >
                <option value="">Seleziona farmacia</option>
                <option value="farmacia-roma">Farmacia Roma</option>
                <option value="farmacia-milano">Farmacia Milano</option>
                <option value="farmacia-napoli">Farmacia Napoli</option>
              </select>
              <div class="absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none">
                <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </div>
            </div>
          </div>

          <div class="text-right">
            <a href="" @click.prevent="betaInfo" class="text-sm text-gray-600 hover:text-purple-600">
              Non vedo il mio luogo di lavoro
            </a>
          </div>

          <button
            type="submit"
            class="w-full bg-purple-600 text-white py-3 rounded-lg font-medium hover:bg-purple-700 transition"
          >
            Registrati
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { successAlert, errorAlert, infoAlert } from '@/utils/sweetalert'

const router = useRouter()

const form = ref({
  nome: '',
  cognome: '',
  email: '',
  password: '',
  ruolo: '',
  luogoLavoro: ''
})

const goBack = () => {
  router.push('/login')
}

const handleRegister = async () => {
  console.log('Registrazione:', form.value)

  if (!form.value.nome || !form.value.cognome || !form.value.email || !form.value.password || !form.value.ruolo) {
    errorAlert('Dati mancanti', 'Compila tutti i campi obbligatori')
    return
  }

  if (form.value.password.length < 8) {
    errorAlert('Password troppo corta', 'La password deve avere almeno 8 caratteri')
    return
  }

  const payload = {
    name: form.value.nome,
    surname: form.value.cognome,
    email: form.value.email,
    password: form.value.password,
    role: form.value.ruolo,
    way_id: null
  }

  try {
    const res = await fetch('http://localhost:8000/users', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })

    if (!res.ok) {
      const errBody = await res.json().catch(() => null)
      const message = errBody?.detail || errBody?.message || res.statusText || 'Errore nella registrazione'
      throw new Error(message)
    }

    successAlert('Registrazione completata!', 'Benvenuto in FarmaLab')
    router.push('/home')
  } catch (err: any) {
    console.error('Errore registrazione:', err)
    errorAlert('Registrazione fallita', err.message || 'Si è verificato un errore')
  }
}

const betaInfo = () => {
  infoAlert('Ops, sei in modalità beta', 'Questa funzionalità è in sviluppo.')
}
</script>