<script setup>
import { ref } from 'vue'
import {
  SearchIcon,
  MoonIcon,
  SunIcon,
  BellIcon,
  MenuIcon,
  OutlineCogIcon,
  OutlinePersonIcon,
  OutlineLogoutIcon
} from '@/icons'
import { Avatar, Button, Badge, Dropdown, DropdownItem, Input } from '@/components/ui'
import { theme, toggleTheme } from '../stores/theme'
import { toggleSidebar } from '../stores/sidebar'

const isNotificationsMenuOpen = ref(false)
const isProfileMenuOpen = ref(false)

function handleNotificationsClick() {
  isNotificationsMenuOpen.value = !isNotificationsMenuOpen.value
}

function handleProfileClick() {
  isProfileMenuOpen.value = !isProfileMenuOpen.value
}

function showAlert(msg) {
  alert(msg)
}
</script>

<template>
  <header class="z-40 py-4 bg-white shadow-bottom dark:bg-gray-800">
    <div
      class="container flex items-center justify-between h-full px-6 mx-auto text-purple-600 dark:text-purple-300"
    >
      <button
        class="p-1 mr-5 -ml-1 rounded-md lg:hidden focus:outline-none focus:shadow-outline-purple"
        @click="toggleSidebar"
        aria-label="Menu"
      >
        <MenuIcon class="w-6 h-6" aria-hidden="true" />
      </button>

      <div class="flex justify-center flex-1 lg:mr-32">
        <div class="relative w-full max-w-xl mr-6 focus-within:text-purple-500">
          <div class="absolute inset-y-0 flex items-center pl-2">
            <SearchIcon class="w-4 h-4" aria-hidden="true" />
          </div>
          <Input class="pl-8 text-gray-700" placeholder="Search for projects" aria-label="Search" />
        </div>
      </div>
      <ul class="flex items-center flex-shrink-0 space-x-6">
        <li class="flex">
          <button
            class="rounded-md focus:outline-none focus:shadow-outline-purple"
            @click="toggleTheme"
            aria-label="Toggle color mode"
          >
            <SunIcon v-if="theme === 'dark'" class="w-5 h-5" aria-hidden="true" />
            <MoonIcon v-else class="w-5 h-5" aria-hidden="true" />
          </button>
        </li>
        <!-- Notifications menu -->
        <li class="relative">
          <button
            class="relative align-middle rounded-md focus:outline-none focus:shadow-outline-purple"
            aria-label="Notifications"
            aria-haspopup="true"
            @click="handleNotificationsClick"
          >
            <BellIcon class="w-5 h-5" aria-hidden="true" />

            <span
              aria-hidden="true"
              class="absolute top-0 right-0 inline-block w-3 h-3 transform translate-x-1 -translate-y-1 bg-red-600 border-2 border-white rounded-full dark:border-gray-800"
            ></span>
          </button>

          <Dropdown
            align="right"
            :isOpen="isNotificationsMenuOpen"
            :onClose="handleNotificationsClick"
          >
            <DropdownItem tag="a" href="#" class="justify-between">
              <span>Messages</span>
              <Badge type="danger">13</Badge>
            </DropdownItem>
            <DropdownItem tag="a" href="#" class="justify-between">
              <span>Sales</span>
              <Badge type="danger">2</Badge>
            </DropdownItem>
            <DropdownItem @click="() => showAlert('Alert!')">
              <span>Alerts</span>
            </DropdownItem>
          </Dropdown>
        </li>

        <!-- Profile menu -->
        <li class="relative">
          <button
            class="rounded-full focus:shadow-outline-purple focus:outline-none"
            @click="handleProfileClick"
            aria-label="Account"
            aria-haspopup="true"
          >
            <Avatar
              class="align-middle"
              src="https://images.unsplash.com/photo-1502378735452-bc7d86632805?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&s=aa3a807e1bbdfd4364d1f449eaa96d82"
              alt=""
              aria-hidden="true"
            />
          </button>
          <Dropdown align="right" :isOpen="isProfileMenuOpen" :onClose="handleProfileClick">
            <DropdownItem tag="a" href="#">
              <OutlinePersonIcon class="w-4 h-4 mr-3" aria-hidden="true" />
              <span>Profile</span>
            </DropdownItem>
            <DropdownItem tag="a" href="#">
              <OutlineCogIcon class="w-4 h-4 mr-3" aria-hidden="true" />
              <span>Settings</span>
            </DropdownItem>
            <DropdownItem @click="() => showAlert('Log out!')">
              <OutlineLogoutIcon class="w-4 h-4 mr-3" aria-hidden="true" />
              <span>Log out</span>
            </DropdownItem>
          </Dropdown>
        </li>
      </ul>
    </div>
  </header>
</template>
