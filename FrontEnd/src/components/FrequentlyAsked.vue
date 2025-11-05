<template>
  <section class="relative bg-gradient-to-br from-cyan-50 via-blue-50 to-purple-50 py-16 px-6 overflow-hidden">
    <!-- Bright Cyan Background Circles -->
    <div class="absolute inset-0 pointer-events-none">
      <!-- Large gradient circle top-left (BLUR) -->
      <div class="absolute -top-48 -left-48 w-[600px] h-[600px] bg-gradient-to-br from-cyan-300 to-blue-400 rounded-full opacity-40 blur-3xl"></div>
      
      <!-- Extra large circle top-right (NO BLUR - Bright accent) -->
      <div class="absolute -top-32 -right-40 w-[500px] h-[500px] bg-cyan-400 rounded-full opacity-25"></div>
      
      <!-- Medium circle middle-left (BLUR with gradient) -->
      <div class="absolute top-1/4 -left-32 w-96 h-96 bg-gradient-to-tr from-teal-300 to-cyan-300 rounded-full opacity-45 blur-2xl"></div>
      
      <!-- Large vibrant circle center-right (NO BLUR) -->
      <div class="absolute top-1/3 right-10 w-[450px] h-[450px] bg-gradient-to-bl from-pink-300 to-purple-300 rounded-full opacity-20"></div>
      
      <!-- Extra large gradient circle bottom-right (BLUR) -->
      <div class="absolute -bottom-56 -right-56 w-[700px] h-[700px] bg-gradient-to-tl from-cyan-300 via-blue-300 to-purple-300 rounded-full opacity-35 blur-3xl"></div>
      
      <!-- Medium circle bottom-left (NO BLUR) -->
      <div class="absolute bottom-20 left-1/4 w-80 h-80 bg-teal-300 rounded-full opacity-30"></div>
      
      <!-- Small accent circle (BLUR) -->
      <div class="absolute top-2/3 left-1/2 w-64 h-64 bg-gradient-to-r from-cyan-200 to-blue-300 rounded-full opacity-40 blur-xl"></div>
      
      <!-- Medium solid circle center (NO BLUR) -->
      <div class="absolute top-1/2 left-1/3 w-72 h-72 bg-cyan-300 rounded-full opacity-20"></div>
      
      <!-- Extra bright accent circle (NO BLUR) -->
      <div class="absolute top-1/4 right-1/3 w-64 h-64 bg-gradient-to-br from-aqua-300 to-cyan-300 rounded-full opacity-25"></div>
    </div>

    <!-- Bright Glassmorphism Overlay -->
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(6,182,212,0.1),transparent_50%)] pointer-events-none"></div>

    <!-- Content -->
    <div class="relative z-10">
      <div class="mx-auto p-10 max-w-5xl">
        <BubbleTeks>
          <template #title>Frequently Asked Questions</template>
          <template #subtitle>Anda Memiliki Pertanyaan?, Kami akan Menjawabnya</template>
        </BubbleTeks>
      </div>

      <div class="max-w-4xl mx-auto text-center mb-12">
        <h2 class="text-3xl md:text-4xl font-bold text-gray-800 mb-4">
          Pertanyaan yang Sering Diajukan
        </h2>
        <p class="text-gray-600 text-base md:text-lg">
          Berikut beberapa pertanyaan umum seputar tes kepribadian dan cara kerjanya.
        </p>
      </div>

      <div class="max-w-3xl mx-auto space-y-4">
        <div
          v-for="(faq, index) in faqs"
          :key="index"
          class="bg-white/70 backdrop-blur-md border border-cyan-200/60 rounded-2xl shadow-lg hover:shadow-xl hover:bg-white/80 hover:border-cyan-300 transition-all duration-300 overflow-hidden"
        >
          <button
            @click="toggleFAQ(index)"
            class="w-full flex justify-between items-center px-6 py-5 text-left focus:outline-none"
          >
            <span class="text-gray-800 font-medium text-lg">
              {{ faq.question }}
            </span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="w-5 h-5 text-cyan-500 transition-transform duration-300"
              :class="{ 'rotate-180': faq.open }"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
            </svg>
          </button>

          <div
            class="px-6 overflow-hidden transition-all duration-500 ease-in-out"
            :style="{ maxHeight: faq.open ? '200px' : '0px' }"
          >
            <p class="text-gray-600 text-sm md:text-base py-3">
              {{ faq.answer }}
            </p>
          </div>
        </div>
      </div>

      <div class="text-center text-gray-700 py-10 text-lg">
        Ada Pertanyaan? , Silahkan Hubungi Kami di 
        <a href="/contact" class="text-cyan-500 hover:text-cyan-600 transition-all duration-200 font-semibold">Contact</a>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";
import BubbleTeks from "../ui-components/BubbleTeks.vue";

const faqs = ref([
  {
    question: "Apakah tes ini gratis?",
    answer:
      "Ya, seluruh tes kepribadian di CareerPath.AI dapat kamu akses secara gratis tanpa biaya apa pun.",
    open: false,
  },
  {
    question: "Berapa lama waktu yang dibutuhkan untuk menyelesaikan tes?",
    answer:
      "Rata-rata peserta menyelesaikan tes dalam waktu sekitar 10–15 menit, tergantung pada kecepatan membaca dan menjawab.",
    open: false,
  },
  {
    question: "Apakah hasil tes saya akan disimpan?",
    answer:
      "Hasil tes kamu akan disimpan secara aman untuk keperluan analisis dan dapat kamu lihat kembali kapan saja.",
    open: false,
  },
  {
    question: "Apakah hasil tes ini bisa dipercaya?",
    answer:
      "Tes kami dirancang berdasarkan model psikometri yang umum digunakan, namun tetap hanya sebagai panduan, bukan penentu mutlak karier.",
    open: false,
  },
]);

function toggleFAQ(index) {
  faqs.value[index].open = !faqs.value[index].open;
}
</script>
