import { ref } from 'vue'
const isSidebarOpen = ref(false)

function toggleSidebar() {
  console.log('click')
  isSidebarOpen.value = !isSidebarOpen.value
}

function closeSidebar() {
  isSidebarOpen.value = false
}

export { isSidebarOpen, toggleSidebar, closeSidebar }
