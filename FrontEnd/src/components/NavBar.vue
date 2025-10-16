<template>
  <nav :class="[
    'fixed top-0 left-0 w-full z-50 transition-all duration-300 flex justify-between items-center px-2 py-2 md:px-6 md:py-2 shadow-md',
    isScrolled ? 'bg-white/95 backdrop-blur-sm shadow-md text-cyan-500' : 'bg-transparent text-white'
  ]">
    <router-link to="/career" class="text-2xl font-bold hover:text-cyan-400 transition-colors">
      <img :src="iconImg" alt="" width="90px">
    </router-link>


    <button @click="toggleMenu" class="md:hidden focus:outline-none">
      <svg v-if="!isOpen" xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24"
        stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
      </svg>
      <svg v-else xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24"
        stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
      </svg>
    </button>

    <ul class="hidden md:flex space-x-6">
      <li><a href="/career" class="border border-transparent text-current p-2 rounded-3xl transition-all duration-300 
         hover:text-white hover:bg-cyan-400 hover:border-cyan-400 hover:scale-105">Home</a></li>
      <li><a href="/about" class="border border-transparent text-current p-2 rounded-3xl transition-all duration-300 
         hover:text-white hover:bg-cyan-400 hover:border-cyan-400 hover:scale-105">About</a></li>
      <li><a href="/career/#career" class="border border-transparent text-current p-2 rounded-3xl transition-all duration-300 
         hover:text-white hover:bg-cyan-400 hover:border-cyan-400 hover:scale-105">Career Path</a></li>
      <li><a href="/contact" class="border border-transparent text-current p-2 rounded-3xl transition-all duration-300 
         hover:text-white hover:bg-cyan-400 hover:border-cyan-400 hover:scale-105">Contact</a></li>
    </ul>


    <transition name="fade">
      <ul v-if="isOpen"
        class="absolute top-full left-0 w-full bg-white/95 backdrop-blur-md shadow-md flex flex-col items-center space-y-4 py-4 md:hidden z-20">
        <li><a @click="closeMenu" href="/career" class="hover:underline text-cyan-600">Home</a></li>
        <li><a @click="closeMenu" href="/about" class="hover:underline text-cyan-600">About</a></li>
        <li><a @click="closeMenu" href="/career/#career" class="hover:underline text-cyan-600">Career Path</a></li>
        <li><a @click="closeMenu" href="/contact" class="hover:underline text-cyan-600">Contact</a></li>
      </ul>
    </transition>
  </nav>
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
