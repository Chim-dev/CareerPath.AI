<template>
  <div>

    <!-- 📦 Isi Halaman -->
    <NavBar />
    <HeaderSection />
    <AboutSection />
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
import AboutSection from '../components/AboutSection.vue'
</script>
