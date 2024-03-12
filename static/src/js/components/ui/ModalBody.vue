<script setup>
import theme from '@/themes/default'
const { modalBody } = theme
const cls = modalBody.base
</script>

<template>
  <p :class="cls">
    <slot />
  </p>
</template>
