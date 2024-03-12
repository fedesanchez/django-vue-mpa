<script setup>
import Layout from '@/containers/Layout.vue'
import { ref, watch } from 'vue'
import CTA from '@/components/CTA.vue'
import InfoCard from '@/components/Cards/InfoCard.vue'
import ChartCard from '@/components/Chart/ChartCard.vue'
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
} from 'chart.js'
import { Doughnut, Line } from 'vue-chartjs'
import ChartLegend from '@/components/Chart/ChartLegend.vue'
import PageTitle from '@/components/Typography/PageTitle.vue'
import { ChatIcon, CartIcon, MoneyIcon, PeopleIcon } from '@/icons'
import RoundIcon from '@/components/RoundIcon.vue'
import response from '@/utils/demo/tableData'
import {
  TableBody,
  TableContainer,
  Table,
  TableHeader,
  TableCell,
  TableRow,
  TableFooter,
  Avatar,
  Badge,
  Pagination
} from '@/components/ui'

import { doughnutOptions, lineOptions, doughnutLegends, lineLegends } from '@/utils/demo/chartsData'

const page = ref(1)
const data = ref([])

// pagination setup
const resultsPerPage = 10
const totalResults = response.length

// pagination change control
function onPageChange(p) {
  page.value = p
}

// on page change, load new sliced data
// here you would make another server request for new data
watch(page, () => {
  data.value = response.slice((page.value - 1) * resultsPerPage, page.value * resultsPerPage)
})
//Initializa data (For some reason watch inmediate:true dosent work )
data.value = response.slice((page.value - 1) * resultsPerPage, page.value * resultsPerPage)

ChartJS.register(ArcElement, Tooltip, CategoryScale, LinearScale, PointElement, LineElement)

const props = defineProps({
  routes: Array,
  user: Object
})
</script>

<template>
  <Layout :routes="routes" :user="user">
    <PageTitle>Dashboard</PageTitle>

    <CTA />

    <!-- Cards -->
    <div class="grid gap-6 mb-8 md:grid-cols-2 xl:grid-cols-4">
      <InfoCard title="Total clients" value="6389">
        <RoundIcon
          iconColorClass="text-orange-500 dark:text-orange-100"
          bgColorClass="bg-orange-100 dark:bg-orange-500"
          class="mr-4"
        >
          <PeopleIcon class="w-5 h-5" />
        </RoundIcon>
      </InfoCard>

      <InfoCard title="Account balance" value="$ 46,760.89">
        <RoundIcon
          iconColorClass="text-green-500 dark:text-green-100"
          bgColorClass="bg-green-100 dark:bg-green-500"
          class="mr-4"
        >
          <MoneyIcon class="w-5 h-5" />
        </RoundIcon>
      </InfoCard>

      <InfoCard title="New sales" value="376">
        <RoundIcon
          iconColorClass="text-blue-500 dark:text-blue-100"
          bgColorClass="bg-blue-100 dark:bg-blue-500"
          class="mr-4"
        >
          <CartIcon class="w-5 h-5" />
        </RoundIcon>
      </InfoCard>

      <InfoCard title="Pending contacts" value="35">
        <RoundIcon
          iconColorClass="text-teal-500 dark:text-teal-100"
          bgColorClass="bg-teal-100 dark:bg-teal-500"
          class="mr-4"
        >
          <ChatIcon class="w-5 h-5" />
        </RoundIcon>
      </InfoCard>
    </div>

    <TableContainer>
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
          <TableRow v-for="(user, index) in data" :key="index">
            <TableCell>
              <div class="flex items-center text-sm">
                <Avatar class="hidden mr-3 md:block" :src="user.avatar" alt="User image" />
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
              <Badge type="{user.status}">{{ user.status }}</Badge>
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
          label="Table navigation"
          :onChange="onPageChange"
        />
      </TableFooter>
    </TableContainer>

    <PageTitle>Charts</PageTitle>
    <div class="grid gap-6 mb-8 md:grid-cols-2">
      <ChartCard title="Revenue">
        <Doughnut v-bind="doughnutOptions" />
        <ChartLegend :legends="doughnutLegends" />
      </ChartCard>

      <ChartCard title="Traffic">
        <Line v-bind="lineOptions" />
        <ChartLegend :legends="lineLegends" />
      </ChartCard>
    </div>
  </Layout>
</template>
