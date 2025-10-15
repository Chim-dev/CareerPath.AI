<template>
  <section
    class="relative h-screen flex items-center justify-center bg-cover bg-center px-6 md:px-16"
    :style="{ backgroundImage: `url(${bgImage})` }"
  >
    <div
      class="relative z-10 flex flex-col md:flex-row items-center justify-between w-full max-w-5xl bg-white/70 backdrop-blur-md border border-white/30 rounded-2xl shadow-xl p-12 md:p-10 lg:p-16"
    >
      <!-- Teks -->
      <div
        class="flex-1 text-center md:text-left space-y-4 md:space-y-5 text-[#0D1B2A]"
      >
        <h1
          class="text-3xl md:text-4xl font-extrabold leading-snug text-zinc-600"
        >
          Temukan <span class="text-[#00B8D9]">Jalur Karier Impianmu</span>
        </h1>
        <p
          class="text-sm md:text-base text-zinc-500 leading-relaxed max-w-md mx-auto md:mx-0"
        >
          CareerAI membantu kamu mengenali potensi, minat, dan jalur karier
          terbaik dengan dukungan kecerdasan buatan. Mulailah perjalanan
          kariermu dengan panduan yang tepat!
        </p>
        <a
          @click="scrollToCareerCards"
          class="inline-block bg-[#00B8D9] text-white px-6 py-2.5 rounded-full font-semibold shadow-md hover:bg-white hover:text-[#00B8D9] transition-all duration-300"
        >
          Jelajahi Sekarang
        </a>
      </div>

      <!-- Gambar -->
      <div class="flex-1 flex justify-center mt-8 md:mt-0">
        <img
          :src="illustImage"
          alt="Career Illustration"
          class="w-56 sm:w-64 md:w-72 lg:w-80 rounded-2xl shadow-xl border border-white/40 object-contain"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import bgImage from "../assets/bg-asset-2.jpg";
import illustImage from "../assets/students-asset.jpg";

function scrollToCareerCards() {
  const target = document.querySelector("#career");
  if (target) {
    target.scrollIntoView({ behavior: "smooth", block: "start" });
  }
}
</script>

<style scoped></style>
