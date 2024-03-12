<script setup>
import theme from '@/themes/default'
const { select } = theme
const baseStyle = select.base
const activeStyle = select.active
const validStyle = select.valid
const invalidStyle = select.invalid
const disabledStyle = select.disabled
const selectStyle = select.select

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
  multiple: {
    type: Boolean,
    default: false
  }
})

const cls = [
  baseStyle,
  // don't apply activeStyle if has valid or disabled
  !hasValidation(props.valid) && !props.disabled && activeStyle,
  // don't apply disabledStyle if has valid
  !hasValidation(props.valid) && props.disabled && disabledStyle,
  validationStyle(props.valid),
  !props.multiple && selectStyle
]
</script>

<template>
  <select :class="cls" :multiple="multiple" :disabled="disabled">
    <slot />
  </select>
</template>
