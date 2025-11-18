<template>
  <section
    class="relative min-h-screen bg-gradient-to-br from-cyan-50 via-blue-50 to-purple-50 py-16 px-6 overflow-hidden">
    <!-- Background Circles -->
    <div class="fixed inset-0 pointer-events-none z-0">
      <div
        class="absolute -top-48 -left-48 w-[600px] h-[600px] bg-gradient-to-br from-cyan-300 to-blue-400 rounded-full opacity-40 blur-3xl" />
      <div class="absolute -top-32 -right-40 w-[500px] h-[500px] bg-cyan-400 rounded-full opacity-25" />
      <div
        class="absolute top-1/4 -left-32 w-96 h-96 bg-gradient-to-tr from-teal-300 to-cyan-300 rounded-full opacity-45 blur-2xl" />
      <div
        class="absolute top-1/3 right-10 w-[450px] h-[450px] bg-gradient-to-bl from-pink-300 to-purple-300 rounded-full opacity-20" />
      <div
        class="absolute -bottom-56 -right-56 w-[700px] h-[700px] bg-gradient-to-tl from-cyan-300 via-blue-300 to-purple-300 rounded-full opacity-35 blur-3xl" />
      <div class="absolute bottom-20 left-1/4 w-80 h-80 bg-teal-300 rounded-full opacity-30" />
      <div
        class="absolute top-2/3 left-1/2 w-64 h-64 bg-gradient-to-r from-cyan-200 to-blue-300 rounded-full opacity-40 blur-xl" />
      <div class="absolute top-1/2 left-1/3 w-72 h-72 bg-cyan-300 rounded-full opacity-20" />
    </div>

    <!-- Overlay Light -->
    <div
      class="fixed inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(6,182,212,0.1),transparent_50%)] pointer-events-none z-0">
    </div>

    <!-- Main Content Card -->
    <div
      class="relative z-10 max-w-4xl mx-auto bg-white/80 backdrop-blur-md shadow-2xl rounded-3xl overflow-hidden border-2 border-cyan-200/60">

      <!-- LANGKAH 1: PILIH GENDER -->
      <div v-if="!genderSelected" class="p-10 md:p-16">
        <div class="text-center mb-12">
          <h2 class="text-4xl md:text-5xl font-bold text-gray-800 mb-4">Career Assessment</h2>
          <p class="text-gray-600 text-lg">Pilih jenis kelamin Anda untuk memulai</p>
        </div>

        <div class="flex flex-col sm:flex-row justify-center gap-6 mb-8">
          <button
            v-for="g in ['Laki-laki', 'Perempuan']"
            :key="g"
            @click="selectGender(g)"
            class="px-12 py-5 rounded-2xl border-2 border-cyan-400 bg-white text-gray-800 font-semibold hover:bg-cyan-400 hover:text-white hover:border-transparent transition-all duration-300 shadow-lg hover:shadow-xl focus:outline-none focus:ring-0">
            {{ g }}
          </button>
        </div>
      </div>

      <!-- LANGKAH 2: TES KARIER -->
      <div v-else>
        <!-- Progress Bar -->
        <div class="bg-white px-8 py-6 border-b-2 border-gray-100">
          <div class="flex justify-between items-center mb-3">
            <h3 class="text-sm font-semibold text-gray-600">Career Assessment</h3>
            <span class="text-sm font-semibold text-cyan-500">
              Question {{ currentQuestionIndex + 1 }} of {{ questions.length }}
            </span>
          </div>
          <div class="w-full bg-gray-200 rounded-full h-3 overflow-hidden">
            <div
              class="bg-gradient-to-r from-cyan-400 to-blue-500 h-full rounded-full transition-all duration-500"
              :style="{ width: `${((currentQuestionIndex + 1) / questions.length) * 100}%` }" />
          </div>
        </div>

        <!-- Soal -->
        <div class="p-8 md:p-12" v-if="questions.length">
          <div class="mb-10">
            <h2 class="text-2xl md:text-3xl font-bold text-gray-800 mb-8">
              {{ questions[currentQuestionIndex]?.question }}
            </h2>

            <div class="flex flex-col gap-4">
              <div
                v-for="(opt, i) in questions[currentQuestionIndex]?.options"
                :key="i"
                class="flex items-start p-5 border-2 rounded-2xl cursor-pointer transition-all duration-300 hover:shadow-lg"
                :class="selectedAnswers[currentQuestionIndex] === opt
                  ? 'border-cyan-400 bg-gradient-to-r from-cyan-50 to-blue-50 shadow-md'
                  : 'border-gray-200 hover:border-cyan-300 bg-white'"
                @click="selectAnswer(currentQuestionIndex, opt)">
                <div
                  class="w-6 h-6 rounded-full border-2 flex items-center justify-center mr-4 flex-shrink-0 mt-0.5"
                  :class="selectedAnswers[currentQuestionIndex] === opt
                    ? 'border-cyan-500 bg-cyan-500'
                    : 'border-gray-300 bg-white'">
                  <div v-if="selectedAnswers[currentQuestionIndex] === opt" class="w-3 h-3 bg-white rounded-full" />
                </div>
                <span
                  class="text-base md:text-lg"
                  :class="selectedAnswers[currentQuestionIndex] === opt
                    ? 'text-cyan-700 font-semibold'
                    : 'text-gray-700'">
                  {{ opt }}
                </span>
              </div>
            </div>
          </div>

          <!-- Tombol Navigasi -->
          <div class="flex justify-between items-center gap-4 mt-8">
            <button
              @click="currentQuestionIndex === 0 ? goBack() : previousQuestion()"
              class="flex items-center gap-2 px-6 py-3 rounded-xl border-2 border-gray-300 text-gray-600 font-medium hover:bg-red-400 hover:text-white hover:border-transparent transition-all duration-300 focus:outline-none focus:ring-0">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24"
                stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
              </svg>
              {{ currentQuestionIndex === 0 ? 'Kembali' : 'Previous' }}
            </button>

            <button
              v-if="currentQuestionIndex < questions.length - 1"
              @click="nextQuestion"
              :disabled="!selectedAnswers[currentQuestionIndex]"
              class="flex items-center gap-2 px-8 py-3 rounded-xl bg-gradient-to-r from-cyan-400 to-blue-500 text-white font-semibold hover:from-cyan-500 hover:to-blue-600 transition-all duration-300 shadow-lg hover:shadow-xl disabled:opacity-50 disabled:cursor-not-allowed focus:outline-none focus:ring-0">
              Next
              <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24"
                stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
              </svg>
            </button>

            <button
              v-else
              @click="submitAnswers"
              :disabled="!selectedAnswers[currentQuestionIndex] || loading"
              class="flex items-center gap-2 px-8 py-3 rounded-xl bg-gradient-to-r from-cyan-400 to-blue-500 text-white font-semibold hover:from-cyan-500 hover:to-blue-600 transition-all duration-300 shadow-lg hover:shadow-xl disabled:opacity-50 disabled:cursor-not-allowed focus:outline-none focus:ring-0">
              <span v-if="loading">⏳ Menganalisis...</span>
              <span v-else>Submit</span>
              <svg v-if="!loading" xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24"
                stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import axios from "axios"
