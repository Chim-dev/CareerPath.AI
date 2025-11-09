<template>
  <section class="relative min-h-screen bg-gradient-to-br from-cyan-50 via-blue-50 to-purple-50 py-16 px-6 overflow-hidden">
    <!-- background seperti onlinetest -->
    <div class="fixed inset-0 pointer-events-none z-0">
      <div class="absolute -top-48 -left-48 w-[600px] h-[600px] bg-gradient-to-br from-cyan-300 to-blue-400 rounded-full opacity-40 blur-3xl"></div>
      <div class="absolute -top-32 -right-40 w-[500px] h-[500px] bg-cyan-400 rounded-full opacity-25"></div>
      <div class="absolute -bottom-56 -right-56 w-[700px] h-[700px] bg-gradient-to-tl from-cyan-300 via-blue-300 to-purple-300 rounded-full opacity-35 blur-3xl"></div>
    </div>

    <!-- card utama -->
    <div class="relative z-10 max-w-3xl mx-auto bg-white/80 backdrop-blur-md shadow-2xl rounded-3xl border-2 border-cyan-200/60 p-10 md:p-16 text-center">
      <h2 class="text-4xl font-bold text-gray-800 mb-4">Hasil Analisis Karier Anda</h2>
      <p class="text-gray-600 mb-8 leading-relaxed whitespace-pre-line">{{ resultStore.analysis }}</p>

      <div class="text-left mb-8">
        <h3 class="text-2xl font-semibold text-cyan-700 mb-3">🎯 Rekomendasi Karier</h3>
        <ul class="list-decimal list-inside text-gray-700 space-y-2">
          <li v-for="(career, i) in resultStore.recommendations" :key="i">
            {{ career }}
          </li>
        </ul>
      </div>

      <p class="text-lg text-gray-600 mb-6">
        ✨ Tingkat Kepercayaan: 
        <span class="font-bold text-cyan-600">{{ (resultStore.confidence * 100).toFixed(0) }}%</span>
      </p>

      <button
        @click="goBack"
        class="px-8 py-3 bg-gradient-to-r from-cyan-400 to-blue-500 text-white rounded-xl font-semibold hover:from-cyan-500 hover:to-blue-600 transition-all duration-300 shadow-lg"
      >
        Kembali ke Tes
      </button>
    </div>
  </section>
</template>

<script setup>
import { useRouter } from "vue-router"
import { resultStore } from "../stores/resultStores"

const router = useRouter()

function goBack() {
  router.push("/career")
}
</script>
