<template>
  <section class="min-h-screen bg-gradient-to-b from-white to-cyan-100 py-16 px-6">
    <div class="max-w-4xl mx-auto bg-white shadow-xl rounded-2xl p-10 border border-cyan-100 relative z-10">
      <!-- LANGKAH 1: PILIH GENDER -->
      <div v-if="!genderSelected" class="text-center">
        <h2 class="text-3xl font-bold text-[#00B8D9] mb-6">Pilih Jenis Kelamin Anda</h2>
        <p class="text-gray-500 mb-10">Pilih salah satu untuk menyesuaikan hasil analisis karier.</p>
        <div class="flex justify-center gap-6 mb-8">
          <button
            v-for="g in ['Laki-laki', 'Perempuan']"
            :key="g"
            @click="selectGender(g)"
            class="px-10 py-4 rounded-xl border-2 border-[#00B8D9] text-[#00B8D9] font-semibold hover:bg-[#00B8D9] hover:text-white transition-all duration-300"
          >
            {{ g }}
          </button>
        </div>
      </div>

      <!-- LANGKAH 2: TES KARIER -->
      <div v-else>
        <h2 class="text-3xl font-bold text-center text-[#00B8D9] mb-8">
          Tes {{ category }}
        </h2>

        <div v-if="questions.length">
          <div
            v-for="(q, index) in questions"
            :key="q.id"
            class="mb-8 border-b border-gray-100 pb-6"
          >
            <h3 class="text-lg font-semibold text-gray-700 mb-6">
              {{ index + 1 }}. {{ q.question }}
            </h3>

            <!-- Pilihan -->
            <div class="flex flex-col gap-4">
              <div
                v-for="(opt, i) in q.options"
                :key="i"
                class="flex items-center p-4 border-2 rounded-xl cursor-pointer transition-all duration-300"
                :class="selectedAnswers[index] === opt
                  ? 'border-[#00B8D9] bg-[#00B8D9]/10'
                  : 'border-gray-200 hover:border-[#00B8D9]/40'"
                @click="selectAnswer(index, opt)"
              >
                <div
                  class="w-5 h-5 rounded-full border-2 flex items-center justify-center mr-4"
                  :class="selectedAnswers[index] === opt
                    ? 'border-[#00B8D9] bg-[#00B8D9]'
                    : 'border-gray-300'"
                >
                  <div
                    v-if="selectedAnswers[index] === opt"
                    class="w-2 h-2 bg-white rounded-full"
                  ></div>
                </div>
                <span
                  :class="selectedAnswers[index] === opt
                    ? 'text-[#00B8D9] font-medium'
                    : 'text-gray-600'"
                >
                  {{ opt }}
                </span>
              </div>
            </div>
          </div>

          <!-- Tombol navigasi -->
          <div class="flex justify-between items-center mt-8">
            <button
              @click="goBack"
              class="px-6 py-2 rounded-lg border text-[#00B8D9] border-[#00B8D9] hover:bg-[#00B8D9] hover:text-white transition-all"
            >
              ← Kembali
            </button>
            <button
              class="px-8 py-2 bg-[#00B8D9] text-white rounded-lg hover:bg-white hover:text-[#00B8D9] border border-[#00B8D9] transition-all"
              @click="submitAnswers"
            >
              Submit Jawaban →
            </button>
          </div>
        </div>

        <p v-else class="text-center text-gray-500">Memuat soal...</p>
      </div>
    </div>

    <!-- ALERT POPUP -->
    <div
      v-if="showAlert"
      class="fixed inset-0 bg-black/30 flex items-center justify-center z-50"
    >
      <div
        class="bg-white text-zinc-500 px-8 py-6 rounded-2xl shadow-2xl text-center w-[90%] max-w-md animate-fadeIn"
      >
        <h3 class="text-xl font-semibold mb-4">Hasil Analisis</h3>
        <p class="mb-6 whitespace-pre-line">{{ alertMessage }}</p>
        <button
          class="px-6 py-2 bg-[#00B8D9] text-white rounded-full hover:bg-cyan-600 transition-all"
          @click="showAlert = false"
        >
          Tutup
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"

const router = useRouter()
const props = defineProps({ category: String })

const genderSelected = ref(false)
const selectedGender = ref(null)
const questions = ref([])
const selectedAnswers = ref([])

const showAlert = ref(false)
const alertMessage = ref("")

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
  } catch (err) {
    console.error("❌ Gagal memuat soal:", err)
  }
}

function selectAnswer(qIndex, answer) {
  selectedAnswers.value[qIndex] =
    selectedAnswers.value[qIndex] === answer ? null : answer
}

function submitAnswers() {
  if (selectedAnswers.value.length < questions.value.length) {
    alertMessage.value = "Masih ada soal yang belum dijawab!"
    showAlert.value = true
    return
  }

  const payload = {
    category: props.category,
    gender: selectedGender.value,
    answers: selectedAnswers.value,
  }

  fetch("http://localhost:8000/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  })
    .then((res) => res.json())
    .then((data) => {
      alertMessage.value =
        data.analysis ||
        `Analisis berhasil untuk ${selectedGender.value}!`
      showAlert.value = true
    })
    .catch((err) => {
      console.error("Gagal mengirim jawaban:", err)
      alertMessage.value = "Terjadi kesalahan saat mengirim jawaban."
      showAlert.value = true
    })
}

function goBack() {
  router.push("/career")
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
  animation: fadeIn 0.25s ease-out;
}
</style>
