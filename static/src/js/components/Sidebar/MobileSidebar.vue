<script setup>
import { isSidebarOpen, closeSidebar } from '@/stores/sidebar'
import SidebarContent from './SidebarContent.vue'
import { Backdrop } from '@/components/ui'
</script>

<template>
  <Transition>
    <div v-show="isSidebarOpen">
      <Transition
        enter-active-class="transition ease-out duration-150"
        enter-from-class="opacity-0"
        enter-to-class="opacity-100"
        leave-active-class="transition ease-in duration-150"
        leave-from-class="opacity-100"
        leave-to-class="opacity-0"
      >
        <Backdrop @click="closeSidebar" v-show="isSidebarOpen" />
      </Transition>

      <Transition
        enter-active-class="transition ease-in-out duration-150"
        enter-from-class="opacity-0 transform -translate-x-20"
        enter-to-class="opacity-100"
        leave-active-class="transition ease-in-out duration-150"
        leave-from-class="opacity-100"
        leave-to-class="opacity-0 transform -translate-x-20"
      >
        <aside
          class="fixed inset-y-0 z-50 flex-shrink-0 w-64 mt-16 overflow-y-auto bg-white dark:bg-gray-800 lg:hidden"
        >
          <SidebarContent />
        </aside>
      </Transition>
    </div>
  </Transition>
</template>