import { resultStore } from "../stores/resultStores"

const router = useRouter()
const props = defineProps({ category: String })

const genderSelected = ref(false)
const selectedGender = ref(null)
const questions = ref([])
const selectedAnswers = ref([])
const currentQuestionIndex = ref(0)
const loading = ref(false)

function selectGender(g) {
  selectedGender.value = g
  genderSelected.value = true
  loadQuestions()
}

async function loadQuestions() {
  try {
    const fileName = props.category.replace(/[^a-zA-Z]/g, "") + ".json"
    const response = await fetch(`/questions/${fileName}`)
    if (!response.ok) throw new Error("File tidak ditemukan")
    questions.value = await response.json()
    selectedAnswers.value = new Array(questions.value.length).fill(null)
  } catch (err) {
    console.error("❌ Gagal memuat soal:", err)
  }
}

function selectAnswer(qIndex, answer) {
  selectedAnswers.value[qIndex] = answer
}

function nextQuestion() {
  if (currentQuestionIndex.value < questions.value.length - 1) {
    currentQuestionIndex.value++
  }
}

function previousQuestion() {
  if (currentQuestionIndex.value > 0) {
    currentQuestionIndex.value--
  }
}

async function submitAnswers() {
  const unanswered = selectedAnswers.value.findIndex((ans) => ans === null)
  if (unanswered !== -1) {
    alert(`Masih ada soal yang belum dijawab! (Nomor ${unanswered + 1})`)
    return
  }

  const payload = {
    category: props.category,
    gender: selectedGender.value,
    answers: selectedAnswers.value,
  }

  loading.value = true
  try {
    const response = await axios.post("http://localhost:8000/analyze", payload, {
      headers: { "Content-Type": "application/json" },
      timeout: 30000,
    })

    const data = response.data

    // Simpan hasil ke store global
    resultStore.analysis = data.analysis
    resultStore.recommendations = data.career_recommendations
    resultStore.confidence = data.confidence_score

    // Arahkan ke halaman hasil
    router.push("/result")
  } catch (error) {
    console.error("❌ Error submit:", error)
    alert("Terjadi kesalahan saat menganalisis hasil. Coba lagi nanti.")
  } finally {
    loading.value = false
  }
}

function goBack() {
  router.push("/")
}
</script>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
.animate-fadeIn {
  animation: fadeIn 0.3s ease-out;
}
</style>
