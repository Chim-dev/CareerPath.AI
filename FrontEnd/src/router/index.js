import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../pages/LandingPage.vue'
import CareerPathPage from '../pages/MainPage.vue'
import AboutPage from '../pages/AboutPage.vue'
import ContactPage from '../pages/ContactPage.vue'
import TestPage from '../pages/TestPage.vue'
import FaqsPage from '../pages/FaqsPage.vue'
import ResultPage from '../pages/ResultPage.vue'

const routes = [
  { path: '/', name: 'Landing', component: LandingPage },
  { path: '/career', name: 'Career', component: CareerPathPage },
  { path: '/about', name: 'About', component: AboutPage},
  { path: '/contact', name: 'Contact', component: ContactPage},
  { path: '/test', name: 'Test', component: TestPage},
  { path: '/faqs', name: 'FAQ', component: FaqsPage},
  { path: '/result', name: 'Result', component: ResultPage}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
