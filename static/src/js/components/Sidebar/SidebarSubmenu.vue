<script setup>
import { ref } from 'vue'
import { Link } from '@inertiajs/vue3'
import { DropdownIcon } from '../../icons/index'
import { Icon } from '@/components/ui'

defineProps({
  name: {
    type: String,
    required: true
  },
  icon: {
    type: String,
    required: true
  },
  routes: {
    type: Array,
    required: true
  }
})

const isDropdownMenuOpen = ref(false)

function handleDropdownMenuClick() {
  isDropdownMenuOpen.value = !isDropdownMenuOpen.value
}
</script>

<template>
  <li class="relative px-6 py-3" :key="name">
    <button
      class="inline-flex items-center justify-between w-full text-sm font-semibold transition-colors duration-150 hover:text-gray-800 dark:hover:text-gray-200"
      @click="handleDropdownMenuClick"
      aria-haspopup="true"
    >
      <span class="inline-flex items-center">
        <Icon class="w-5 h-5" aria-hidden="true" :icon="icon" />
        <span class="ml-4">{{ name }}</span>
      </span>
      <DropdownIcon class="w-4 h-4" aria-hidden="true" />
    </button>
    <Transition
      name="submenu"
      enter-active-class="transition ease-in duration-150"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition ease-out duration-150"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <ul
        v-show="isDropdownMenuOpen"
        class="p-2 mt-2 space-y-2 overflow-hidden text-sm font-medium text-gray-500 rounded-md shadow-inner bg-gray-50 dark:text-gray-400 dark:bg-gray-900"
        aria-label="submenu"
      >
        <li
          v-for="(item, index) in routes"
          class="px-2 py-1 transition-colors duration-150 hover:text-gray-800 dark:hover:text-gray-200"
          v-bind:key="item.name"
        >
          <Link :href="item.path" class="w-full">
            {{ item.name }}
          </Link>
        </li>
      </ul>
    </Transition>
  </li>
</template>
