<template>
  <section 
    id="about" 
    class="relative h-screen bg-gradient-to-br from-cyan-50 via-blue-50 to-purple-50 flex flex-col justify-center items-center text-center px-6 md:px-20 overflow-hidden"
  >
    <!-- Absolute Bright Cyan Background Circles -->
    <div class="absolute inset-0 pointer-events-none z-0">
      <!-- Large gradient circle top-left (BLUR) -->
      <div class="absolute -top-48 -left-48 w-[600px] h-[600px] bg-gradient-to-br from-cyan-300 to-blue-400 rounded-full opacity-40 blur-3xl"></div>
      
      <!-- Extra large circle top-right (NO BLUR) -->
      <div class="absolute -top-32 -right-40 w-[500px] h-[500px] bg-cyan-400 rounded-full opacity-25"></div>
      
      <!-- Medium circle middle-left (BLUR) -->
      <div class="absolute top-1/4 -left-32 w-96 h-96 bg-gradient-to-tr from-teal-300 to-cyan-300 rounded-full opacity-45 blur-2xl"></div>
      
      <!-- Large vibrant circle center-right (NO BLUR) -->
      <div class="absolute top-1/3 right-10 w-[450px] h-[450px] bg-gradient-to-bl from-pink-300 to-purple-300 rounded-full opacity-20"></div>
      
      <!-- Extra large gradient circle bottom-right (BLUR) -->
      <div class="absolute -bottom-56 -right-56 w-[700px] h-[700px] bg-gradient-to-tl from-cyan-300 via-blue-300 to-purple-300 rounded-full opacity-35 blur-3xl"></div>
      
      <!-- Medium circle bottom-left (NO BLUR) -->
      <div class="absolute bottom-20 left-1/4 w-80 h-80 bg-teal-300 rounded-full opacity-30"></div>
      
      <!-- Small accent circle (BLUR) -->
      <div class="absolute top-2/3 left-1/2 w-64 h-64 bg-gradient-to-r from-cyan-200 to-blue-300 rounded-full opacity-40 blur-xl"></div>
      
      <!-- Medium solid circle center (NO BLUR) -->
      <div class="absolute top-1/2 left-1/3 w-72 h-72 bg-cyan-300 rounded-full opacity-20"></div>
    </div>

    <!-- Dark Overlay untuk gelapin background -->
    <div class="absolute inset-0 bg-black/10 pointer-events-none z-0"></div>

    <!-- Glassmorphism Overlay -->
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(6,182,212,0.1),transparent_50%)] pointer-events-none z-0"></div>

    <!-- Content -->
    <div class="relative z-10 max-w-6xl border-2 rounded-3xl bg-white/70 p-10 md:p-12 border-cyan-200/60 backdrop-blur-md shadow-xl animate-fadeIn">
      <div class="flex items-center justify-center gap-6 mb-8 flex-wrap">
        <h2 class="text-4xl md:text-5xl font-bold text-gray-800">Tentang</h2>
        <img :src="iconAbout" alt="Icon" class="object-contain" width="150px"/>
      </div>

      <p class="text-xl md:text-2xl leading-relaxed text-gray-700">
        <strong class="text-cyan-600">CareerAI</strong> adalah sistem berbasis kecerdasan buatan (AI) 
        yang dirancang untuk membantu kamu memahami potensi dan arah kariermu. 
        Dengan mengisi form sederhana, sistem kami akan menganalisis preferensi, 
        minat, dan bakatmu untuk memberikan rekomendasi karier yang paling sesuai 
        dengan kepribadian dan tujuan hidupmu.
      </p>
    </div>
  </section>
</template>

<script setup>
import iconAbout from '../assets/icons/Icon.png'
</script>

<style scoped>
@keyframes fadeIn {
  from { 
    opacity: 0; 
    transform: translateY(30px); 
  }
  to { 
    opacity: 1; 
    transform: translateY(0); 
  }
}

.animate-fadeIn {
  animation: fadeIn 0.8s ease-out;
}
</style>
