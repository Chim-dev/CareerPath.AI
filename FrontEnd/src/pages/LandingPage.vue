<template>
  <div>
    <HeroSection @get-started="goToCareer" />
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import HeroSection from '../components/HeroSection.vue'

const router = useRouter()
const goToCareer = () => router.push('/career')
</script>
