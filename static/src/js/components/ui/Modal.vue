<script setup>
import Backdrop from './Backdrop.vue'

import theme from '@/themes/default'
const { modal } = theme
const baseStyle = modal.base

const props = defineProps({
  isOpen: Boolean,
  onClose: Function
})
</script>

<template>
  <Transition>
    <Transition
      enter-active-class="transition ease-out duration-150"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition ease-in duration-150"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <Backdrop @click="onClose" v-show="isOpen">
        <Transition
          enter-active-class="transition ease-out duration-150"
          enter-from-class="opacity-0 transform translate-y-1/2"
          enter-to-class="opacity-100"
          leave-active-class="transition ease-in duration-150"
          leave-from-class="opacity-100"
          leave-to-class="opacity-0  transform translate-y-1/2"
        >
          <div :class="baseStyle" role="dialog" v-show="isOpen">
            <header class="flex justify-end">
              <button
                class="inline-flex items-center justify-center w-6 h-6 text-gray-400 transition-colors duration-150 rounded dark:hover:text-gray-200 hover: hover:text-gray-700"
                aria-label="close"
                @click="onClose"
              >
                <svg
                  class="w-4 h-4"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                  role="img"
                  aria-hidden="true"
                >
                  <path
                    d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                    clipRule="evenodd"
                    fillRule="evenodd"
                  ></path>
                </svg>
              </button>
            </header>
            <slot />
          </div>
        </Transition>
      </Backdrop>
    </Transition>
  </Transition>
</template>
