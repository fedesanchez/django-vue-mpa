<script setup>
import { Button } from '@/components/ui'
import { Link } from '@inertiajs/vue3'

const props = defineProps({
  page: String | Number,
  isActive: { type: Boolean, default: false },
  href: String
})
</script>

<template>
  <Link :href="href" preserve-scroll>
    <Button size="pagination" :layout="isActive ? 'primary' : 'link'">
      {{ page }}
    </Button>
  </Link>
</template>
