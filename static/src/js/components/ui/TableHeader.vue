<script setup>
import theme from '@/themes/default'
const { tableHeader } = theme
const baseStyle = tableHeader.base
const cls = [baseStyle]
</script>

<template>
  <thead :class="cls">
    <slot />
  </thead>
</template>
