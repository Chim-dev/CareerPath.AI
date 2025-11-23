  <template>
    <section
      class="relative py-20 lg:pt-50 lg:py-10 w-full min-h-auto bg-gradient-to-br from-cyan-50 via-blue-50 to-purple-50 px-4 md:px-10 overflow-hidden"
    >
      <!-- Soft Gradient Background Shapes -->
      <div class="absolute inset-0 pointer-events-none z-0">
        <div class="absolute -top-40 -left-40 w-[450px] h-[450px] bg-gradient-to-br from-cyan-300 to-blue-400 rounded-full opacity-30 blur-3xl"></div>
        <div class="absolute top-1/3 -right-20 w-[350px] h-[350px] bg-gradient-to-tr from-purple-300 to-pink-300 rounded-full opacity-25 blur-2xl"></div>
        <div class="absolute bottom-10 left-1/3 w-[300px] h-[300px] bg-gradient-to-bl from-blue-200 to-teal-200 rounded-full opacity-20 blur-2xl"></div>
      </div>

      <div class="relative z-10 max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-16 items-start">
        <!-- CONTACT INFO -->
        <div class="space-y-6 px-4 md:px-0">
          <h2 class="text-4xl md:text-5xl font-bold text-gray-800">Contact Us</h2>
          <p class="text-gray-600 text-lg max-w-md">
            Anda Memiliki pertanyaan? <br />
            Jangan ragu untuk menghubungi kami melalui email.
          </p>

          <div class="space-y-5 pt-4">
            <div class="flex items-start gap-4">
              <span class="text-cyan-500 text-2xl">📧</span>
              <p class="text-gray-700">11231048@student.itk.ac.id</p>
            </div>
            <div class="flex items-start gap-4">
              <span class="text-cyan-500 text-2xl">📍</span>
              <p class="text-gray-700">
                Institute Technology of Kalimantan <br />
                Kalimantan Timur, Indonesia
              </p>
            </div>
            <div class="flex items-start gap-4">
              <span class="text-cyan-500 text-2xl">📞</span>
              <p class="text-gray-700"> Not Available </p>
            </div>
          </div>
        </div>

        <!-- FORM -->
        <div
          class="bg-white/80 backdrop-blur-xl border border-gray-200 shadow-xl rounded-3xl p-8 md:p-10 w-full"
        >
          <form @submit.prevent="sendEmail" class="space-y-5">

            <!-- Name Input -->
            <div>
              <label class="block font-medium text-gray-700 mb-1">Name</label>
              <input
                v-model="form.name"
                type="text"
                required
                placeholder="Enter your name"
                class="px-4 py-3 rounded-lg bg-white border border-gray-300 focus:ring-2 focus:ring-cyan-400 w-full text-gray-700"
              />
            </div>

            <!-- Email Input -->
            <div>
              <label class="block font-medium text-gray-700 mb-1">Email</label>
              <input
                v-model="form.email"
                type="email"
                required
                placeholder="Enter your email"
                class="px-4 py-3 rounded-lg bg-white border border-gray-300 focus:ring-2 focus:ring-cyan-400 w-full text-gray-700"
              />
            </div>

            <!-- Message -->
            <div>
              <label class="block font-medium text-gray-700 mb-1">Message</label>
              <textarea
                v-model="form.message"
                rows="5"
                required
                placeholder="Write your message"
                class="w-full px-4 py-3 bg-white border border-gray-300 rounded-lg focus:ring-2 focus:ring-cyan-400 text-gray-700"
              ></textarea>
            </div>

            <!-- Submit Button -->
            <button
              type="submit"
              :disabled="loading"
              class="w-full py-3 text-white font-semibold rounded-lg transition-all duration-300 disabled:opacity-70"
              :class="loading ? 'bg-gray-400' : 'bg-gradient-to-r from-cyan-500 to-purple-500 hover:opacity-90'"
            >
              {{ loading ? "Sending..." : "Submit" }}
            </button>
          </form>

          <!-- Success or Error Message -->
          <p
            v-if="successMessage"
            class="text-green-600 mt-4 text-center font-medium"
          >
            {{ successMessage }}
          </p>
          <p
            v-if="errorMessage"
            class="text-red-600 mt-4 text-center font-medium"
          >
            {{ errorMessage }}
          </p>
        </div>
      </div>
    </section>
  </template>

  <script setup>
  import { ref } from "vue";
  import emailjs from "emailjs-com";

  const form = ref({
    name: "",
    email: "",
    website: "",
    message: "",
  });

  const loading = ref(false);
  const successMessage = ref("");
  const errorMessage = ref("");

  const sendEmail = () => {
    loading.value = true;
    successMessage.value = "";
    errorMessage.value = "";

    emailjs
      .send(
        "service_xxxxxx", // your service ID
        "template_xxxxxx", // your template ID
        {
          from_name: form.value.name,
          from_email: form.value.email,
          website: form.value.website,
          message: form.value.message,
        },
        "public_xxxxxxxxx" // Public key
      )
      .then(() => {
        successMessage.value = "Your message has been sent successfully ✅";
        form.value = { name: "", email: "", website: "", message: "" };
      })
      .catch(() => {
        errorMessage.value = "Failed to send message. Please try again later ❌";
      })
      .finally(() => {
        loading.value = false;
      });
  };
  </script>

  <style scoped>
  @media (max-width: 768px) {
    section {
      padding-top: 6rem;
    }
  }
  </style>
