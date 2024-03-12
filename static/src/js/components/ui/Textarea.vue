<script setup>
import theme from '@/themes/default'
const { textarea } = theme
const baseStyle = textarea.base
const activeStyle = textarea.active
const disabledStyle = textarea.disabled
const validStyle = textarea.valid
const invalidStyle = textarea.invalid

function hasValidation(valid) {
  return valid !== undefined
}

function validationStyle(valid) {
  if (hasValidation(valid)) {
    return valid ? validStyle : invalidStyle
  }
  return ''
}

const props = defineProps({
  valid: {
    type: Boolean,
    default: undefined
  },
  disabled: {
    type: Boolean,
    default: false
  },
  value: String
})

const cls = [
  baseStyle,
  // don't apply activeStyle if has valid or disabled
  !hasValidation(props.valid) && !props.disabled && activeStyle,
  // don't apply disabledStyle if has valid
  !hasValidation(props.valid) && props.disabled && disabledStyle,
  validationStyle(props.valid)
]
</script>

<template>
  <textarea :class="cls" :disabled="disabled">{{ value }}</textarea>
</template>
