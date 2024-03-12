<script setup>
import { Button } from '@/components/ui'

const props = defineProps({
  page: String | Number,
  isActive: { type: Boolean, default: false },
  onClick: Function
})
</script>

<template>
  <Button size="pagination" :layout="isActive ? 'primary' : 'link'" @click="onClick">
    {{ page }}
  </Button>
</template>
