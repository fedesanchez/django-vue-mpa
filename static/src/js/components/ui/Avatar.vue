<script setup>
import theme from '@/themes/default'
const { avatar } = theme
const baseStyle = avatar.base
const sizeStyles = {
  large: avatar.size.large,
  regular: avatar.size.regular,
  small: avatar.size.small
}

const props = defineProps({
  size: {
    type: String,
    default: 'regular'
  },
  alt: String,
  src: String
})

const cls = [baseStyle, sizeStyles[props.size]]
</script>

<template>
  <div :class="cls">
    <img class="object-cover w-full h-full rounded-full" :src="src" :alt="alt" loading="lazy" />
    <div class="absolute inset-0 rounded-full shadow-inner" aria-hidden="true"></div>
  </div>
</template>
