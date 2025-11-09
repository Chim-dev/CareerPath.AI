<template>
  <footer class="bg-white border-t border-gray-200 py-12 text-gray-600">
    <div class="max-w-7xl mx-auto px-6 md:px-12">
      <div class="grid md:grid-cols-4 gap-8 mb-8">
        <div class="col-span-1 flex flex-col items-start">
          <div class="flex items-center space-x-2 mb-3">
            <img :src="logoIcon" alt="Career.AI Logo" class="w-10 h-10" />
            <h2 class="text-xl font-semibold text-[#00B8D9]">Career.AI</h2>
          </div>
          <p class="text-sm leading-relaxed">
            Tes karier berbasis AI untuk membantu mahasiswa dan profesional
            menemukan jalur karier terbaik sesuai potensi dan minat mereka.
          </p>
        </div>

        <div>
          <h3 class="font-semibold text-gray-800 mb-3">Explore</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="/" class="hover:text-[#00B8D9] transition">Home</a></li>
            <li><a href="/about" class="hover:text-[#00B8D9] transition">About Us</a></li>
            <li><a href="/career" class="hover:text-[#00B8D9] transition">Career Path</a></li>
            <li><a href="#contact" class="hover:text-[#00B8D9] transition">Contact</a></li>
          </ul>
        </div>

        <div>
          <h3 class="font-semibold text-gray-800 mb-3">Support</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="/faqs" class="hover:text-[#00B8D9] transition">FAQs</a></li>
          </ul>
        </div>

      </div>

      <!-- Garis Pemisah -->
      <hr class="my-6 border-gray-200" />

      <div class="flex flex-col items-center text-center text-sm text-gray-500 space-y-3">
        <div class="max-w-3xl">
          <p class="inline">
            Disclaimer: Career.AI tidak memberikan hasil profesional atau diagnosis pasti.
            Tes ini bertujuan sebagai panduan awal pengembangan karier.
          </p>
          <span v-if="!showMore">
            <button
              @click="showMore = true"
              class="text-[#00B8D9] hover:underline focus:outline-none ml-1"
            >
              read more
            </button>
          </span>
          <span v-else>
            <span class="inline">
              Career.AI dikembangkan untuk memberikan rekomendasi karier berdasarkan algoritma
              pembelajaran mesin yang menganalisis jawaban pengguna. Hasil tes bersifat
              indikatif dan bukan penilaian profesional.
              Keputusan akhir mengenai karier tetap menjadi tanggung jawab pribadi pengguna.
              Career.AI tidak bertanggung jawab atas keputusan yang diambil berdasarkan hasil tes,
              serta tidak menyimpan informasi pribadi pengguna tanpa izin eksplisit. Semua data
              yang digunakan akan dianonimkan untuk keperluan analisis dan pengembangan sistem.
            </span>
            <button
              @click="showMore = false"
              class="text-[#00B8D9] hover:underline focus:outline-none ml-1"
            >
              show less
            </button>
          </span>
        </div>

        <div class="flex space-x-4">
          <a
            href="https://github.com/Chim-dev"
            target="_blank"
            class="text-gray-400 hover:text-[#00B8D9] transition"
            aria-label="GitHub"
          >
            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-6 h-6" viewBox="0 0 24 24">
              <path
                fill-rule="evenodd"
                d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.438 9.8 8.205 11.385.6.112.82-.26.82-.577v-2.17c-3.338.726-4.042-1.61-4.042-1.61-.546-1.384-1.333-1.752-1.333-1.752-1.089-.745.083-.729.083-.729 1.205.084 1.84 1.237 1.84 1.237 1.07 1.834 2.807 1.304 3.492.997.108-.775.42-1.305.763-1.605-2.665-.305-5.466-1.334-5.466-5.933 0-1.31.468-2.382 1.236-3.222-.124-.303-.536-1.527.117-3.18 0 0 1.008-.322 3.3 1.23a11.49 11.49 0 0 1 3.003-.404 11.47 11.47 0 0 1 3.003.404c2.29-1.552 3.297-1.23 3.297-1.23.655 1.653.243 2.877.12 3.18.77.84 1.235 1.912 1.235 3.222 0 4.61-2.803 5.624-5.475 5.921.43.372.823 1.102.823 2.22v3.293c0 .32.217.694.825.576C20.565 21.8 24 17.31 24 12 24 5.37 18.63 0 12 0Z"
                clip-rule="evenodd"
              />
            </svg>
          </a>
        </div>

        <p>© 2025 <span class="text-[#00B8D9] font-semibold">CarteChia</span>. All rights reserved.</p>
        <p class="text-xs text-gray-400">v1.0.0</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue'
import logoIcon from '../assets/Icons/Icon.png'

const showMore = ref(false)
</script>