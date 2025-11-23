<template>
  <section
    class="relative py-50 px-6 bg-gradient-to-br from-cyan-50 via-white to-blue-50 overflow-hidden"
  >
    <!-- Background Decorative Glow -->
    <div class="absolute inset-0 pointer-events-none">
      <div
        class="absolute -top-32 -left-40 w-[500px] h-[500px] bg-cyan-300/25 blur-3xl rounded-full"
      ></div>
      <div
        class="absolute top-1/3 right-0 w-[450px] h-[450px] bg-purple-300/20 blur-2xl rounded-full"
      ></div>
    </div>

    <!-- TITLE -->
    <div class="relative z-10 text-center max-w-3xl mx-auto mb-16">
      <h2 class="text-4xl md:text-5xl font-extrabold text-gray-800 tracking-tight">
        Frequently Asked Questions
      </h2>
      <p class="mt-3 text-gray-600 text-lg">
        Berikut beberapa pertanyaan umum tentang layanan kami.
      </p>
    </div>

    <!-- FAQ LIST -->
    <div class="relative z-10 max-w-3xl mx-auto space-y-4">
      <div
        v-for="(faq, index) in faqs"
        :key="index"
        class="group bg-white/80 backdrop-blur-xl border border-gray-200/60 
               rounded-2xl shadow-sm hover:shadow-lg transition-all duration-300"
      >
        <!-- HEADER BUTTON -->
        <button
          @click="toggleFAQ(index)"
          class="w-full px-6 py-5 flex justify-between items-center text-left"
        >
          <span class="text-gray-800 text-lg font-semibold leading-snug">
            {{ faq.question }}
          </span>

          <!-- ICON -->
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-6 h-6 text-cyan-500 transition-transform duration-300"
            :class="{ 'rotate-180': faq.open }"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="2"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M19 9l-7 7-7-7"
            />
          </svg>
        </button>

        <!-- ANSWER -->
        <transition name="faq">
          <div
            v-if="faq.open"
            class="px-6 pb-5 overflow-hidden text-gray-600 text-base leading-relaxed"
          >
            {{ faq.answer }}
          </div>
        </transition>
      </div>
    </div>

    <!-- FOOTER -->
    <div class="text-center mt-16 text-gray-600 text-lg">
      Ada Pertanyaan Lain?  
      <a
        href="/contact"
        class="text-cyan-600 font-semibold hover:text-cyan-700 transition"
      >
        Hubungi Kami
      </a>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";

const faqs = ref([
  {
    question: "Apakah tes ini gratis?",
    answer:
      "Ya, semua tes di platform kami 100% gratis dan dapat kamu akses tanpa batas.",
    open: false,
  },
  {
    question: "Berapa lama menyelesaikan tes?",
    answer:
      "Rata-rata pengguna menyelesaikan tes dalam waktu 10-15 menit.",
    open: false,
  },
  {
    question: "Apakah hasil tes saya disimpan?",
    answer:
      "Hasil tes tidak disimpan. Kamu bebas mengulang tes kapan pun.",
    open: false,
  },
  {
    question: "Seberapa akurat tes ini?",
    answer:
      "Tes kami berbasis model psikometri modern dan memberikan hasil prediktif, namun tetap sebagai panduan.",
    open: false,
  },
]);

function toggleFAQ(index) {
  faqs.value[index].open = !faqs.value[index].open;
}
</script>

<style>
/* Smooth fade + slide animation */
.faq-enter-active,
.faq-leave-active {
  transition: all 0.3s ease;
}
.faq-enter-from {
  opacity: 0;
  transform: translateY(-8px);
}
.faq-enter-to {
  opacity: 1;
  transform: translateY(0px);
}
.faq-leave-from {
  opacity: 1;
  transform: translateY(0px);
}
.faq-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}
</style>
