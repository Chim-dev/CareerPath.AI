<template>
  <section 
    id="about" 
    class="h-screen bg-no-repeat bg-cover bg-fixed bg-bottom flex flex-col justify-center items-center text-center px-6 md:px-20"
    :style="{ backgroundImage: `url(${bgImage})` }"
  >
    <div class="max-w-3xl border rounded-2xl bg-white/10 p-10 border-white/10 backdrop-blur-sm">
      <div class="flex items-center justify-center gap-6 mb-6">
        <h2 class="text-4xl font-bold text-zinc-200">Tentang</h2>
        <img :src="iconAbout" alt="Icon" class="object-contain" width="150px"/>
      </div>

      <p class="text-lg/loose text-zinc-200 leading-relaxed">
        <strong>CareerAI</strong> adalah sistem berbasis kecerdasan buatan (AI) 
        yang dirancang untuk membantu kamu memahami potensi dan arah kariermu. 
        Dengan mengisi form sederhana, sistem kami akan menganalisis preferensi, 
        minat, dan bakatmu untuk memberikan rekomendasi karier yang paling sesuai 
        dengan kepribadian dan tujuan hidupmu.
      </p>
    </div>
  </section>
</template>

<script setup>
import bgImage from '../assets/bg-asset-3.jpg'
import iconAbout from '../assets/icons/Icon.png'
</script>

<style scoped>
section {
  animation: fadeIn 0.6s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
