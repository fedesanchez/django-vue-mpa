<script setup>
import theme from '@/themes/default'
const { badge } = theme
const baseStyle = badge.base
const typeStyle = {
  success: badge.success,
  danger: badge.danger,
  warning: badge.warning,
  neutral: badge.neutral,
  primary: badge.primary
}
const props = defineProps({
  type: { type: String, default: 'primary' }
})

const cls = [baseStyle, typeStyle[props.type]]
</script>

<template>
  <span :class="cls">
    <slot />
  </span>
</template>
