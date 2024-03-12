<script setup>
import { Link } from '@inertiajs/vue3'
import ImageLight from '../assets/img/login-office.jpeg'
import ImageDark from '../assets/img/login-office-dark.jpeg'
import { GithubIcon, TwitterIcon } from '@/icons'
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
            <h1 class="mb-4 text-xl font-semibold text-gray-700 dark:text-gray-200">Login</h1>
            <Label>
              <span>Email</span>
              <Input class="mt-1" type="email" placeholder="john@doe.com" />
            </Label>

            <Label class="mt-4">
              <span>Password</span>
              <Input class="mt-1" type="password" placeholder="***************" />
            </Label>

            <Link
              class="align-bottom inline-flex items-center justify-center cursor-pointer leading-5 transition-colors duration-150 font-medium focus:outline-none px-4 py-2 rounded-lg text-sm text-white bg-purple-600 border border-transparent active:bg-purple-600 hover:bg-purple-700 focus:ring focus:ring-purple-300 w-full mt-4"
              href="/app"
            >
              Log in
            </Link>

            <hr class="my-8" />

            <Button block layout="outline">
              <GithubIcon class="w-4 h-4 mr-2" aria-hidden="true" />
              Github
            </Button>
            <Button class="mt-4" block layout="outline">
              <TwitterIcon class="w-4 h-4 mr-2" aria-hidden="true" />
              Twitter
            </Button>

            <p class="mt-4">
              <Link
                class="text-sm font-medium text-purple-600 dark:text-purple-400 hover:underline"
                href="/forgot-password"
              >
                Forgot your password?
              </Link>
            </p>
            <p class="mt-1">
              <Link
                class="text-sm font-medium text-purple-600 dark:text-purple-400 hover:underline"
                href="/create-account"
              >
                Create account
              </Link>
            </p>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>
