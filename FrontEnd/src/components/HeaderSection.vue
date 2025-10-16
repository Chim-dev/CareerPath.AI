<template>
  <section
    class="relative h-screen flex items-center justify-center bg-cover bg-center px-6 md:px-16 bg-fixed"
    :style="{ backgroundImage: `url(${bgImage})` }"
  >
    <div
      class="relative z-10 flex flex-col md:flex-row items-center justify-between w-full max-w-7xl bg-white/70 backdrop-blur-md border border-white/30 rounded-3xl shadow-2xl p-10 md:p-16 lg:p-20"
    >
      <!-- Teks -->
      <div
        class="flex-1 text-center md:text-left space-y-6 text-[#0D1B2A]"
      >
        <h1
          class="text-4xl md:text-5xl font-extrabold leading-snug text-zinc-700"
        >
          Temukan <span class="text-[#00B8D9]">Jalur Karier Impianmu</span>
        </h1>
        <p
          class="text-base md:text-lg text-zinc-600 leading-relaxed max-w-lg mx-auto md:mx-0"
        >
          CareerAI membantu kamu mengenali potensi, minat, dan jalur karier
          terbaik dengan dukungan kecerdasan buatan. Mulailah perjalanan
          kariermu dengan panduan yang tepat!
        </p>
        <a
          @click="scrollToCareerCards"
          class="inline-block bg-[#00B8D9] text-white px-8 py-3 rounded-full font-semibold shadow-md hover:bg-white hover:text-[#00B8D9] transition-all duration-300 text-lg"
        >
          Jelajahi Sekarang
        </a>
      </div>

      <!-- Gambar -->
      <div class="flex-1 flex justify-center mt-10 md:mt-0">
        <div class="overflow-hidden rounded-3xl">
          <img
            :src="illustImage"
            alt="Career Illustration"
            class="w-72 sm:w-80 md:w-96 lg:w-[30rem] rounded-3xl shadow-2xl border border-white/40 object-contain hover:scale-125 duration-200 transition-all"
          />
        </div>
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
