<template>
  <section
    class="relative min-h-screen bg-gradient-to-br from-cyan-50 via-blue-50 to-purple-50 py-12 px-4 md:px-6 overflow-hidden">

    <!-- Background Circles -->
    <div class="fixed inset-0 pointer-events-none z-0">
      <div class="absolute -top-48 -left-48 w-[400px] h-[400px] bg-gradient-to-br from-cyan-300 to-blue-400 rounded-full opacity-30 blur-2xl"></div>
      <div class="absolute -top-20 -right-20 w-[320px] h-[320px] bg-cyan-300 rounded-full opacity-20 blur-xl"></div>
      <div class="absolute top-1/4 -left-20 w-72 h-72 bg-gradient-to-tr from-teal-300 to-cyan-300 rounded-full opacity-30 blur-xl"></div>
      <div class="absolute top-1/3 right-10 w-72 h-72 bg-gradient-to-bl from-pink-300 to-purple-300 rounded-full opacity-20 blur-xl"></div>
    </div>

    <!-- Main Content Card -->
    <div
      class="relative z-10 w-full max-w-3xl mx-auto bg-white/70 backdrop-blur-xl border border-white/30 shadow-2xl rounded-2xl overflow-hidden">

      <!-- LANGKAH 1: PILIH GENDER -->
      <div v-if="!genderSelected" class="p-8 md:p-10">
        <div class="text-center mb-10">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-800 mb-3">Career Assessment</h2>
          <p class="text-gray-600 text-base md:text-lg">Pilih jenis kelamin Anda untuk memulai</p>
        </div>

        <div class="flex flex-col sm:flex-row justify-center gap-4">
          <button
            v-for="g in ['Laki-laki', 'Perempuan']"
            :key="g"
            @click="selectGender(g)"
            class="px-10 py-4 rounded-xl border-2 border-cyan-400 bg-white text-gray-800 font-semibold 
                   hover:bg-cyan-400 hover:text-white transition-all duration-300 shadow-md hover:shadow-lg">
            {{ g }}
          </button>
        </div>
      </div>

      <!-- LANGKAH 2: TES KARIER -->
      <div v-else>
        <!-- Progress Bar -->
        <div class="bg-white/60 px-6 md:px-8 py-5 border-b border-gray-200 backdrop-blur-md">
          <div class="flex justify-between items-center mb-2">
            <h3 class="text-xs md:text-sm font-semibold text-gray-600">Career Assessment</h3>
            <span class="text-sm font-semibold text-cyan-500">
              Question {{ currentQuestionIndex + 1 }} / {{ questions.length }}
            </span>
          </div>

          <div class="w-full bg-gray-200 rounded-full h-3 overflow-hidden">
            <div
              class="bg-gradient-to-r from-cyan-400 to-blue-500 h-full rounded-full transition-all duration-500"
              :style="{ width: `${((currentQuestionIndex + 1) / questions.length) * 100}%` }"></div>
          </div>
        </div>

        <!-- Soal -->
        <div class="p-6 md:p-8 lg:p-10" v-if="questions.length">
          <h2 class="text-xl md:text-2xl font-bold text-gray-800 mb-6">
            {{ questions[currentQuestionIndex]?.question }}
          </h2>

          <div class="flex flex-col gap-3 md:gap-4">
            <div
              v-for="(opt, i) in questions[currentQuestionIndex]?.options"
              :key="i"
              class="flex items-start p-4 md:p-5 border-2 rounded-xl cursor-pointer transition-all duration-300"
              :class="selectedAnswers[currentQuestionIndex] === opt
                ? 'border-cyan-400 bg-gradient-to-r from-cyan-50 to-blue-50 shadow'
                : 'border-gray-200 hover:border-cyan-300 bg-white'"
              @click="selectAnswer(currentQuestionIndex, opt)">

              <div
                class="w-6 h-6 rounded-full border-2 flex items-center justify-center mr-4"
                :class="selectedAnswers[currentQuestionIndex] === opt
                  ? 'border-cyan-500 bg-cyan-500'
                  : 'border-gray-300 bg-white'">
                <div v-if="selectedAnswers[currentQuestionIndex] === opt"
                  class="w-3 h-3 bg-white rounded-full"></div>
              </div>

              <span class="text-base md:text-lg"
                :class="selectedAnswers[currentQuestionIndex] === opt
                  ? 'text-cyan-700 font-semibold'
                  : 'text-gray-700'">
                {{ opt }}
              </span>
            </div>
          </div>

          <!-- Tombol Navigasi -->
          <div class="flex justify-between items-center gap-3 mt-8">
            <button
              @click="currentQuestionIndex === 0 ? goBack() : previousQuestion()"
              class="flex items-center gap-2 px-5 py-2.5 rounded-xl border border-gray-300 text-gray-600 
                     hover:bg-red-400 hover:text-white transition-all duration-300">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none"
                viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
              </svg>
              {{ currentQuestionIndex === 0 ? 'Kembali' : 'Previous' }}
            </button>

            <button
              v-if="currentQuestionIndex < questions.length - 1"
              @click="nextQuestion"
              :disabled="!selectedAnswers[currentQuestionIndex]"
              class="flex items-center gap-2 px-6 py-3 rounded-xl bg-gradient-to-r from-cyan-400 to-blue-500 
                     text-white font-semibold hover:from-cyan-500 hover:to-blue-600 transition-all duration-300 
                     disabled:opacity-50 disabled:cursor-not-allowed">
              Next >
            </button>

            <button
              v-else
              @click="submitAnswers"
              :disabled="!selectedAnswers[currentQuestionIndex] || loading"
              class="flex items-center gap-2 px-6 py-3 rounded-xl bg-gradient-to-r from-cyan-400 to-blue-500 
                     text-white font-semibold hover:from-cyan-500 hover:to-blue-600 transition-all duration-300 
                     disabled:opacity-50 disabled:cursor-not-allowed">
              <span v-if="loading">⏳ Menganalisis...</span>
              <span v-else>Submit</span>
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
import api from "@/api/client.js"
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
  const unanswered = selectedAnswers.value.findIndex(a => a === null)
  if (unanswered !== -1) {
    alert(`Masih ada soal yang belum dijawab! (Nomor ${unanswered + 1})`)
    return
  }

  loading.value = true
  try {
    const payload = {
      category: props.category,
      gender: selectedGender.value,
      questions: questions.value.map(q => q.question),
      answers: selectedAnswers.value,
    }
    
    const response = await api.post("/analyze", payload)

    resultStore.analysis = response.data.analysis
    resultStore.recommendations = response.data.career_recommendations
    resultStore.confidence = response.data.confidence_score

    router.push("/result")

  } catch (error) {
    console.error(error)
    alert("Error saat menganalisis hasil. Coba lagi.")
  } finally {
    loading.value = false
  }
}

function goBack() {
  router.push("/")
}
</script>
