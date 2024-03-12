<script setup>
import Layout from '@/containers/Layout.vue'
import PageTitle from '@/components/Typography/PageTitle.vue'
const props = defineProps({
  routes: Array,
  user: Object
})
</script>

<template>
  <Layout :routes="routes" :user="user">
     <PageTitle>Blank</PageTitle>
  </Layout>
</template>
