<script setup>
import Layout from '@/containers/Layout.vue'
import PageTitle from '@/components/Typography/PageTitle.vue'
import SectionTitle from '@/components/Typography/SectionTitle.vue'
import CTA from '@/components/CTA.vue'
import InfoCard from '@/components/Cards/InfoCard.vue'
import Card from '@/components/Cards/Card.vue'
import CardBody from '@/components/Cards/CardBody.vue'
import { CartIcon, ChatIcon, MoneyIcon, PeopleIcon } from '@/icons'
import RoundIcon from '@/components/RoundIcon.vue'
const props = defineProps({
  routes: Array,
  user: Object
})
</script>

<template>
  <Layout :routes="routes" :user="user">
    <PageTitle>Cards</PageTitle>

    <CTA />

    <SectionTitle>Big section cards</SectionTitle>

    <Card class="mb-8 shadow-md">
      <CardBody>
        <p class="text-sm text-gray-600 dark:text-gray-400">Large, full width sections goes here</p>
      </CardBody>
    </Card>

    <SectionTitle>Responsive cards</SectionTitle>

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

    <SectionTitle>Cards with title</SectionTitle>

    <div class="grid gap-6 mb-8 md:grid-cols-2">
      <Card>
        <CardBody>
          <p class="mb-4 font-semibold text-gray-600 dark:text-gray-300">Revenue</p>
          <p class="text-gray-600 dark:text-gray-400">
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Fuga, cum commodi a omnis
            numquam quod? Totam exercitationem quos hic ipsam at qui cum numquam, sed amet ratione!
            Ratione, nihil dolorum.
          </p>
        </CardBody>
      </Card>

      <Card colored class="text-white bg-purple-600">
        <CardBody>
          <p class="mb-4 font-semibold">Colored card</p>
          <p>
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Fuga, cum commodi a omnis
            numquam quod? Totam exercitationem quos hic ipsam at qui cum numquam, sed amet ratione!
            Ratione, nihil dolorum.
          </p>
        </CardBody>
      </Card>
    </div>
  </Layout>  
</template>
