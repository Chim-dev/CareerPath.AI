<template>
    <section class="min-h-screen bg-gradient-to-b from-white to-cyan-50 py-16 px-6">
        <div class="max-w-4xl mx-auto bg-white shadow-xl rounded-2xl p-10 border border-cyan-100">
            <h2 class="text-3xl font-bold text-center text-[#00B8D9] mb-6">
                Tes {{ category }}
            </h2>

            <div v-if="questions.length">
                <div v-for="(q, index) in questions" :key="q.id" class="mb-8 border-b border-gray-100 pb-6">
                    <h3 class="text-lg font-semibold text-gray-700 mb-6">
                        {{ index + 1 }}. {{ q.question }}
                    </h3>

                    <!-- Pilihan -->
                    <div class="flex flex-wrap justify-center gap-8">
                        <div v-for="(opt, i) in q.options" :key="i"
                            class="flex flex-col items-center cursor-pointer transition-transform duration-300"
                            @click="selectAnswer(index, opt)">
                            <span class="text-sm mb-2 transition-colors duration-300" :class="selectedAnswers[index] === opt
                                ? 'text-cyan-600 font-semibold'
                                : 'text-gray-500'">
                                {{ opt }}
                            </span>

                            <div class="w-10 h-10 rounded-full border-2 transition-all duration-300" :class="[
                                getCircleBorderColor(opt),
                                selectedAnswers[index] === opt ? getCircleFillColor(opt) : 'bg-transparent'
                            ]"></div>
                        </div>
                    </div>
                </div>

                <button
                    class="w-full bg-[#00B8D9] text-white py-3 rounded-lg mt-6 hover:bg-white hover:text-[#00B8D9] border border-[#00B8D9] transition-all duration-300 font-medium"
                    @click="submitAnswers">
                    Submit Jawaban
                </button>

                <button
                    class="w-full bg-[#f7f7f7] text-[#00B8D9] py-3 rounded-lg mt-4 hover:bg-[#00B8D9] hover:text-white border border-[#00B8D9] transition-all duration-300 font-medium"
                    @click="goBack">
                    Kembali
                </button>
            </div>

            <p v-else class="text-center text-gray-500">Memuat soal...</p>
        </div>
        <!-- ALERT POPUP -->
        <div v-if="showAlert" class="fixed inset-0 bg-black/30 flex items-center justify-center z-50">
            <div
                class="bg-white text-zinc-500 px-8 py-6 rounded-2xl shadow-2xl text-center w-[90%] max-w-md animate-fadeIn">
                <h3 class="text-xl font-semibold mb-4">Hasil Analisis</h3>
                <p class="mb-6 whitespace-pre-line">{{ alertMessage }}</p>
                <button class="px-6 py-2 bg-[#00B8D9] text-white rounded-full hover:bg-cyan-600 transition-all"
                    @click="showAlert = false">
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
const showAlert = ref(false)
const alertMessage = ref("")
const props = defineProps({
    category: String
})

const questions = ref([])
const selectedAnswers = ref([])

onMounted(async () => {
    try {
        const fileName = props.category.replace(/[^a-zA-Z]/g, '') + '.json'
        console.log("🔍 Mencoba memuat:", fileName)
        const response = await fetch(`/questions/${fileName}`)
        if (!response.ok) throw new Error('File tidak ditemukan')
        questions.value = await response.json()
    } catch (err) {
        console.error("❌ Gagal memuat soal:", err)
    }
})

function getCircleBorderColor(option) {
    const text = option.toLowerCase()
    if (text.includes("sangat tidak setuju")) return "border-black"
    if (text.includes("tidak setuju")) return "border-gray-400"
    if (text.includes("netral")) return "border-gray-300"
    if (text.includes("setuju") && !text.includes("sangat")) return "border-cyan-300"
    if (text.includes("sangat setuju")) return "border-[#00B8D9]"
    return "border-gray-200"
}

function getCircleFillColor(option) {
    const text = option.toLowerCase()
    if (text.includes("sangat tidak setuju")) return "bg-black"
    if (text.includes("tidak setuju")) return "bg-gray-400"
    if (text.includes("netral")) return "bg-gray-200"
    if (text.includes("setuju") && !text.includes("sangat")) return "bg-cyan-300"
    if (text.includes("sangat setuju")) return "bg-[#00B8D9]"
    return "bg-gray-200"
}

function selectAnswer(qIndex, answer) {
    if (selectedAnswers.value[qIndex] === answer) {
        selectedAnswers.value[qIndex] = null
    } else (
        selectedAnswers.value[qIndex] = answer
    )
}


function submitAnswers() {
    if (selectedAnswers.value.length < questions.value.length) {
        alertMessage.value = "Masih ada soal yang belum dijawab!"
        showAlert.value = true
        return
    }

    const payload = {
        category: props.category,
        answers: selectedAnswers.value
    }

    fetch("http://localhost:8000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    })
        .then((res) => res.json())
        .then((data) => {
            alertMessage.value = data.analysis || "Analisis berhasil!"
            showAlert.value = true
        })
        .catch((err) => {
            console.error("Gagal mengirim jawaban:", err)
            alertMessage.value = "Terjadi kesalahan saat mengirim jawaban."
            showAlert.value = true
        })
}

function goBack() {
    router.push('/career')
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
