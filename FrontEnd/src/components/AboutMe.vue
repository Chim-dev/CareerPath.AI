<template>
  <section
    id="about"
    class="relative w-full xl:py-30 2xl:py-40 py-20 px-6 md:px-16 bg-white overflow-hidden"
  >
    <!-- Background gradient halus -->
    <div
      class="absolute inset-0 bg-[radial-gradient(circle_at_20%_20%,rgba(0,200,255,0.07),transparent_70%)]"
    ></div>

    <!-- Grid: baru 2 kolom di lg -->
    <div
      class="max-w-7xl mx-auto grid lg:grid-cols-2 gap-16 lg:gap-20 items-center relative z-10"
    >
      <!-- TEXT -->
      <div
        class="opacity-0 translate-x-10 animation-fade-left px-10 pt-4 md:p-10 lg:p-14 sm:px-20"
        style="animation-delay: 0.5s"
      >
        <h1
          class="text-5xl md:text-6xl font-semibold tracking-tight text-gray-900 mb-8"
        >
          Muhammad Abdurrachim
        </h1>
        <h2
          class="text-md md:text-xl font-semibold tracking-tight text-gray-900 mb-8"
        >
          11231048 - INFORMATIKA - ITK
        </h2>

        <p class="text-gray-700 text-lg leading-[1.8] mb-6">
          <strong class="text-cyan-600">Me</strong> Lorem, ipsum dolor sit amet
          consectetur adipisicing elit. Odio, aut necessitatibus illo deleniti
          quibusdam commodi est amet quia cum facilis deserunt, optio incidunt
          atque ipsum officia beatae? Aliquam, voluptate sunt!
        </p>

        <p class="text-gray-700 text-lg leading-[1.8] mb-10">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eum esse
          asperiores enim dolorem placeat nisi vero, quaerat eligendi odio
          possimus maiores quasi odit distinctio ullam? Iste nobis nostrum non
          ea.
        </p>
      </div>
      
      <!-- IMAGE -->
      <div
        class="opacity-0 translate-y-10 animation-fade-up hidden lg:block"
        style="animation-delay: 0.2s"
      >
        <img
          :src="aboutImg"
          alt="About Image"
          class="rounded-3xl shadow-[0_20px_40px_rgba(0,0,0,0.06)] object-cover w-full h-[420px] md:h-[520px]"
        />
      </div>
    </div>

    <!-- br -->
     <div class="py-20 mt-10">
        <h2 class="text-gray-800 text-6xl flex items-center justify-center">Skills</h2>
     </div>
    <!-- cards -->
    <div  class="relative max-w-6xl mx-auto px-6 grid md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-3 gap-16 items-center z-10" data-aos="fade-up" data-aos-delay="500">
      <div
        v-for="(item, index) in galleryItems"
        :key="index"
        class="flex flex-col items-center text-center space-y-6 p-6 rounded-3xl"
      >
        <img
          :src="item.image"
          :alt="item.titles"
          class="w-72 h-72 object-contain drop-shadow-lg hover:scale-110 transition-all"
        />
        <h2 class="text-2xl font-semibold text-[#00B8D9]">
          {{ item.titles }}
        </h2>
        <p class="text-zinc-800 leading-relaxed max-w-md">
          {{ item.paragraph }}
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";
import aboutImg from "../assets/about-img (1).jpg";
import gallery1 from "@/assets/gallery-asset.jpg";
import gallery2 from "@/assets/gallery-asset-2.jpg";
import gallery3 from "@/assets/icons/comp-sci-asset.png";

const galleryItems = ref([
  {
    titles: "FullStack Web Developer",
    paragraph:
      "Proficient in Vue Vite and NextJs",
    image: gallery1,
  },
  {
    titles: "UI/UX",
    paragraph:
      "Proficient in Figma to create responsive and modern website user interface",
    image: gallery2,
  },
  {
    titles: "Game Designer",
    paragraph:
      "Design or drawing assets for Game Developer",
    image: gallery3,
  },
]);
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
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Utility Classes */
.animation-fade-up {
  animation: fadeUp 0.5s ease-out forwards;
}

.animation-fade-left {
  animation: fadeLeft 0.6s ease-out forwards;
}
</style>
