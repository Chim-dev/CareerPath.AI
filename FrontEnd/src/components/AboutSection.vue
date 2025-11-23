<template>
  <section id="about" class="relative w-full py-45 px-6 md:px-20 bg-white overflow-hidden">
    <!-- Background subtle gradient -->
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_20%_20%,rgba(0,200,255,0.08),transparent_70%)]"></div>

    <div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-20 items-center relative z-10">

      <!-- IMAGE -->
      <div class="opacity-0 translate-y-10 animation-fade-up" style="animation-delay: 0.2s">
        <img :src="aboutImg" alt="About Image"
          class="rounded-3xl shadow-[0_20px_40px_rgba(0,0,0,0.06)] object-cover w-full h-[420px] md:h-[520px]" />
      </div>

      <!-- TEXT -->
      <div class="opacity-0 translate-x-10 animation-fade-left p-14" style="animation-delay: 0.5s">
        <h2 class="text-5xl md:text-6xl font-semibold tracking-tight text-gray-900 mb-8">
          About Us
        </h2>

        <p class="text-gray-700 text-lg leading-[1.8] mb-6">
          <strong class="text-cyan-600">CareerAI</strong> Dirancang untuk membantu individu menemukan jalur karier ideal
          mereka melalui analisis kepribadian dan minat yang cerdas. Kami berfokus membangun sistem modern dan andal
          yang didukung AI untuk memandu pengguna menuju pilihan yang bermakna.
        </p>

        <p class="text-gray-700 text-lg leading-[1.8] mb-10">
          Terinspirasi oleh desain pengalaman terbaik, pendekatan kami menggunakan antarmuka yang bersih dan intuitif,
          serta mudah dinavigasi untuk memastikan pengalaman pengguna yang optimal.
        </p>

        <!-- Clean Apple-like Social Icons -->
        <div class="flex gap-7 items-center">
          <i class="lab la-facebook-f text-3xl text-gray-800 hover:text-black transition"></i>
          <i class="lab la-twitter text-3xl text-gray-800 hover:text-black transition"></i>
          <i class="lab la-instagram text-3xl text-gray-800 hover:text-black transition"></i>
          <i class="lab la-linkedin-in text-3xl text-gray-800 hover:text-black transition"></i>
        </div>
      </div>

    </div>
  </section>
</template>

<script setup>
import aboutImg from "../assets/about-img (1).jpg";
</script>

<style scoped>
/* Fade Up Animation */
@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(35px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Fade Left Animation */
@keyframes fadeLeft {
  from {
    opacity: 0;
    transform: translateX(40px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Utility Classes */
.animation-fade-up {
  animation: fadeUp 1s ease-out forwards;
}

.animation-fade-left {
  animation: fadeLeft 1s ease-out forwards;
}
</style>