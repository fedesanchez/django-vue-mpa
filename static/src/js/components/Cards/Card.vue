<script setup>
import theme from '@/themes/default'
const { card } = theme
const baseStyle = card.base
const uncoloredStyle = card.default

const props = defineProps({
  colored: {
    type: Boolean,
    default: false
  }
})
</script>

<template>
  <div :class="[baseStyle, !colored && uncoloredStyle]">
    <slot />
  </div>
</template>
