<script>
import * as icons from '@/icons/index'
export default {
  components: {
    ...icons
  },
  props: {
    icon: {
      type: String,
      required: true
    }
  }
}
</script>

<template>
  <component :is="icon"></component>
</template>
