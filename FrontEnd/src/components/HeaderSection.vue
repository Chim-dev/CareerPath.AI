<template>
  <section
    class="relative h-screen flex items-center justify-center bg-cover bg-center px-6 md:px-16"
    :style="{ backgroundImage: `url(${bgImage})` }"
  >

    <div
      class="relative z-10 flex flex-col md:flex-row items-center justify-between w-full max-w-6xl bg-white/70 backdrop-blur-md border border-white/30 rounded-3xl shadow-2xl p-8 md:p-12"
    >
      <div class="flex-1 text-center md:text-left space-y-6 text-[#0D1B2A]">
        <h1 class="text-4xl text-zinc-500 md:text-5xl font-extrabold leading-tight">
          Temukan <span class="text-[#00B8D9]">Jalur Karier Impianmu</span>
        </h1>
        <p class="text-base md:text-lg text-zinc-500 leading-relaxed">
          CareerAI membantu kamu mengenali potensi, minat, dan jalur karier terbaik
          dengan dukungan kecerdasan buatan. Mulailah perjalanan kariermu dengan panduan yang tepat!
        </p>
        <a
          @click="scrollToCareerCards"
          class="inline-block bg-[#00B8D9] text-white px-8 py-3 rounded-full font-semibold shadow-md hover:bg-white hover:text-[#00B8D9] transition-all duration-300"
        >
          Jelajahi Sekarang
        </a>
      </div>

      <div class="flex-1 flex justify-center mt-10 md:mt-0">
        <img
          :src="illustImage"
          alt="Career Illustration"
          class="w-72 md:w-[28rem] rounded-2xl shadow-xl border border-white/40"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import bgImage from '../assets/bg-asset-2.jpg'
import illustImage from '../assets/students-asset.jpg'

function scrollToCareerCards() {
  const target = document.querySelector('#career')
  if (target) {
    target.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }
}

</script>

<style scoped> 

</style>