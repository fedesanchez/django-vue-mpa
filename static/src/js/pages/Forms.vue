<script setup>
import Layout from '@/containers/Layout.vue'
import PageTitle from '@/components/Typography/PageTitle.vue'
import SectionTitle from '@/components/Typography/SectionTitle.vue'
import CTA from '@/components/CTA.vue'
import { MailIcon } from '@/icons'
import { Button, Label, Input, Select, Textarea, HelperText } from '@/components/ui'
const props = defineProps({
  routes: Array,
  user: Object
})
</script>

<template>
  <Layout :routes="routes" :user="user">
    <PageTitle>Forms</PageTitle>
    <CTA />
    <SectionTitle>Elements</SectionTitle>

    <div class="px-4 py-3 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800">
      <Label>
        <span>Name</span>
        <Input class="mt-1" placeholder="Jane Doe" />
      </Label>

      <Label class="mt-4">
        <span>Disabled</span>
        <Input disabled class="mt-1" placeholder="Jane Doe" />
      </Label>

      <div class="mt-4">
        <Label>Account Type</Label>
        <div class="mt-2">
          <Label radio>
            <Input type="radio" value="personal" name="accountType" />
            <span class="ml-2">Personal</span>
          </Label>
          <Label class="ml-6" radio>
            <Input type="radio" value="business" name="accountType" />
            <span class="ml-2">Business</span>
          </Label>
          <Label disabled class="ml-6" radio>
            <Input disabled type="radio" value="disabled" name="accountType" />
            <span class="ml-2">Disabled</span>
          </Label>
        </div>
      </div>

      <Label class="mt-4">
        <span>Requested Limit</span>
        <Select class="mt-1">
          <option>$1,000</option>
          <option>$5,000</option>
          <option>$10,000</option>
          <option>$25,000</option>
        </Select>
      </Label>

      <Label class="mt-4">
        <span>Multiselect</span>
        <Select class="mt-1" multiple>
          <option>Option 1</option>
          <option>Option 2</option>
          <option>Option 3</option>
          <option>Option 4</option>
          <option>Option 5</option>
        </Select>
      </Label>

      <Label class="mt-4">
        <span>Message</span>
        <Textarea
          class="mt-1"
          rows="3"
          placeholder="this is the placeholder"
          value="Enter some long form content."
        />
      </Label>

      <Label class="mt-6" check>
        <Input type="checkbox" />
        <span class="ml-2"> I agree to the <span class="underline">privacy policy</span> </span>
      </Label>
    </div>

    <SectionTitle>Validation</SectionTitle>

    <div class="px-4 py-3 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800">
      <Label>
        <span>Invalid input</span>
        <Input class="mt-1" :valid="false" placeholder="Jane Doe" />
        <HelperText :valid="false">Your password is too short.</HelperText>
      </Label>

      <Label class="mt-4">
        <span>Valid input</span>
        <Input class="mt-1" :valid="true" placeholder="Jane Doe" />
        <HelperText :valid="true">Your password is strong.</HelperText>
      </Label>

      <Label class="mt-4">
        <span>Helper text</span>
        <Input class="mt-1" placeholder="Jane Doe" />
        <HelperText>Your password must be at least 6 characters long.</HelperText>
      </Label>
    </div>

    <!-- Inputs with icons -->
    <SectionTitle>Icons</SectionTitle>

    <div class="px-4 py-3 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800">
      <Label>
        <span>Icon left</span>
        <!-- focus-within sets the color for the icon when input is focused -->
        <div
          class="relative text-gray-500 focus-within:text-purple-600 dark:focus-within:text-purple-400"
        >
          <input
            class="block w-full pl-10 mt-1 text-sm text-black dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray form-input"
            placeholder="Jane Doe"
          />
          <div class="absolute inset-y-0 flex items-center ml-3 pointer-events-none">
            <MailIcon class="w-5 h-5" aria-hidden="true" />
          </div>
        </div>
      </Label>

      <Label class="mt-4">
        <span class="text-gray-700 dark:text-gray-400">Icon right</span>
        <!-- focus-within sets the color for the icon when input is focused -->
        <div
          class="relative text-gray-500 focus-within:text-purple-600 dark:focus-within:text-purple-400"
        >
          <input
            class="block w-full pr-10 mt-1 text-sm text-black dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray form-input"
            placeholder="Jane Doe"
          />
          <div class="absolute inset-y-0 right-0 flex items-center mr-3 pointer-events-none">
            <MailIcon class="w-5 h-5" aria-hidden="true" />
          </div>
        </div>
      </Label>
    </div>

    <!-- Inputs with buttons -->
    <SectionTitle>Buttons</SectionTitle>

    <div class="px-4 py-3 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800">
      <Label>
        <span>Button left</span>
        <div class="relative">
          <input
            class="block w-full pl-20 mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray form-input"
            placeholder="Jane Doe"
          />
          <button
            class="absolute inset-y-0 px-4 text-sm font-medium leading-5 text-white transition-colors duration-150 bg-purple-600 border border-transparent rounded-l-md active:bg-purple-600 hover:bg-purple-700 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray"
          >
            Click
          </button>
        </div>
      </Label>

      <Label class="mt-4">
        <span>Button right</span>
        <div class="relative text-gray-500 focus-within:text-purple-600">
          <input
            class="block w-full pr-20 mt-1 text-sm text-black dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray form-input"
            placeholder="Jane Doe"
          />
          <button
            class="absolute inset-y-0 right-0 px-4 text-sm font-medium leading-5 text-white transition-colors duration-150 bg-purple-600 border border-transparent rounded-r-md active:bg-purple-600 hover:bg-purple-700 focus:outline-none focus:shadow-outline-purple"
          >
            Click
          </button>
        </div>
      </Label>
    </div>
  </Layout>
</template>
