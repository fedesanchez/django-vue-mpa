<script setup>
import theme from '@/themes/default'
const { tableRow } = theme
const baseStyle = tableRow.base
const cls = [baseStyle]
</script>

<template>
  <tr :class="cls">
    <slot />
  </tr>
</template>
