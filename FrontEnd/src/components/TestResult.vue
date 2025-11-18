<template>
  <section class="relative min-h-screen bg-gradient-to-br from-cyan-50 via-blue-50 to-purple-50 py-14 px-4 md:px-6 overflow-hidden">
    
    <!-- Background -->
    <div class="fixed inset-0 pointer-events-none z-0">
      <div class="absolute -top-48 -left-48 w-[600px] h-[600px] bg-gradient-to-br from-cyan-300 to-blue-400 rounded-full opacity-40 blur-3xl"></div>
      <div class="absolute -top-32 -right-40 w-[500px] h-[500px] bg-cyan-400 rounded-full opacity-25"></div>
      <div class="absolute -bottom-56 -right-56 w-[700px] h-[700px] bg-gradient-to-tl from-cyan-300 via-blue-300 to-purple-300 rounded-full opacity-35 blur-3xl"></div>
    </div>

    <!-- Card Utama -->
    <div id="pdf-area" class="relative z-10 max-w-3xl mx-auto bg-white/90 backdrop-blur-md shadow-2xl rounded-3xl border border-cyan-200/60 p-8 md:p-14 text-center">

      <h2 class="text-3xl md:text-4xl font-extrabold text-gray-800 mb-8">📊 Hasil Analisis Karier Anda</h2>

      <!-- ANALISIS PER PARAGRAF DALAM CARD -->
      <div class="space-y-4 text-left mb-10">
        <div
          v-for="(block, idx) in analysisBlocks"
          :key="idx"
          :class="[
            'p-5 rounded-2xl shadow-md border text-sm md:text-base leading-relaxed',
            colorBlocks[idx % colorBlocks.length]
          ]"
        >
          {{ block }}
        </div>
      </div>

      <!-- Rekomendasi -->
      <div class="text-left mb-10">
        <h3 class="text-2xl font-semibold text-cyan-700 mb-3 flex items-center gap-2">
          🎯 Rekomendasi Karier
        </h3>
        <ul class="list-decimal list-inside text-gray-700 space-y-2">
          <li v-for="(career, i) in resultStore.recommendations" :key="i">
            {{ career }}
          </li>
        </ul>
      </div>

      <!-- Confidence -->
      <p class="text-lg text-gray-700 mb-8">
        ✨ Tingkat Kepercayaan: 
        <span class="font-bold text-cyan-600">{{ (resultStore.confidence * 100).toFixed(0) }}%</span>
      </p>

      <!-- Buttons -->
      <div class="flex flex-col md:flex-row gap-4 justify-center">
        <button
          @click="goBack"
          class="px-8 py-3 bg-gradient-to-r from-cyan-400 to-blue-500 text-white rounded-xl font-semibold hover:from-cyan-500 hover:to-blue-600 transition-all duration-300 shadow-lg"
        >
          ⬅ Kembali ke Tes
        </button>

        <button
          @click="downloadPDF"
          class="px-8 py-3 bg-white border border-cyan-400 text-cyan-700 font-semibold rounded-xl hover:bg-cyan-50 transition-all duration-300 shadow-md"
        >
          📄 Download PDF
        </button>
      </div>
    </div>

  </section>
</template>

<script setup>
import { computed } from "vue"
import { useRouter } from "vue-router"
import { resultStore } from "../stores/resultStores"
import html2pdf from "html2pdf.js/dist/html2pdf.bundle.min.js"

// router
const router = useRouter()
function goBack() {
  router.push("/career")
}

// warna bergantian
const colorBlocks = [
  "bg-red-50 border-red-200 text-red-800",
  "bg-blue-50 border-blue-200 text-blue-800",
  "bg-green-50 border-green-200 text-green-800",
  "bg-purple-50 border-purple-200 text-purple-800",
  "bg-yellow-50 border-yellow-200 text-yellow-800"
]

// pecah analisis menjadi paragraf / blok
const analysisBlocks = computed(() => {
  if (!resultStore.analysis) return []
  return resultStore.analysis
    .split(/\n\s*\n/)      // blok pisah per paragraf kosong
    .map(b => b.trim())
    .filter(b => b.length > 0)
})

// download PDF
function downloadPDF() {
  const element = document.getElementById("pdf-area")
  const opt = {
    margin: 0.5,
    filename: "career-analysis.pdf",
    image: { type: "jpeg", quality: 0.98 },
    html2canvas: { scale: 2, useCORS: true },
    jsPDF: { unit: "in", format: "a4", orientation: "portrait" }
  }
  html2pdf().from(element).set(opt).save()
}
</script>
