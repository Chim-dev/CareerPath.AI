<template>
  <section
    class="min-h-screen bg-cover flex items-center justify-center bg-gradient-to-br from-cyan-50 to-white py-20"
    :style="{ backgroundImage: `url(${contactBg})` }"
  >
    <div
      class="w-full max-w-2xl bg-white rounded-2xl shadow-lg p-8 md:p-10 border border-cyan-100"
    >
      <h2 class="text-3xl font-bold text-cyan-400 mb-2 text-center">Get in Touch</h2>
      <p class="text-gray-500 text-center mb-8">
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
            class="w-full px-4 py-3 bg-gray-50 text-gray-800 placeholder-gray-400 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-400"
          />
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Your Email</label>
          <input
            v-model="form.email"
            type="email"
            required
            placeholder="Enter your email"
            class="w-full px-4 py-3 bg-gray-50 text-gray-800 placeholder-gray-400 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-400"
          />
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Message</label>
          <textarea
            v-model="form.message"
            rows="5"
            required
            placeholder="Type your message here..."
            class="w-full px-4 py-3 bg-gray-50 text-gray-800 placeholder-gray-400 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-400"
          ></textarea>
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full bg-cyan-400 text-white py-3 rounded-lg font-semibold hover:bg-white hover:text-cyan-400 shadow-lg transition disabled:opacity-70"
        >
          {{ loading ? "Sending..." : "Send Message" }}
        </button>
      </form>

      <p v-if="successMessage" class="text-green-600 mt-4 text-center">
        {{ successMessage }}
      </p>
      <p v-if="errorMessage" class="text-red-600 mt-4 text-center">
        {{ errorMessage }}
      </p>
    </div>
  </section>
</template>


<script setup>
import { ref } from "vue"
import emailjs from "emailjs-com"
import contactBg from '../assets/bg-asset-2.jpg'

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
