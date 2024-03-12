<script setup>
import Layout from '@/containers/Layout.vue'
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement
} from 'chart.js'
import { Doughnut, Line, Bar } from 'vue-chartjs'
import ChartCard from '../components/Chart/ChartCard.vue'
import ChartLegend from '../components/Chart/ChartLegend.vue'
import PageTitle from '../components/Typography/PageTitle.vue'
import {
  doughnutOptions,
  lineOptions,
  barOptions,
  doughnutLegends,
  lineLegends,
  barLegends
} from '../utils/demo/chartsData'
ChartJS.register(
  ArcElement,
  Tooltip,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement
)
</script>

<template>
  <Layout>
    <PageTitle>Charts</PageTitle>
    <div class="grid gap-6 mb-8 md:grid-cols-2">
      <ChartCard title="Lines">
        <Line v-bind="lineOptions" />
        <ChartLegend :legends="lineLegends" />
      </ChartCard>

      <ChartCard title="Bars">
        <Bar v-bind="barOptions" />
        <ChartLegend :legends="barLegends" />
      </ChartCard>

      <!-- WARNING: doughnut chart is larger for some reason -->
      <ChartCard title="Doughnut">
        <Doughnut v-bind="doughnutOptions" />
        <ChartLegend :legends="doughnutLegends" />
      </ChartCard>
    </div>
  </Layout>
</template>
