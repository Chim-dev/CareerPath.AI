<template>
    <section class="py-20 bg-white">
        <div class="max-w-6xl mx-auto px-6">
            <div class="flex flex-col md:flex-row items-center gap-8 p-6 md:p-10
               bg-cyan-50/40 backdrop-blur-sm 
               rounded-tr-lg rounded-bl-lg rounded-tl-[80px] rounded-br-[80px]">
                <div class="w-full md:w-1/2 flex justify-center">
                    <img :src="missionImage" alt="Our Mission" class="w-72 md:w-96 object-contain rounded-md" />
                </div>


                <div class="w-full md:w-1/2">
                    <h3 class="text-sm text-gray-500 font-semibold mb-2">Misi Kami</h3>
                    <h2 class="text-2xl md:text-3xl font-bold text-cyan-600 mb-4 leading-tight">
                        Membuka Wawasan Anda tentang Jenjang Karir Anda
                    </h2>
                    <p class="text-gray-700 leading-relaxed">
                        {{ fullText }}
                    </p>

                    <div class="mt-6">
                        <a @click="scrollToCareerCards"
                            class="inline-block bg-[#00B8D9] text-white px-8 py-3 rounded-full font-semibold shadow-md hover:bg-white hover:text-[#00B8D9] transition-all duration-300">
                            Jelajahi Sekarang
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
import missionImage from '../assets/Icons/mission-icon.png' 

const fullText = `Misi kami adalah membimbing individu dalam memahami pilihan karir serta rekomendasi jenjang karir mereka. Dengan memanfaatkan kecerdasan buatan, kami bertujuan untuk mengungkap bidang minat dan keahlian Anda.`
function scrollToCareerCards() {
  const target = document.querySelector('#career')
  if (target) {
    target.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }
}

</script>
<style scoped>
@supports (border-radius: 80px) {}


.container-fallback {
    border-radius: 16px;
}
</style>
