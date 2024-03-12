<script setup>
import theme from '../../themes/default'
const { dropdownItem } = theme
const baseStyle = dropdownItem.base
import Button from './Button.vue'
</script>

<template>
  <li :class="[baseStyle]">
    <Button layout="__dropdownItem">
      <slot />
    </Button>
  </li>
</template>
