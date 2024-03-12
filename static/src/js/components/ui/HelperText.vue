<script setup>
import theme from '@/themes/default'
const { helperText } = theme

const baseStyle = helperText.base
const validStyle = helperText.valid
const invalidStyle = helperText.invalid

const validationStyle = (valid) => {
  switch (valid) {
    case true:
      return validStyle
    case false:
      return invalidStyle
    default:
      return ''
  }
}

const props = defineProps({
  valid: {
    type: Boolean,
    default: undefined
  }
})

const cls = [baseStyle, validationStyle(props.valid)]
</script>

<template>
  <span :class="cls">
    <slot />
  </span>
</template>
