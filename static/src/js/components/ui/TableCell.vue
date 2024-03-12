<script setup>
import theme from '@/themes/default'
const { tableCell } = theme
const baseStyle = tableCell.base
const cls = [baseStyle]
</script>

<template>
  <td :class="cls">
    <slot />
  </td>
</template>
