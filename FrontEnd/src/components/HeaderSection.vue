<template>
  <section
    class="relative flex items-center justify-center h-screen bg-cover bg-center bg-fixed px-6 md:px-16"
    :style="{ backgroundImage: `url(${bgImage})` }"
  >
    <!-- Lapisan transparan biru -->
    <div class="absolute inset-0 bg-[#00B8D9]/50"></div>

    <div
      class="relative z-10 text-center max-w-4xl mx-auto flex flex-col items-center justify-center text-white space-y-8"
    >
      <!-- Tombol kecil di atas -->
      <button
        class="px-5 py-2 border border-white/60 rounded-full text-sm font-semibold backdrop-blur-md hover:bg-white hover:text-[#00B8D9] transition-all"
      >
        Temukan Jalur Karier yang Tepat untukmu
      </button>

      <!-- Judul besar -->
      <h1
        class="text-4xl md:text-6xl font-extrabold leading-snug tracking-tight text-white drop-shadow-sm"
      >
        Temukan Karier Impianmu <br />
        Dengan <span class="text-cyan-200 ">Wawasan Bertenaga AI</span>
      </h1>

      <!-- Deskripsi -->
      <p class="text-base md:text-lg text-white/90 max-w-2xl leading-relaxed">
        Ikuti tes penilaian karier kami yang komprehensif dan dapatkan rekomendasi pribadi yang disesuaikan dengan keterampilan, minat, dan tujuanmu.
      </p>

      <!-- Tombol aksi -->
      <div class="flex flex-col sm:flex-row gap-4 mt-4">
        <button
          @click="scrollToCareerCards"
          class="px-8 py-3 rounded-full font-semibold shadow-md hover:text-white bg-white text-[#00B8D9] hover:bg-cyan-400 transition-all duration-300 text-lg"
        >
          Mulai Tes Gratis
        </button>
      </div>

      <!-- Info kecil di bawah -->
      <div class="flex items-center justify-center gap-6 text-sm text-white/80 mt-6">
        <span>⏱ Tes 5 menit</span>
        <span>💰 100% Gratis</span>
        <span>✨ Hasil yang Dipersonalisasi</span>
      </div>
    </div>
  </section>
</template>


<script setup>
import bgImage from "../assets/bg-asset-2.jpg";

function scrollToCareerCards() {
  const target = document.querySelector("#career");
  if (target) {
    target.scrollIntoView({ behavior: "smooth", block: "start" });
  }
}
</script>
