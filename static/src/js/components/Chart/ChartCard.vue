<script setup>
defineProps({
  title: String
})
</script>

<template>
  <div class="min-w-0 p-4 bg-white rounded-lg shadow-xs dark:bg-gray-800">
    <p class="mb-4 font-semibold text-gray-800 dark:text-gray-300">{{ title }}</p>
    <slot />
  </div>
</template>
