<script setup>
defineProps({
  legends: Array
})
</script>

<template>
  <div class="flex justify-center mt-4 space-x-3 text-sm text-gray-600 dark:text-gray-400">
    <div v-for="legend in legends" class="flex items-center" :key="legend.title">
      <span :class="['inline-block w-3 h-3 mr-1 rounded-full', legend.color]"></span>
      <span>{{ legend.title }}</span>
    </div>
  </div>
</template>
