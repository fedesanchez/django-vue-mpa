<script setup>
import Layout from '@/containers/Layout.vue'
import PageTitle from '@/components/Typography/PageTitle.vue'
import CTA from '@/components/CTA.vue'
import Button from '@/components/ui/Button.vue'
import Modal from '@/components/ui/Modal.vue'
import ModalHeader from '@/components/ui/ModalHeader.vue'
import ModalBody from '@/components/ui/ModalBody.vue'
import ModalFooter from '@/components/ui/ModalFooter.vue'
import { ref } from 'vue'

const isModalOpen = ref(false)

function openModal() {
  isModalOpen.value = true
}

function closeModal() {
  isModalOpen.value = false
}

const props = defineProps({
  routes: Array,
  user: Object
})
</script>

<template>
  <Layout :routes="routes" :user="user">
    <PageTitle>Modals</PageTitle>
    <CTA />

    <div>
      <Button @click="openModal">Open modal</Button>
    </div>

    <Modal :isOpen="isModalOpen" :onClose="closeModal">
      <ModalHeader>Modal header</ModalHeader>
      <ModalBody>
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nostrum et eligendi repudiandae
        voluptatem tempore!
      </ModalBody>
      <ModalFooter>
        <div className="hidden sm:block">
          <Button layout="outline" onClick="{closeModal}"> Cancel </Button>
        </div>
        <div className="hidden sm:block">
          <Button>Accept</Button>
        </div>
        <div className="block w-full sm:hidden">
          <Button block size="large" layout="outline" onClick="{closeModal}"> Cancel </Button>
        </div>
        <div className="block w-full sm:hidden">
          <Button block size="large"> Accept </Button>
        </div>
      </ModalFooter>
    </Modal>
  </Layout>
</template>
