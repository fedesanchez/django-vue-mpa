<script setup>
import Layout from '@/containers/Layout.vue'
import { ref, watch } from 'vue'
import PageTitle from '../components/Typography/PageTitle.vue'
import SectionTitle from '../components/Typography/SectionTitle.vue'
import CTA from '../components/CTA.vue'
import {
  Table,
  TableHeader,
  TableCell,
  TableBody,
  TableRow,
  TableFooter,
  TableContainer,
  Badge,
  Avatar,
  Button,
  Pagination
} from '../components/ui'
import { EditIcon, TrashIcon } from '../icons'
import response from '../utils/demo/tableData'
// make a copy of the data, for the second table
const response2 = response.concat([])
/**
 * DISCLAIMER: This code could be badly improved, but for the sake of the example
 * and readability, all the logic for both table are here.
 * You would be better served by dividing each table in its own
 * component, like Table(?) and TableWithActions(?) hiding the
 * presentation details away from the page view.
 */

// setup pages control for every table

const pageTable1 = ref(1)
const pageTable2 = ref(1)

// setup data for every table
const dataTable1 = ref([])
const dataTable2 = ref([])

// pagination setup
const resultsPerPage = 10
const totalResults = response.length

// pagination change control
function onPageChangeTable1(p) {
  pageTable1.value = p
}

// pagination change control
function onPageChangeTable2(p) {
  pageTable2.value = p
}

// on page change, load new sliced data
// here you would make another server request for new data

watch(pageTable1, () => {
  dataTable1.value = response.slice(
    (pageTable1.value - 1) * resultsPerPage,
    pageTable1.value * resultsPerPage
  )
})

watch(pageTable2, () => {
  dataTable2.value = response2.slice(
    (pageTable2.value - 1) * resultsPerPage,
    pageTable2.value * resultsPerPage
  )
})

//Load first page
dataTable1.value = response.slice(
  (pageTable1.value - 1) * resultsPerPage,
  pageTable1.value * resultsPerPage
)
dataTable2.value = response2.slice(
  (pageTable2.value - 1) * resultsPerPage,
  pageTable2.value * resultsPerPage
)
</script>

<template>
  <Layout>
    <PageTitle>Tables</PageTitle>
    <CTA />

    <SectionTitle>Simple table</SectionTitle>
    <TableContainer class="mb-8">
      <Table>
        <TableHeader>
          <tr>
            <TableCell>Client</TableCell>
            <TableCell>Amount</TableCell>
            <TableCell>Status</TableCell>
            <TableCell>Date</TableCell>
          </tr>
        </TableHeader>
        <TableBody>
          <TableRow v-for="(user, index) in dataTable1" :key="index">
            <TableCell>
              <div class="flex items-center text-sm">
                <Avatar class="hidden mr-3 md:block" :src="user.avatar" alt="User avatar" />
                <div>
                  <p class="font-semibold">{{ user.name }}</p>
                  <p class="text-xs text-gray-600 dark:text-gray-400">{{ user.job }}</p>
                </div>
              </div>
            </TableCell>
            <TableCell>
              <span class="text-sm">$ {{ user.amount }}</span>
            </TableCell>
            <TableCell>
              <Badge :type="user.status">{{ user.status }}</Badge>
            </TableCell>
            <TableCell>
              <span class="text-sm">{{ new Date(user.date).toLocaleDateString() }}</span>
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
      <TableFooter>
        <Pagination
          :totalResults="totalResults"
          :resultsPerPage="resultsPerPage"
          :onChange="onPageChangeTable1"
          label="Table navigation"
        />
      </TableFooter>
    </TableContainer>

    <SectionTitle>Table with actions</SectionTitle>
    <TableContainer class="mb-8">
      <Table>
        <TableHeader>
          <tr>
            <TableCell>Client</TableCell>
            <TableCell>Amount</TableCell>
            <TableCell>Status</TableCell>
            <TableCell>Date</TableCell>
            <TableCell>Actions</TableCell>
          </tr>
        </TableHeader>
        <TableBody>
          <TableRow v-for="(user, index) in dataTable2" :key="index">
            <TableCell>
              <div class="flex items-center text-sm">
                <Avatar class="hidden mr-3 md:block" :src="user.avatar" alt="User avatar" />
                <div>
                  <p class="font-semibold">{{ user.name }}</p>
                  <p class="text-xs text-gray-600 dark:text-gray-400">{{ user.job }}</p>
                </div>
              </div>
            </TableCell>
            <TableCell>
              <span class="text-sm">$ {{ user.amount }}</span>
            </TableCell>
            <TableCell>
              <Badge :type="user.status">{{ user.status }}</Badge>
            </TableCell>
            <TableCell>
              <span class="text-sm">{{ new Date(user.date).toLocaleDateString() }}</span>
            </TableCell>
            <TableCell>
              <div class="flex items-center space-x-4">
                <Button layout="link" size="icon" aria-label="Edit">
                  <EditIcon class="w-5 h-5" aria-hidden="true" />
                </Button>
                <Button layout="link" size="icon" aria-label="Delete">
                  <TrashIcon class="w-5 h-5" aria-hidden="true" />
                </Button>
              </div>
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
      <TableFooter>
        <Pagination
          :totalResults="totalResults"
          :resultsPerPage="resultsPerPage"
          :onChange="onPageChangeTable2"
          label="Table navigation"
        />
      </TableFooter>
    </TableContainer>

  </Layout>
  </template>
