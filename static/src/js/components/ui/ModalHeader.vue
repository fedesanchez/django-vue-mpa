<script setup>
import theme from '@/themes/default'
const { modalHeader } = theme
const cls = modalHeader.base
</script>

<template>
  <p :class="cls">
    <slot />
  </p>
</template>
