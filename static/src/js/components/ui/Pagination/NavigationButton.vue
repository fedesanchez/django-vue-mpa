<script setup>
import { Button } from '@/components/ui'
import { Link } from '@inertiajs/vue3'

const props = defineProps({
  href: String,
  disabled: Boolean,
  directionIcon: String
})
const ariaLabel = props.directionIcon === 'prev' ? 'Previous' : 'Next'
const icon = props.directionIcon === 'prev' ? 'PrevIcon' : 'NextIcon'
</script>

<template>
  <Link :href="href" preserve-scroll>
    <Button
      size="small"
      layout="link"
      :icon="icon"
      :disabled="disabled"
      :aria-label="ariaLabel"
    />
  </Link>
</template>
