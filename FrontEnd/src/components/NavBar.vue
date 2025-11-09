<template>
  <div class="fixed top-0 left-0 w-full z-50 flex justify-center pt-4 px-4">
    <nav
      :class="[ 
        'transition-all duration-1000 ease-in-out flex items-center justify-between w-full shadow-md px-6 py-6 md:px-10 md:py-7',
        'backdrop-blur-md text-cyan-500',
        isScrolled
          ? 'bg-white/95 shadow-lg rounded-3xl scale-100 max-w-3xl'
          : 'bg-white/40 shadow-md rounded-3xl max-w-6xl backdrop-blur-2xl text-white'
      ]"
    >
      <!-- Logo -->
      <router-link
        to="/career"
        class="text-2xl font-bold hover:text-cyan-400 transition-colors flex items-center"
      >
        <img :src="iconImg" alt="logo" width="90" />
      </router-link>

      <!-- Tombol hamburger (mobile) -->
      <button @click="toggleMenu" class="md:hidden focus:outline-none">
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

      <!-- Menu desktop -->
      <ul class="hidden md:flex space-x-8 font-medium">
        <li>
          <a
            href="/career"
            class="border border-transparent text-current px-4 py-2 rounded-3xl transition-all duration-300 hover:text-white hover:bg-cyan-400 hover:border-cyan-400 hover:scale-105"
          >
            Home
          </a>
        </li>
        <li>
          <a
            href="/about"
            class="border border-transparent text-current px-4 py-2 rounded-3xl transition-all duration-300 hover:text-white hover:bg-cyan-400 hover:border-cyan-400 hover:scale-105"
          >
            About
          </a>
        </li>
        <li>
          <a
            href="/career/#career"
            class="border border-transparent text-current px-4 py-2 rounded-3xl transition-all duration-300 hover:text-white hover:bg-cyan-400 hover:border-cyan-400 hover:scale-105"
          >
            Career Path
          </a>
        </li>
        <li>
          <a
            href="/contact"
            class="border border-transparent text-current px-4 py-2 rounded-3xl transition-all duration-300 hover:text-white hover:bg-cyan-400 hover:border-cyan-400 hover:scale-105"
          >
            Contact
          </a>
        </li>
      </ul>
    </nav>

    <!-- Mobile dropdown -->
    <transition name="fade">
      <ul
        v-if="isOpen"
        class="absolute top-full left-0 right-0 mt-3 mx-4 bg-white/95 backdrop-blur-md rounded-2xl shadow-md flex flex-col items-center space-y-4 py-5 px-4 text-cyan-600 md:hidden"
      >
        <li><a @click="closeMenu" href="/career" class="hover:text-cyan-400 transition">Home</a></li>
        <li><a @click="closeMenu" href="/about" class="hover:text-cyan-400 transition">About</a></li>
        <li>
          <a @click="closeMenu" href="/career/#career" class="hover:text-cyan-400 transition">
            Career Path
          </a>
        </li>
        <li><a @click="closeMenu" href="/contact" class="hover:text-cyan-400 transition">Contact</a></li>
      </ul>
    </transition>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import iconImg from '../assets/icons/Icon.png'

const isOpen = ref(false)
const isScrolled = ref(false)

const toggleMenu = () => (isOpen.value = !isOpen.value)
const closeMenu = () => (isOpen.value = false)

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})
onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
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
