<script setup>
import ImageLight from '../assets/img/forgot-password-office.jpeg'
import ImageDark from '../assets/img/forgot-password-office-dark.jpeg'
import { Label, Input, Button } from '@/components/ui'
</script>

<template>
  <div class="flex items-center min-h-screen p-6 bg-gray-50 dark:bg-gray-900">
    <div
      class="flex-1 h-full max-w-4xl mx-auto overflow-hidden bg-white rounded-lg shadow-xl dark:bg-gray-800"
    >
      <div class="flex flex-col overflow-y-auto md:flex-row">
        <div class="h-32 md:h-auto md:w-1/2">
          <img
            aria-hidden="true"
            class="object-cover w-full h-full dark:hidden"
            :src="ImageLight"
            alt="Office"
          />
          <img
            aria-hidden="true"
            class="hidden object-cover w-full h-full dark:block"
            :src="ImageDark"
            alt="Office"
          />
        </div>
        <main class="flex items-center justify-center p-6 sm:p-12 md:w-1/2">
          <div class="w-full">
            <h1 class="mb-4 text-xl font-semibold text-gray-700 dark:text-gray-200">
              Forgot password
            </h1>

            <Label>
              <span>Email</span>
              <Input class="mt-1" placeholder="Jane Doe" />
            </Label>

            <Button tag="{Link}" to="/login" block class="mt-4"> Recover password </Button>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>
