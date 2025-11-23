<template>
  <section class="relative overflow-hidden py-20 px-6 bg-[#FDFDF9]">

    <!-- Konten -->
    <div class="relative z-10 max-w-6xl mx-auto text-center">
      <h2 data-aos="fade-up" data-aos-delay="500" class="text-3xl md:text-5xl font-extrabold text-[#0D1B2A] mb-4">
        Jelajahi Berbagai Jalur Karier
      </h2>
      <p data-aos="fade-up" data-aos-delay="700" class="text-gray-600 max-w-2xl mx-auto mb-12">
        Tes kami mencakup berbagai bidang karier untuk membantu Anda menemukan jalur yang paling sesuai
        dengan bakat dan aspirasi Anda.
      </p>

      <div data-aos="fade-up" data-aos-delay="900" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="(career, index) in careers"
          :key="index"
          data-aos="fade-up"
          class="bg-[#FAFAF9] rounded-2xl border border-gray-200 shadow-sm hover:shadow-md hover:-translate-y-1 transition-all duration-300 p-8 text-left"
        >
          <div
            class="w-12 h-12 rounded-xl flex items-center justify-center mb-4"
            :class="career.bgColor"
            data-aos="fade-up"
          >
            <component :is="career.icon" class="w-6 h-6" :class="career.iconColor" />
          </div>
          <h3 class="text-lg font-semibold text-[#0D1B2A] mb-2">{{ career.title }}</h3>
          <p class="text-gray-600 text-sm leading-relaxed">{{ career.desc }}</p>
        </div>
      </div>
    </div>

    <GallerySection />
  </section>
</template>

<script setup>
import { Briefcase, Code2, Heart, Palette, LineChart, Users } from "lucide-vue-next";
import GallerySection from "./GallerySection.vue";

const careers = [
  {
    title: "Teknologi",
    desc: "Pengembangan perangkat lunak, data science, keamanan siber, dan karier di bidang IT.",
    icon: Code2,
    iconColor: "text-[#00B8D9]",
    bgColor: "bg-[#00B8D9]/10",
  },
  {
    title: "Bisnis",
    desc: "Manajemen, keuangan, konsultasi, serta peluang di bidang kewirausahaan.",
    icon: Briefcase,
    iconColor: "text-[#00B8D9]",
    bgColor: "bg-[#00B8D9]/10",
  },
  {
    title: "Kreatif",
    desc: "Desain, pemasaran, pembuatan konten, dan profesi di bidang seni.",
    icon: Palette,
    iconColor: "text-[#00B8D9]",
    bgColor: "bg-[#00B8D9]/10",
  },
];
</script>

<style scoped>
@keyframes floaty {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
  100% { transform: translateY(0px); }
}
.animate-pulse {
  animation: floaty 8s ease-in-out infinite;
}
</style>
