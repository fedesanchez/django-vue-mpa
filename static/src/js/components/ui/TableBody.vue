<script setup>
import theme from '@/themes/default'
const { tableBody } = theme
const baseStyle = tableBody.base
const cls = [baseStyle]
</script>

<template>
  <tbody :class="cls">
    <slot />
  </tbody>
</template>
