<script setup>
import { watch, ref } from 'vue'
import theme from '../../themes/default'
const { dropdown } = theme
const props = defineProps({
  onClose: Function,
  isOpen: { type: Boolean, default: false },
  align: { type: String, default: 'left' }
})
const baseStyle = dropdown.base
const alignStyle = dropdown.align[props.align]

function handleEsc(e) {
  if (e.key === 'Esc' || e.key === 'Escape') {
    props.onClose()
  }
}

const dropdownRef = ref(null)
function handleClickOutside(e) {
  if (dropdownRef.value && !dropdownRef.value.contains(e.target)) {
    props.onClose()
  }
}

watch(
  () => props.isOpen,
  (isOpen) => {
    if (isOpen) {
      console.log('add Listener')
      document.addEventListener('click', handleClickOutside, { capture: true })
      document.addEventListener('keydown', handleEsc, { capture: true })
    } else {
      console.log('Remove listeners')
      document.removeEventListener('click', handleClickOutside, { capture: true })
      document.removeEventListener('keydown', handleEsc, { capture: true })
    }
  }
)

const cls = [baseStyle, alignStyle]
</script>

<template>
  <Transition
    leave-active-class="transition ease-out duration-150"
    leave-from-class="opacity-100"
    leave-to-class="opacity-0"
  >
    <div v-show="isOpen">
      <ul :class="cls" ref="dropdownRef" aria-label="submenu">
        <slot></slot>
      </ul>
    </div>
  </Transition>
</template>
