<script setup>
import Card from './Card.vue'
import CardBody from './CardBody.vue'
defineProps({
  title: String,
  value: String
})
</script>

<template>
  <Card>
    <CardBody class="flex items-center">
      <slot></slot>
      <div>
        <p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">{{ title }}</p>
        <p class="text-lg font-semibold text-gray-700 dark:text-gray-200">{{ value }}</p>
      </div>
    </CardBody>
  </Card>
</template>
