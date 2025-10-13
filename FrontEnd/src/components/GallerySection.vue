<template>
  <section class="py-24 bg-gradient-to-b from-blue-50 to-white">
    <div class="max-w-6xl mx-auto px-6 grid md:grid-cols-2 gap-10 items-center">
      <div 
        v-for="(item, index) in galleryItems" 
        :key="index" 
        class="flex flex-col items-center text-center space-y-4"
      >
        <img 
          :src="item.image" 
          :alt="item.titles" 
          class="w-72 h-72 object-contain"
        />
        <h2 class="text-2xl font-semibold text-cyan-400">{{ item.titles }}</h2>
        <p class="text-zinc-400">{{ item.paragraph }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue"

const galleryItems = ref([
  {
    titles: "Ketahui bakat dan bidang minatmu dengan AI",
    paragraph: "Tes kami menawarkan wawasan mendalam dan personal, membantu Anda menyusun karir masa depan.",
    image: "/src/assets/gallery-asset.png"
  },
  {
    titles: "Temukan karir masa depanmu dengan mengikuti tes kami",
    paragraph: "Dapatkan wawasan dan bantu diri Anda membangun fokus dalam menentukan arah karir.",
    image: "/src/assets/gallery-asset-2.png"
  }
])
</script>
