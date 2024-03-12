<script setup>
import theme from '@/themes/default'
const { tableContainer } = theme
const baseStyle = tableContainer.base
const cls = [baseStyle]
</script>
<template>
  <div class="cls">
    <slot />
  </div>
</template>
