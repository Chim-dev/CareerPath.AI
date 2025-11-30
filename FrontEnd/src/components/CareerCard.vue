<template>
  <section class="py-24 bg-[#FDFDF9]" id="career">
    <div class="text-center mb-16">
      <h2 class="text-4xl font-bold mb-4 text-[#00B8D9]">Temukan Jalur Kariermu</h2>
      <p class="text-zinc-500 max-w-2xl mx-auto">
        Ketahui bidang karier yang cocok dengan minat dan potensimu. Mulailah perjalananmu hari ini.
      </p>
    </div>

    <!-- Ubah jadi grid -->
    <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 md:p-20 xl:p-2 xl:grid-cols-3 gap-10" data-aos="fade-up" data-aos-delay="600" data-aos-duration="500">
      <div v-for="(category, index) in careerCategories" :key="index"
        class="bg-[#FAFAF9] rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-500 p-10 flex flex-col items-center text-center">
        <img :src="category.animation" :alt="category.name" class="w-56 h-56 object-contain mb-6" />

        <h3 class="text-2xl font-semibold text-[#00B8D9] mb-4">
          {{ category.name }}
        </h3>

        <p class="text-zinc-500 mb-8">
          {{ category.intro }}
        </p>

        <button @click="goToTest(category.name)"
          class="px-6 py-3 bg-[#00B8D9] text-white rounded-lg hover:bg-white hover:text-[#00B8D9] border border-[#00B8D9] transition-all duration-300 font-medium">
          Mulai Tes
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router'
import compScience from '../assets/Icons/comp-sci-asset.png'
import dataBusiness from '../assets/Icons/data-asset.png'
import artsDesign from '../assets/Icons/arts-asset.png'
const router = useRouter()

const goToTest = (category) => {
  router.push({
    name: 'Test',
    query: { category }
  })
}

const careerCategories = [
  {
    name: 'Computer Science',
    intro: 'Jelajahi dunia teknologi dan inovasi. Bangun solusi digital untuk masa depan bersama Career.AI',
    animation: compScience,
  },
  {
    name: 'Arts & Design',
    intro: 'Kembangkan kreativitasmu dalam dunia desain dan seni visual yang inspiratif',
    animation: artsDesign,
  },
  {
    name: 'Business & Data',
    intro: 'Pelajari strategi bisnis modern dan analisis data untuk mengambil keputusan yang cerdas',
    animation: dataBusiness,
  },
]
</script>
