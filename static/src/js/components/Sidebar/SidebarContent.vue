<script setup>
import { Link } from '@inertiajs/vue3'
import SidebarSubmenu from './SidebarSubmenu.vue'
import routes from '../../router/sidebar.js'
import { Icon, Button } from '../ui/'
</script>

<template>
  <div class="py-4 text-gray-500 dark:text-gray-400">
    <a class="ml-6 text-lg font-bold text-gray-800 dark:text-gray-200" href="#"> Windmill </a>
    <ul class="mt-6">
      <template v-for="route in routes">
        <template v-if="route.routes">
          <SidebarSubmenu v-bind="route" />
        </template>
        <template v-else>
          <li class="relative px-6 py-3" v-bind:key="route.name">
            <Link
              :href="route.path"
              class="inline-flex items-center w-full text-sm font-semibold transition-colors duration-150 hover:text-gray-800 dark:hover:text-gray-200"
              activeClass="text-gray-800 dark:text-gray-100"
            >
              <Icon class="w-5 h-5" aria-hidden="true" :icon="route.icon" />
              <span class="ml-4">{{ route.name }}</span>
            </Link>
          </li>
        </template>
      </template>
    </ul>
    <div class="px-6 my-6">
      <Button>
        Create account
        <span class="ml-2" aria-hidden="true"> + </span>
      </Button>
    </div>
  </div>
</template>
