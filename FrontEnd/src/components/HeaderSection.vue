<template>
  <section
    class="relative flex items-center justify-center min-h-screen bg-cover bg-center bg-fixed px-6 md:px-16 py-12 pt-20 md:pt-1 lg:pt-1 xl:pt-20"
    :style="{ backgroundImage: `url(${bgImage})` }"
  >
    <!-- Overlay -->
    <div class="absolute inset-0 bg-[#00B8D9]/50"></div>

    <!-- DROPLET / RIPPLE ANIMATION -->
    <div class="ripple-circle"></div>

    <!-- CONTENT -->
    <div
      class="relative z-10 text-center max-w-4xl mx-auto flex flex-col items-center justify-center text-white space-y-4 md:space-y-6 lg:space-y-8"
    >
      <button
        class="px-4 py-1.5 md:px-5 md:py-2 border border-white/60 rounded-full text-xs md:text-sm font-semibold backdrop-blur-md hover:bg-white hover:text-[#00B8D9] transition-all hero-item item-delay-1"
      >
        Temukan Jalur Karier yang Tepat untukmu
      </button>

      <h1
        class="text-3xl md:text-5xl lg:text-6xl font-extrabold leading-tight tracking-tight text-white hero-item item-delay-2"
      >
        Temukan Karier Masa Depan Impianmu <br />
        Dengan <span class="text-cyan-200">Career AI</span>
      </h1>

      <p
        class="text-sm md:text-base lg:text-lg text-white/90 max-w-2xl leading-relaxed hero-item item-delay-3"
      >
        Ikuti tes penilaian karier kami yang komprehensif dan dapatkan rekomendasi pribadi yang disesuaikan dengan keterampilan, minat, dan tujuanmu.
      </p>

      <div class="flex flex-col sm:flex-row gap-3 md:gap-4 mt-2 md:mt-4 hero-item item-delay-4">
        <button
          @click="scrollToCareerCards"
          class="px-6 md:px-8 py-2.5 md:py-3 rounded-full font-semibold shadow-md hover:text-white bg-white text-[#00B8D9] hover:bg-cyan-400 transition-all duration-300 text-base md:text-lg"
        >
          Mulai Tes Gratis
        </button>
      </div>

      <div
        class="flex items-center justify-center gap-4 md:gap-6 text-xs md:text-sm text-white/80 mt-3 md:mt-6 hero-item item-delay-5"
      >
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
  if (target) target.scrollIntoView({ behavior: "smooth" });
}
</script>

<style scoped>
/* SLIDE UP ANIMATION */
.hero-item {
  opacity: 0;
  transform: translateY(20px); /* Mulai dari bawah */
  animation: slide-up 0.6s ease-out forwards;
}

@keyframes slide-up {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0); /* Akhirnya di posisi normal */
  }
}

/* Stagger delay */
.item-delay-1 {
  animation-delay: 0.4s;
}
.item-delay-2 {
  animation-delay: 0.5s;
}
.item-delay-3 {
  animation-delay: 0.6s;
}
.item-delay-4 {
  animation-delay: 0.7s;
}
.item-delay-5 {
  animation-delay: 0.8s;
}
</style>

