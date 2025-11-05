<template>
  <section
    class="relative min-h-screen bg-gradient-to-br from-cyan-50 via-blue-50 to-purple-50 flex items-center justify-center py-20 overflow-hidden"
  >
    <!-- Fixed Bright Cyan Background Circles -->
    <div class="fixed inset-0 pointer-events-none z-0">
      <!-- Large gradient circle top-left (BLUR) -->
      <div class="absolute -top-48 -left-48 w-[600px] h-[600px] bg-gradient-to-br from-cyan-300 to-blue-400 rounded-full opacity-40 blur-3xl"></div>
      
      <!-- Extra large circle top-right (NO BLUR) -->
      <div class="absolute -top-32 -right-40 w-[500px] h-[500px] bg-cyan-400 rounded-full opacity-25"></div>
      
      <!-- Medium circle middle-left (BLUR) -->
      <div class="absolute top-1/4 -left-32 w-96 h-96 bg-gradient-to-tr from-teal-300 to-cyan-300 rounded-full opacity-45 blur-2xl"></div>
      
      <!-- Large vibrant circle center-right (NO BLUR) -->
      <div class="absolute top-1/3 right-10 w-[450px] h-[450px] bg-gradient-to-bl from-pink-300 to-purple-300 rounded-full opacity-20"></div>
      
      <!-- Extra large gradient circle bottom-right (BLUR) -->
      <div class="absolute -bottom-56 -right-56 w-[700px] h-[700px] bg-gradient-to-tl from-cyan-300 via-blue-300 to-purple-300 rounded-full opacity-35 blur-3xl"></div>
      
      <!-- Medium circle bottom-left (NO BLUR) -->
      <div class="absolute bottom-20 left-1/4 w-80 h-80 bg-teal-300 rounded-full opacity-30"></div>
      
      <!-- Small accent circle (BLUR) -->
      <div class="absolute top-2/3 left-1/2 w-64 h-64 bg-gradient-to-r from-cyan-200 to-blue-300 rounded-full opacity-40 blur-xl"></div>
      
      <!-- Medium solid circle center (NO BLUR) -->
      <div class="absolute top-1/2 left-1/3 w-72 h-72 bg-cyan-300 rounded-full opacity-20"></div>
    </div>

    <!-- Glassmorphism Overlay -->
    <div class="fixed inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(6,182,212,0.1),transparent_50%)] pointer-events-none z-0"></div>

    <!-- Contact Form Content -->
    <div class="relative z-10 w-full max-w-2xl bg-white/70 backdrop-blur-md rounded-3xl shadow-xl p-8 md:p-10 border-2 border-cyan-200/60 mx-4">
      <h2 class="text-3xl md:text-4xl font-bold text-gray-800 mb-2 text-center">Get in Touch</h2>
      <p class="text-gray-600 text-center mb-8">
        Got a question, feedback, or collaboration idea? Drop me a message below 👇
      </p>

      <form @submit.prevent="sendEmail" class="space-y-5">
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Your Name</label>
          <input
            v-model="form.name"
            type="text"
            required
            placeholder="Enter your name"
            class="w-full px-4 py-3 bg-white/60 backdrop-blur-sm text-gray-800 placeholder-gray-400 border border-cyan-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-cyan-400 focus:border-transparent transition"
          />
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Your Email</label>
          <input
            v-model="form.email"
            type="email"
            required
            placeholder="Enter your email"
            class="w-full px-4 py-3 bg-white/60 backdrop-blur-sm text-gray-800 placeholder-gray-400 border border-cyan-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-cyan-400 focus:border-transparent transition"
          />
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Message</label>
          <textarea
            v-model="form.message"
            rows="5"
            required
            placeholder="Type your message here..."
            class="w-full px-4 py-3 bg-white/60 backdrop-blur-sm text-gray-800 placeholder-gray-400 border border-cyan-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-cyan-400 focus:border-transparent transition resize-none"
          ></textarea>
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full bg-gradient-to-r from-cyan-400 to-blue-500 text-white py-3 rounded-xl font-semibold hover:from-cyan-500 hover:to-blue-600 shadow-lg hover:shadow-xl transition-all duration-300 disabled:opacity-70 disabled:cursor-not-allowed"
        >
          {{ loading ? "Sending..." : "Send Message" }}
        </button>
      </form>

      <p v-if="successMessage" class="text-green-600 mt-4 text-center font-medium">
        {{ successMessage }}
      </p>
      <p v-if="errorMessage" class="text-red-600 mt-4 text-center font-medium">
        {{ errorMessage }}
      </p>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue"
import emailjs from "emailjs-com"

// form data
const form = ref({
  name: "",
  email: "",
  message: "",
})

const loading = ref(false)
const successMessage = ref("")
const errorMessage = ref("")

// kirim email via EmailJS
const sendEmail = () => {
  loading.value = true
  successMessage.value = ""
  errorMessage.value = ""

  emailjs
    .send(
      "service_xxxxxx", // <-- ganti dengan Service ID kamu dari EmailJS
      "template_xxxxxx", // <-- ganti dengan Template ID kamu
      {
        from_name: form.value.name,
        from_email: form.value.email,
        message: form.value.message,
        to_email: "11231048@student.itk.ac.id", // email tujuan
      },
      "public_xxxxxxxxxx" // <-- ganti dengan Public Key kamu
    )
    .then(() => {
      successMessage.value = "Your message has been sent successfully ✅"
      form.value = { name: "", email: "", message: "" }
    })
    .catch(() => {
      errorMessage.value = "Failed to send message. Please try again later ❌"
    })
    .finally(() => {
      loading.value = false
    })
}
</script>
