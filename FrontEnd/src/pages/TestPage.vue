<script setup>
import { useRoute } from 'vue-router'
import TestQuestionSection from '../components/OnlineTesQuestion.vue'

const route = useRoute()
const selectedCategory = route.query.category || 'Tes'
</script>

<template>
  <main>
    <TestQuestionSection :category="selectedCategory" />
  </main>
</template>
