<template>
  <div class="fixed top-0 left-0 w-full z-50 flex justify-center pt-1 px-4">
    <nav
      :class="[
        'transition-all duration-500 ease-in-out flex items-center justify-between w-full shadow-md px-6 py-6 md:px-10 md:py-4',
        isScrolled
          ? 'bg-[#FDFDF9] shadow-lg rounded-3xl scale-100 max-w-3xl text-cyan-500'
          : 'bg-[#FDFDF9] shadow-md rounded-3xl max-w-6xl',
        !isScrolled && isWhiteText ? 'text-cyan-500' : 'text-cyan-500'
      ]"
    >
      <!-- ======================= -->
      <!-- LOGO - Navigasi ke Home -->
      <!-- ======================= -->
      <router-link
        to="/career"
        class="text-2xl font-bold hover:text-cyan-400 transition-colors flex items-center"
      >
        <img :src="iconImg" alt="logo" width="90" />
      </router-link>

      <!-- ========================= -->
      <!-- HAMBURGER - Mobile Toggle -->
      <!-- ========================= -->
      <button @click="toggleMenu" class="md:hidden focus:outline-none">
        <!-- Icon Menu (3 garis) -->
        <svg
          v-if="!isOpen"
          xmlns="http://www.w3.org/2000/svg"
          class="w-7 h-7"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="2"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
        <!-- Icon Close (X) -->
        <svg
          v-else
          xmlns="http://www.w3.org/2000/svg"
          class="w-7 h-7"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="2"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <!-- ============== -->
      <!-- MENU - Desktop -->
      <!-- ============== -->
      <ul class="hidden md:flex space-x-8 font-medium">
        <li>
          <router-link to="/career" class="menu-link">Home</router-link>
        </li>
        <li>
          <router-link to="/about" class="menu-link">About</router-link>
        </li>
        <!-- 
          Career Path Link:
          - Menggunakan :to dengan computed property untuk dynamic routing
          - @click.prevent digunakan HANYA jika sudah di halaman yang punya #career
        -->
        <li>
          <router-link 
            :to="careerLinkTarget" 
            class="menu-link"
            @click="handleCareerClick"
          >
            Career Path
          </router-link>
        </li>
        <li>
          <router-link to="/contact" class="menu-link">Contact</router-link>
        </li>
      </ul>
    </nav>

    <!-- ============= -->
    <!-- MENU - Mobile -->
    <!-- ============= -->
    <transition name="fade">
      <ul
        v-if="isOpen"
        :class="[
          'absolute top-full left-0 right-0 mt-3 mx-4 backdrop-blur-md rounded-2xl shadow-md flex flex-col items-center space-y-4 py-5 px-4 md:hidden',
          isWhiteText ? 'bg-white text-cyan-500' : 'bg-white/95 text-cyan-600'
        ]"
      >
        <li>
          <router-link @click="closeMenu" to="/career" class="hover:text-cyan-400 transition">
            Home
          </router-link>
        </li>
        <li>
          <router-link @click="closeMenu" to="/about" class="hover:text-cyan-400 transition">
            About
          </router-link>
        </li>
        <!-- Career Path untuk Mobile -->
        <li>
          <router-link 
            :to="careerLinkTarget"
            @click="handleCareerClickMobile"
            class="hover:text-cyan-400 transition"
          >
            Career Path
          </router-link>
        </li>
        <li>
          <router-link @click="closeMenu" to="/contact" class="hover:text-cyan-400 transition">
            Contact
          </router-link>
        </li>
      </ul>
    </transition>
  </div>
</template>

<script setup>
/**
 * ============================================
 * NavBar.vue - Navigation Component
 * ============================================
 * 
 * Fitur:
 * - Responsive navbar (desktop & mobile)
 * - Scroll-aware styling (berubah saat scroll)
 * - Smart navigation ke #career section
 * 
 * Dependencies:
 * - vue-router untuk navigasi
 * - Tailwind CSS untuk styling
 */

import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import iconImg from '@/assets/icons/logo-icon.png'

// ==================
// ROUTER INSTANCES
// ==================
const route = useRoute()   // Untuk membaca current route
const router = useRouter() // Untuk navigasi programmatic

