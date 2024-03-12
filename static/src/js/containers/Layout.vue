<script setup>
import { provide } from 'vue'
import LayoutHeader from '../components/Header.vue'
import Sidebar from '../components/Sidebar/index.vue'
import Main from '../containers/Main.vue'

const props = defineProps({
  routes: Array,
  user: Object
})

provide('routes', props.routes)
provide('user', props.user)
</script>

<template>
  <div class="flex h-screen bg-gray-50 dark:bg-gray-900">
    <Sidebar />
    <div class="flex flex-col flex-1 w-full">
      <LayoutHeader />
      <Main>
        <slot></slot>
      </Main>
    </div>
  </div>
</template>
