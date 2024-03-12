<script setup>
const props = defineProps({
  iconColorClass: {
    type: String,
    default: 'text-purple-600 dark:text-purple-100'
  },
  bgColorClass: {
    type: String,
    default: 'bg-purple-100 dark:bg-purple-600'
  }
})
const baseStyle = 'p-3 rounded-full'
</script>

<template>
  <div :class="[baseStyle, iconColorClass, bgColorClass]">
    <slot></slot>
  </div>
</template>
