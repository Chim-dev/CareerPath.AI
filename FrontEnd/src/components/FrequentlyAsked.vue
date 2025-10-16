<template>
  <section class="bg-gradient-to-b from-cyan-200 to-white py-16 px-6">
    <div class="mx-auto p-10 max-w-5xl ">
        <BubbleTeks class="">
            <template #title>Frequently Asked Questions</template>
            <template #subtitle>Anda Memiliki Pertanyaan?, Kami akan Menjawabnya</template>
        </BubbleTeks>
    </div>
    <div class="max-w-4xl mx-auto text-center mb-12">
      <h2 class="text-3xl md:text-4xl font-bold text-zinc-800 mb-4">
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
        class="overflow-hidden transition-all duration-300"
      >
        <button
          @click="toggleFAQ(index)"
          class="w-full flex justify-between items-center px-6 py-4 text-left focus:outline-none"
        >
          <span class="text-[#0D1B2A] font-medium text-lg">
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

    <div class="text-center text-black py-10 text-lg/loose">
        Ada Pertanyaan? , Silahkan Hubungi Kami di <a href="/contact" class="text-cyan-400 hover:text-cyan-500 transition-all duration-200">Contact</a>
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
