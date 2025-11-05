<template>
  <div class="app-container">
    <!-- 🔵 Background bola-bola -->
    <div class="bubble-background"></div>

    <!-- 📦 Isi Halaman -->
    <NavBar />
    <HeaderSection />
    <ExplorePath />
    <HowItWorks />
    <CareerCard />
    <FooterSection />
  </div>
</template>

<script setup>
import NavBar from '../components/NavBar.vue'
import CareerCard from '../components/CareerCard.vue'
import HeaderSection from '../components/HeaderSection.vue'
import FooterSection from '../components/FooterSection.vue'
import HowItWorks from '../components/HowItWorks.vue'
import ExplorePath from '../components/ExplorePath.vue'
</script>
