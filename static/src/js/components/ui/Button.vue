<script setup>
import Icon from '../ui/Icon.vue'
import { useSlots } from 'vue'
import theme from '@/themes/default'
const { button } = theme
const slots = useSlots()
import { toRefs, computed } from 'vue'

const props = defineProps({
  disabled: {
    type: Boolean,
    default: false
  },
  size: {
    type: String,
    default: 'regular'
  },
  icon: {
    type: String
  },
  iconLeft: {
    type: String
  },
  iconRight: {
    type: String
  },
  layout: {
    type: String,
    default: 'primary'
  },
  block: {
    type: Boolean,
    default: false
  },
  type: {
    type: String,
    default: 'button'
  }
})
const { layout, size, disabled, block, icon, iconLeft, iconRight } = toRefs(props)

const baseStyle = button.base
const blockStyle = button.block
const sizeStyles = {
  larger: button.size.larger,
  large: button.size.large,
  regular: button.size.regular,
  small: button.size.small,
  /**
   * Only used in Pagination.
   * Not meant for general use.
   */
  pagination: button.size.pagination
}
const iconSizeStyles = {
  larger: button.size.icon.larger,
  large: button.size.icon.large,
  regular: button.size.icon.regular,
  small: button.size.icon.small,
  pagination: button.size.icon.regular
}

const layoutStyles = {
  primary: button.primary.base,
  outline: button.outline.base,
  link: button.link.base
}
const activeStyles = {
  primary: button.primary.active,
  outline: button.outline.active,
  link: button.link.active
}
const disabledStyles = {
  primary: button.primary.disabled,
  outline: button.outline.disabled,
  link: button.link.disabled
}

/**
 * Only used in DropdownItem.
 * Not meant for general use.
 */
const dropdownItemStyle = button.dropdownItem.base

const hasSlot = !!slots
const hasIcon = !!icon.value || !!iconLeft.value || !!iconRight.value

const buttonStyles = computed(() =>
  layout.value === '__dropdownItem'
    ? [dropdownItemStyle]
    : [
        baseStyle,
        hasIcon && !hasSlot && iconSizeStyles[size.value],
        // has icon and children
        hasIcon && hasSlot && sizeStyles[size.value],
        !hasIcon && sizeStyles[size.value],
        layoutStyles[layout.value],
        disabled.value ? disabledStyles[layout.value] : activeStyles[layout.value],
        block.value ? blockStyle : null
      ]
)

const ComponentIcon = computed(() => icon.value || iconLeft.value || iconRight.value)
const iconBaseStyle = button.icon[size.value]
const iconLeftStyle = [iconBaseStyle, hasSlot ? button.icon.left : '']
const iconRightStyles = [iconBaseStyle, hasSlot ? button.icon.right : '']
</script>

<template>
  <button :type="type" :class="buttonStyles" :disabled="disabled">
    <template v-if="iconLeft">
      <Icon :icon="ComponentIcon" :class="iconLeftStyle" />
    </template>

    <template v-if="icon">
      <Icon :icon="ComponentIcon" :class="iconBaseStyle" />
    </template>
    <slot />

    <template v-if="iconRight">
      <Icon :icon="ComponentIcon" :class="iconRightStyles" />
    </template>
  </button>
</template>
