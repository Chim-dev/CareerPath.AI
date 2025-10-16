<template>
  <div
    class="w-full bg-cyan-50 rounded-2xl py-12 px-6 md:px-12 flex flex-col items-center justify-center text-center"
  >
    <h2 class="text-3xl md:text-4xl font-extrabold text-[#0D1B2A] mb-3">
      <slot name="title">Default Title</slot>
    </h2>
    <p class="text-gray-700 text-base md:text-lg">
      <slot name="subtitle">Default subtitle.</slot>
    </p>
  </div>
</template>
