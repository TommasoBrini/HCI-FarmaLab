<template>
  <div class="min-h-screen relative flex items-center justify-center p-4">
    <div 
      class="absolute inset-0 bg-cover bg-center"
      :style="{ backgroundImage: `url(${bgImage})` }"
    >
      <div class="absolute inset-0 bg-black/30"></div>
    </div>

    <div class="relative z-10 w-full max-w-md">
      <div class="flex justify-center mb-8">
        <img :src="logo" alt="FarmaLab" class="h-24 w-auto" />
      </div>

      <div class="bg-white rounded-3xl shadow-2xl p-8">
        <h1 class="text-3xl font-bold text-center text-gray-900 mb-2">
          Bentornato
        </h1>
        <p class="text-center text-gray-600 text-sm mb-8">
          Ci sei mancato! Perfavore inserisci le credenziali
        </p>

        <form @submit.prevent="handleLogin" class="space-y-5">
          <div>
            <label class="block text-sm font-semibold text-gray-900 mb-2">
              Email
            </label>
            <input
              v-model="email"
              type="email"
              required
              placeholder="esempio: mario.rossi@gmail.com"
              class="w-full px-4 py-3 rounded-xl border border-gray-300 focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none transition text-sm"
            />
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-900 mb-2">
              Password
            </label>
            <div class="relative">
              <input
                v-model="password"
                :type="showPassword ? 'text' : 'password'"
                required
                placeholder="******"
                class="w-full px-4 py-3 rounded-xl border border-gray-300 focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none transition text-sm pr-12"
              />
              <button
                type="button"
                @click="showPassword = !showPassword"
                class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
              >
                <svg v-if="!showPassword" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                </svg>
                <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21" />
                </svg>
              </button>
            </div>
          </div>

          <div class="text-right">
            <a href="#" class="text-sm text-gray-700 hover:text-purple-600">
              Hai dimenticato la password?
            </a>
          </div>

          <button
            type="submit"
            class="w-full bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white font-semibold py-3.5 rounded-xl transition duration-200 transform hover:scale-[1.02] shadow-lg"
          >
            Accedi
          </button>
        </form>

        <div class="flex items-center gap-4 my-6">
          <div class="flex-1 h-px bg-gray-300"></div>
          <span class="text-sm text-gray-500">Oppure</span>
          <div class="flex-1 h-px bg-gray-300"></div>
        </div>

        <p class="text-center text-sm text-gray-700">
          Non hai un account? 
          <router-link to="/register" class="underline font-medium hover:text-purple-600">
            Registrati
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

import logo from '@/assets/images/logo.png'
import bgImage from '@/assets/images/background.jpg'
import { successAlert, errorAlert } from '@/utils/sweetalert'

const router = useRouter()
const email = ref('')
const password = ref('')
const showPassword = ref(false)

const handleLogin = async () => {
  if (!email.value || !password.value) {
    await errorAlert('Errore', 'Inserisci email e password')
    return
  }

  await successAlert('Login effettuato!', 'Benvenuto in FarmaLab')
  router.push('/home')
}
</script>