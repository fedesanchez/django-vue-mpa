<script setup>
import { Button } from '@/components/ui'

const props = defineProps({
  onClick: Function,
  disabled: Boolean,
  directionIcon: String
})
const ariaLabel = props.directionIcon === 'prev' ? 'Previous' : 'Next'
const icon = props.directionIcon === 'prev' ? 'PrevIcon' : 'NextIcon'
</script>

<template>
  <Button
    size="small"
    layout="link"
    :icon="icon"
    @click="onClick"
    :disabled="disabled"
    :aria-label="ariaLabel"
  />
</template>
