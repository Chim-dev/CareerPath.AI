<template>
  <section class="py-24">

    <!-- konten -->
    <div class="relative max-w-6xl mx-auto px-6 grid md:grid-cols-2 gap-16 items-center z-10">
      <div
        v-for="(item, index) in galleryItems"
        :key="index"
        class="flex flex-col items-center text-center space-y-6 p-6 rounded-3xl bg-white/60 backdrop-blur-md shadow-xl hover:shadow-2xl transition-all duration-300"
      >
        <img
          :src="item.image"
          :alt="item.titles"
          class="w-72 h-72 object-contain drop-shadow-lg"
        />
        <h2 class="text-2xl font-semibold text-[#00B8D9]">
          {{ item.titles }}
        </h2>
        <p class="text-zinc-500 leading-relaxed max-w-md">
          {{ item.paragraph }}
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";

const galleryItems = ref([
  {
    titles: "Ketahui bakat dan bidang minatmu dengan AI",
    paragraph:
      "Tes kami menawarkan wawasan mendalam dan personal, membantu Anda menyusun karir masa depan.",
    image: "/src/assets/gallery-asset.png",
  },
  {
    titles: "Temukan karir masa depanmu dengan mengikuti tes kami",
    paragraph:
      "Dapatkan wawasan dan bantu diri Anda membangun fokus dalam menentukan arah karir.",
    image: "/src/assets/gallery-asset-2.png",
  },
]);
</script>
