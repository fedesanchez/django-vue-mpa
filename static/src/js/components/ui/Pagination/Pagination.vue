<script setup>
import NavigationButton from './NavigationButton.vue'
import PageButton from './PageButton.vue'
import theme from '@/themes/default'
const { pagination } = theme
const baseStyle = pagination.base
const MAX_VISIBLE_PAGES = 7

function getPages(activePage, totalPages) {
  let newPages = []
  if (totalPages <= MAX_VISIBLE_PAGES) {
    newPages = Array.from({ length: totalPages }).map((_, i) => i + 1)
  } else if (activePage < 5) {
    // #1 activePage < 5 -> show first 5
    newPages = [1, 2, 3, 4, 5, '...', totalPages]
  } else if (activePage >= 5 && activePage < totalPages - 3) {
    // #2 activePage >= 5 && < totalPages - 3
    newPages = [1, '...', activePage - 1, activePage, activePage + 1, '...', totalPages]
  } else {
    // #3 activePage >= totalPages - 3 -> show last
    newPages = [
      1,
      '...',
      totalPages - 4,
      totalPages - 3,
      totalPages - 2,
      totalPages - 1,
      totalPages
    ]
  }
  return newPages
}

const props = defineProps({
  has_previous: Boolean,
  previous_page_number: Number,
  active_page: Number,
  has_next: Boolean,
  next_page_number: Number,
  start_index: Number,
  end_index: Number,
  num_pages: Number,
  per_page: Number,
  count: Number
})

const pages = getPages(props.active_page, props.num_pages)

</script>

<template>
  <div :class="baseStyle">
    <span class="flex items-center font-semibold tracking-wide uppercase">
      Showing {{ start_index }} -
      {{ end_index }} of {{ count }}
    </span>

    <div class="flex mt-2 sm:mt-auto sm:justify-end">
      <nav>
        <ul class="inline-flex items-center">
          <li>
            <NavigationButton
              directionIcon="prev"
              :disabled="!has_previous"
              :href="has_previous? '?page=' + previous_page_number: ''"              
            />
          </li>

          <li v-for="(page, index) in pages" :key="index">
            <template v-if="page === '...'">
              <span class="px-2 py-1">...</span>
            </template>
            
            <template v-else>
              <PageButton
                :page="page"
                :isActive="page === active_page"
                :href="'?page=' + page"            
              />
            </template>
          </li>

          <li>
            <NavigationButton
              directionIcon="next"
              :disabled="!has_next"
              :href="has_next ? '?page=' + next_page_number : ''"
            />
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>
