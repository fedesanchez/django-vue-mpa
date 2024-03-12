<script setup>
import theme from '@/themes/default'
const { label } = theme
const baseStyle = label.base
const checkStyle = label.check
const disabledStyle = label.disabled

const props = defineProps({
  check: Boolean,
  radio: Boolean,
  disabled: Boolean
})
const cls = [
  baseStyle,
  // check and radio are interchangeable
  (props.check || props.radio) && checkStyle,
  props.disabled && disabledStyle
]
</script>

<template>
  <label :class="cls">
    <slot />
  </label>
</template>