// ==================
// REACTIVE STATE
// ==================
const isOpen = ref(false)      // Toggle state untuk mobile menu
const isScrolled = ref(false)  // State untuk deteksi scroll

// ==================
// CONFIGURATION
// ==================

/**
 * Daftar halaman yang membutuhkan text putih
 * (untuk kontras dengan background gelap)
 */
const whiteTextRoutes = ['/career']

/**
 * Daftar halaman yang memiliki section #career
 * Digunakan untuk menentukan behavior navigasi Career Path
 */
const pagesWithCareer = ['/career', '/about']

// ==================
// COMPUTED PROPERTIES
// ==================

/**
 * Menentukan apakah text navbar harus putih
 * berdasarkan halaman saat ini
 */
const isWhiteText = computed(() => {
  return whiteTextRoutes.includes(route.path)
})

/**
 * Dynamic target untuk link Career Path
 * 
 * Logic:
 * - Jika sudah di halaman yang punya #career → return hash saja
 * - Jika di halaman lain (misal Contact) → return path + hash
 * 
 * @returns {Object} Vue Router location object
 */
const careerLinkTarget = computed(() => {
  const currentPath = route.path
  
  if (pagesWithCareer.includes(currentPath)) {
    // Sudah di halaman dengan #career, cukup scroll
    return { path: currentPath, hash: '#career' }
  }
  
  // Di halaman lain, navigasi ke /career dengan hash
  return { path: '/career', hash: '#career' }
})

// ==================
// METHODS
// ==================

/**
 * Toggle mobile menu open/close
 */
const toggleMenu = () => {
  isOpen.value = !isOpen.value
}

/**
 * Tutup mobile menu
 */
const closeMenu = () => {
  isOpen.value = false
}

/**
 * Handler untuk scroll event
 * Update isScrolled state berdasarkan posisi scroll
 */
const handleScroll = () => {
  isScrolled.value = window.scrollY > 50
}

/**
 * Handler click untuk Career Path link (Desktop)
 * 
 * Behavior:
 * - Jika sudah di halaman dengan #career: prevent default, scroll manual
 * - Jika di halaman lain: biarkan router-link handle navigasi
 * 
 * @param {Event} event - Click event
 */
function handleCareerClick(event) {
  const currentPath = route.path
  
  // Cek apakah halaman saat ini punya section #career
  if (pagesWithCareer.includes(currentPath)) {
    // Prevent router navigation, lakukan scroll manual
    event.preventDefault()
    scrollToCareerSection()
  }
  // Jika tidak, biarkan router-link navigate secara normal
  // scrollBehavior di router akan handle scroll setelah navigasi
}

/**
 * Handler click untuk Career Path link (Mobile)
 * Sama seperti desktop, tapi juga tutup menu
 * 
 * @param {Event} event - Click event
 */
function handleCareerClickMobile(event) {
  handleCareerClick(event)
  closeMenu()
}

/**
 * Scroll ke section #career dengan smooth animation
 * Includes offset untuk navbar fixed
 */
function scrollToCareerSection() {
  const careerElement = document.getElementById('career')
  
  if (careerElement) {
    // Gunakan scrollIntoView untuk smooth scroll
    careerElement.scrollIntoView({ 
      behavior: 'smooth',
      block: 'start'
    })
  } else {
    // Fallback: jika element tidak ditemukan, log warning
    console.warn('[NavBar] Element #career tidak ditemukan di halaman ini')
  }
}

// ==================
// LIFECYCLE HOOKS
// ==================

onMounted(() => {
  // Pasang scroll listener saat component mounted
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  // Bersihkan scroll listener saat component unmounted
  // Penting untuk mencegah memory leak
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
/* ==================
   MENU LINK STYLING
   ================== */
.menu-link {
  border: 1px solid transparent;
  padding: 0.5rem 1rem;
  border-radius: 1.5rem;
  transition: all 0.3s ease;
}

.menu-link:hover {
  color: white;
  background: #22d3ee;
  border-color: #22d3ee;
  transform: scale(1.05);
}

/* ==================
   MOBILE MENU TRANSITION
   ================== */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s ease, transform 0.4s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
