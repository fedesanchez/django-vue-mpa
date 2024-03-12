<script setup>
import theme from '@/themes/default'
const { modalFooter } = theme
const cls = modalFooter.base
</script>

<template>
  <footer :class="cls">
    <slot />
  </footer>
</template>
