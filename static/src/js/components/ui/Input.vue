<script setup>
import theme from '@/themes/default'
const { input } = theme
const baseStyle = input.base
const activeStyle = input.active
const disabledStyle = input.disabled
const validStyle = input.valid
const invalidStyle = input.invalid
const radioStyle = input.radio
const checkStyle = input.checkbox

const props = defineProps({
  valid: {
    type: Boolean,
    default: undefined
  },
  disabled: {
    type: Boolean,
    default: false
  },
  type: {
    type: String,
    default: 'text'
  }
})

const cls = [
  typeStyle(props.type),
  // don't apply activeStyle if has valid or disabled
  !hasValidation(props.valid) && !props.disabled && activeStyle,
  // don't apply disabledStyle if has valid
  !hasValidation(props.valid) && props.disabled && disabledStyle,
  validationStyle(props.valid)
]

function hasValidation(valid) {
  return valid !== undefined
}

function validationStyle(valid) {
  if (hasValidation(valid)) {
    return valid ? validStyle : invalidStyle
  }
  return ''
}

function typeStyle(type) {
  switch (type) {
    case 'radio':
      return radioStyle
    case 'checkbox':
      return checkStyle
    default:
      return baseStyle
  }
}
</script>

<template>
  <input :class="cls" :type="type" :disabled="disabled" />
</template>
