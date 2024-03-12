<script setup>
import theme from '@/themes/default'
const { backdrop } = theme
const cls = backdrop.base
</script>

<template>
  <div :class="cls">
    <slot />
  </div>
</template>
