<script setup>
import Layout from '@/containers/Layout.vue'
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
import Icon from "@/components/ui/Icon"
import RoundIcon from '@/components/RoundIcon.vue'
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

ChartJS.register(ArcElement, Tooltip, CategoryScale, LinearScale, PointElement, LineElement)

const props = defineProps({
  routes: Array,
  user: Object,
  page_obj: Object,
  cards: Array
})

const pagination = {
  has_previous: props.page_obj.has_previous,
  previous_page_number: props.page_obj.previous_page_number,
  active_page: props.page_obj.number,  
  has_next: props.page_obj.has_next,
  next_page_number: props.page_obj.next_page_number,
  start_index: props.page_obj.start_index,
  end_index: props.page_obj.end_index,
  num_pages: props.page_obj.paginator.num_pages,
  per_page: props.page_obj.paginator.per_page,
  count: props.page_obj.paginator.count
}
</script>

<template>
  <Layout :routes="routes" :user="user">
    <PageTitle>Dashboard</PageTitle>

    <CTA />

    <!-- Cards -->
    <div class="grid gap-6 mb-8 md:grid-cols-2 xl:grid-cols-4">
      
      <div v-for="(card, index) in cards" :key="index">
         <InfoCard :title="card.title" :value="`${card.value}`">
          <RoundIcon
            :iconColorClass="`text-${card.color}-500 dark:text-${card.color}-100`"
            :bgColorClass="`bg-${card.color}-100 dark:bg-${card.color}-500`"
            class="mr-4"
          >
            <Icon :icon="card.icon" class="w-5 h-5" />
          </RoundIcon>
        </InfoCard>
      </div>

    </div>

     <!-- Table -->
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
          <TableRow v-for="(user, index) in page_obj.object_list" :key="index">
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
              <Badge :type="user.status">{{ user.status }}</Badge>
            </TableCell>
            <TableCell>
              <span class="text-sm">{{ user.date }}</span>
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
      <TableFooter>
        <Pagination
          v-bind="pagination"        
        />
      </TableFooter>
    </TableContainer>

     <!-- Charts -->

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
