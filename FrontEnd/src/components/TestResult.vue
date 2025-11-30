<template>
  <section
    class="relative min-h-screen bg-gradient-to-br from-cyan-50 via-blue-50 to-purple-50 py-14 px-4 md:px-6 overflow-hidden"
  >
    <!-- Enhanced Background with Animation -->
    <div class="fixed inset-0 pointer-events-none z-0">
      <div
        class="absolute -top-48 -left-48 w-[600px] h-[600px] bg-gradient-to-br from-cyan-300 to-blue-400 rounded-full opacity-40 blur-3xl animate-pulse-slow"
      ></div>
      <div
        class="absolute -top-32 -right-40 w-[500px] h-[500px] bg-cyan-400 rounded-full opacity-25 animate-float"
      ></div>
      <div
        class="absolute -bottom-56 -right-56 w-[700px] h-[700px] bg-gradient-to-tl from-cyan-300 via-blue-300 to-purple-300 rounded-full opacity-35 blur-3xl animate-pulse-slow"
      ></div>
      <div
        class="absolute top-1/2 left-1/4 w-64 h-64 bg-gradient-to-r from-pink-200 to-purple-200 rounded-full opacity-20 blur-2xl animate-float-reverse"
      ></div>
    </div>

    <!-- Card with Enhanced Shadow -->
    <div
      class="relative z-10 max-w-4xl mx-auto bg-white/95 backdrop-blur-xl shadow-2xl rounded-3xl border-2 border-cyan-200/70 overflow-hidden"
    >
      <!-- Header Section with Gradient -->
      <div class="bg-gradient-to-r from-cyan-500 via-blue-500 to-purple-500 p-8 md:p-10 text-center relative overflow-hidden">
        <div class="absolute inset-0 bg-white/10 backdrop-blur-sm"></div>
        <div class="relative z-10">
          <div class="inline-block bg-white/20 backdrop-blur-md rounded-full px-6 py-2 mb-4">
            <span class="text-white font-semibold text-sm">Assessment Completed</span>
          </div>
          <h2 class="text-3xl md:text-5xl font-extrabold text-white mb-2 drop-shadow-lg">
             Hasil Analisis Karier
          </h2>
          <p class="text-cyan-50 text-lg">Temukan potensi terbaik Anda</p>
        </div>
      </div>

      <!-- Content Section -->
      <div class="p-8 md:p-12">
        <!-- Analisis Section -->
        <div class="mb-12">
          <div class="flex items-center gap-3 mb-6">
            <div class="w-1 h-8 bg-gradient-to-b from-cyan-500 to-blue-500 rounded-full"></div>
            <h3 class="text-2xl md:text-3xl font-bold text-gray-800">Analisis Kepribadian</h3>
          </div>
          
          <div class="space-y-5">
            <div
              v-for="(block, idx) in analysisBlocks"
              :key="idx"
              :class="[
                'p-6 rounded-2xl shadow-lg border-l-4 text-sm md:text-base leading-relaxed transform transition-all duration-300 hover:scale-[1.02] hover:shadow-xl',
                colorBlocks[idx % colorBlocks.length],
              ]"
              :style="{ animationDelay: `${idx * 0.1}s` }"
              class="animate-slide-in"
            >
              <div class="flex items-start gap-3">
                <span class="text-2xl flex-shrink-0">{{ emojiList[idx % emojiList.length] }}</span>
                <p class="flex-1">{{ block }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Podium Section -->
        <div class="mb-12">
          <div class="flex items-center gap-3 mb-8">
            <div class="w-1 h-8 bg-gradient-to-b from-yellow-500 to-orange-500 rounded-full"></div>
            <h3 class="text-2xl md:text-3xl font-bold text-gray-800">Top 3 Rekomendasi Karier</h3>
          </div>

          <div class="flex flex-col md:flex-row items-end justify-center gap-6 mb-4">
            <template v-for="(item, i) in podium" :key="i">
              <div
                v-if="item"
                class="podium-item flex flex-col items-center"
                :class="{
                  'order-2 md:order-2': i === 0,
                  'order-1 md:order-1': i === 1,
                  'order-3 md:order-3': i === 2,
                }"
                :style="{ animationDelay: `${i * 0.2}s` }"
              >
                <div
                  class="relative mb-4 transform transition-all duration-300 hover:scale-110"
                  :class="{ 'animate-bounce-slow': i === 0 }"
                >
                  <div
                    class="rounded-full flex items-center justify-center shadow-2xl"
                    :class="[
                      i === 0 ? 'w-20 h-20 bg-gradient-to-br from-yellow-300 via-yellow-400 to-yellow-500 border-4 border-yellow-200' : '',
                      i === 1 ? 'w-16 h-16 bg-gradient-to-br from-gray-300 via-gray-400 to-gray-500 border-4 border-gray-200' : '',
                      i === 2 ? 'w-16 h-16 bg-gradient-to-br from-orange-300 via-orange-400 to-orange-500 border-4 border-orange-200' : '',
                    ]"
                  >
                    <span class="text-4xl" v-if="i === 0">👑</span>
                    <span class="text-3xl font-bold text-white" v-else>{{ i + 1 }}</span>
                  </div>
                </div>

                <div
                  class="relative rounded-2xl p-5 mb-3 text-center shadow-lg"
                  :class="[
                    i === 0 ? 'bg-gradient-to-br from-yellow-50 to-yellow-100 border-2 border-yellow-400 w-full md:w-48' : '',
                    i === 1 ? 'bg-gradient-to-br from-gray-50 to-gray-100 border-2 border-gray-400 w-full md:w-44' : '',
                    i === 2 ? 'bg-gradient-to-br from-orange-50 to-orange-100 border-2 border-orange-400 w-full md:w-44' : '',
                  ]"
                >
                  <p
                    class="font-bold leading-tight"
                    :class="[
                      i === 0 ? 'text-yellow-900 text-base md:text-lg' : '',
                      i === 1 ? 'text-gray-900 text-sm md:text-base' : '',
                      i === 2 ? 'text-orange-900 text-sm md:text-base' : '',
                    ]"
                  >
                    {{ item }}
                  </p>
                </div>

                <div
                  class="rounded-t-2xl shadow-xl"
                  :class="[
                    i === 0 ? 'bg-gradient-to-t from-yellow-400 to-yellow-300 h-40 w-full md:w-48' : '',
                    i === 1 ? 'bg-gradient-to-t from-gray-400 to-gray-300 h-32 w-full md:w-44' : '',
                    i === 2 ? 'bg-gradient-to-t from-orange-400 to-orange-300 h-24 w-full md:w-44' : '',
                  ]"
                ></div>
              </div>
            </template>
          </div>
        </div>

        <!-- Confidence Score -->
        <div class="bg-gradient-to-r from-cyan-50 to-blue-50 rounded-2xl p-6 mb-10 border border-cyan-200 shadow-md">
          <div class="flex items-center justify-between mb-3">
            <span class="text-lg font-semibold text-gray-800 flex items-center gap-2">
              ✨ Tingkat Kepercayaan
            </span>
            <span class="text-2xl font-black text-cyan-600">
              {{ (resultStore.confidence * 100).toFixed(0) }}%
            </span>
          </div>
          <div class="w-full bg-gray-200 rounded-full h-4 overflow-hidden shadow-inner">
            <div
              class="bg-gradient-to-r from-cyan-400 via-blue-500 to-purple-500 h-full rounded-full transition-all duration-1000 ease-out animate-progress"
              :style="{ width: `${resultStore.confidence * 100}%` }"
            ></div>
          </div>
        </div>

        <!-- Actions (PDF removed → hanya tombol kembali) -->
        <div class="flex justify-center">
          <button
            @click="goBack"
            class="px-8 py-4 bg-gradient-to-r from-cyan-500 to-blue-500 text-white rounded-xl font-semibold hover:from-cyan-600 hover:to-blue-600 transition-all duration-300 shadow-lg hover:shadow-2xl transform hover:-translate-y-1 flex items-center gap-2"
          >
            ⬅ Kembali ke Tes
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from "vue";
import { useRouter } from "vue-router";
import { resultStore } from "../stores/resultStores";

