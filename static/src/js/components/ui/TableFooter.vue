<script setup>
import theme from '@/themes/default'
const { tableFooter } = theme
const baseStyle = tableFooter.base
const cls = [baseStyle]
</script>

<template>
  <div :class="cls">
    <slot />
  </div>
</template>
