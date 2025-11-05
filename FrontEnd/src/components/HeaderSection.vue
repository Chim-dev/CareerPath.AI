<template>
  <section
    class="relative flex items-center justify-center h-screen bg-cover bg-center bg-fixed px-6 md:px-16"
    :style="{ backgroundImage: `url(${bgImage})` }"
  >
    <div class="absolute inset-0 bg-[#00B8D9]/50"></div>

    <div
      class="relative z-10 text-center max-w-4xl mx-auto flex flex-col items-center justify-center text-white space-y-8"
    >
      <!-- Tombol kecil atas -->
      <button
        class="px-5 py-2 border border-white/60 rounded-full text-sm font-semibold backdrop-blur-md hover:bg-white hover:text-[#00B8D9] transition-all"
      >
        Discover Your Perfect Career Path
      </button>

      <!-- Judul besar -->
      <h1
        class="text-4xl md:text-6xl font-extrabold leading-snug tracking-tight text-white drop-shadow-sm"
      >
        Find Your Dream Career <br />
        With <span class="text-cyan-200 ">AI-Powered Insights</span>
      </h1>

      <!-- Deskripsi -->
      <p class="text-base md:text-lg text-white/90 max-w-2xl leading-relaxed">
        Take our comprehensive career assessment test and unlock personalized
        recommendations tailored to your skills, interests, and goals.
      </p>

      <!-- Tombol aksi -->
      <div class="flex flex-col sm:flex-row gap-4 mt-4">
        <button
          @click="scrollToCareerCards"
          class="px-8 py-3 rounded-full font-semibold shadow-md hover:text-white bg-white text-[#00B8D9] hover:bg-cyan-400 transition-all duration-300 text-lg"
        >
          Start Free Assessment
        </button>
      </div>

      <!-- Info kecil bawah -->
      <div class="flex items-center justify-center gap-6 text-sm text-white/80 mt-6">
        <span>⏱ 5-minute test</span>
        <span>💰 100% Free</span>
        <span>✨ Personalized results</span>
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