const router = useRouter();
function goBack() {
  router.push("/career");
}

// Enhanced color blocks
const colorBlocks = [
  "bg-red-50 border-red-400 text-red-900",
  "bg-blue-50 border-blue-400 text-blue-900",
  "bg-green-50 border-green-400 text-green-900",
  "bg-purple-50 border-purple-400 text-purple-900",
  "bg-yellow-50 border-yellow-400 text-yellow-900",
];

// Emoji list
const emojiList = ["", "", "", "", ""];

// Split analysis text
const analysisBlocks = computed(() => {
  if (!resultStore.analysis) return [];
  return resultStore.analysis
    .split(/\n\s*\n/)
    .map((b) => b.trim())
    .filter((b) => b.length > 0);
});

// Podium
const podium = computed(() => {
  const list = resultStore.recommendations || [];
  if (list.length < 3) return ["Menunggu data", "Menunggu data", "Menunggu data"];
  return [list[0], list[1], list[2]];
});
</script>

<style scoped>
/* semua animation sama, tidak dihapus */
@keyframes pulse-slow {
  0%, 100% { opacity: 0.4; transform: scale(1); }
  50% { opacity: 0.6; transform: scale(1.05); }
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}

@keyframes float-reverse {
  0%, 100% { transform: translateY(0px) translateX(0px); }
  50% { transform: translateY(20px) translateX(10px); }
}

@keyframes slide-in {
  from { opacity: 0; transform: translateX(-20px); }
  to { opacity: 1; transform: translateX(0); }
}

@keyframes bounce-slow {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

@keyframes progress {
  from { width: 0; }
}

.animate-pulse-slow { animation: pulse-slow 8s ease-in-out infinite; }
.animate-float { animation: float 6s ease-in-out infinite; }
.animate-float-reverse { animation: float-reverse 7s ease-in-out infinite; }
.animate-slide-in { animation: slide-in 0.6s ease-out forwards; }
.animate-bounce-slow { animation: bounce-slow 2s ease-in-out infinite; }
.animate-progress { animation: progress 1.5s ease-out; }
</style>
