<script setup>
import { ref, watch, reactive } from 'vue'
import NavigationButton from './NavigationButton.vue'
import PageButton from './PageButton.vue'
import theme from '@/themes/default'
const { pagination } = theme
const baseStyle = pagination.base

const props = defineProps({
  totalResults: Number,
  resultsPerPage: Number,
  label: String,
  onChange: Function
})

const { totalResults, resultsPerPage = 10, label, onChange } = props
const state = reactive({
  pages: [],
  activePage: 1
})
//const pages = ref([])
//const pagesRefs = ref([]) //https://vuejs.org/guide/essentials/template-refs#refs-inside-v-for
//const activePage = ref(1)

const TOTAL_PAGES = Math.ceil(totalResults / resultsPerPage)
const FIRST_PAGE = 1
const LAST_PAGE = TOTAL_PAGES
const MAX_VISIBLE_PAGES = 7

function handlePreviousClick() {
  setActivePage(state.activePage - 1)
}

function handleNextClick() {
  setActivePage(state.activePage + 1)
}

function setPages(activePage) {
  let newPages = []
  if (TOTAL_PAGES <= MAX_VISIBLE_PAGES) {
    newPages = Array.from({ length: TOTAL_PAGES }).map((_, i) => i + 1)
  } else if (activePage < 5) {
    // #1 active page < 5 -> show first 5
    newPages = [1, 2, 3, 4, 5, '...', TOTAL_PAGES]
  } else if (activePage >= 5 && activePage < TOTAL_PAGES - 3) {
    // #2 active page >= 5 && < TOTAL_PAGES - 3
    newPages = [1, '...', activePage - 1, activePage, activePage + 1, '...', TOTAL_PAGES]
  } else {
    // #3 active page >= TOTAL_PAGES - 3 -> show last
    newPages = [
      1,
      '...',
      TOTAL_PAGES - 4,
      TOTAL_PAGES - 3,
      TOTAL_PAGES - 2,
      TOTAL_PAGES - 1,
      TOTAL_PAGES
    ]
  }
  state.pages = newPages
}

function setActivePage(page) {
  state.activePage = page
}

watch(state, () => {
  onChange(state.activePage)
  //setPages(state.activePage)
})

//Initialize pages
setPages(state.activePage)
</script>

<template>
  <div :class="baseStyle">
    <span class="flex items-center font-semibold tracking-wide uppercase">
      Showing {{ state.activePage * resultsPerPage - resultsPerPage + 1 }}-
      {{ Math.min(state.activePage * resultsPerPage, totalResults) }} of {{ totalResults }}
    </span>

    <div class="flex mt-2 sm:mt-auto sm:justify-end">
      <nav :aria-label="label">
        <ul class="inline-flex items-center">
          <li>
            <NavigationButton
              directionIcon="prev"
              :disabled="state.activePage === FIRST_PAGE"
              @click="handlePreviousClick"
            />
          </li>

          <li v-for="(page, index) in state.pages" :key="index">
            <template v-if="page === '...'">
              <span class="px-2 py-1">...</span>
            </template>
            <template v-else>
              <PageButton
                :page="page"
                :isActive="page === state.activePage"
                @click="() => setActivePage(+page)"
              />
            </template>
          </li>

          <li>
            <NavigationButton
              directionIcon="next"
              :disabled="state.activePage === LAST_PAGE"
              @click="handleNextClick"
            />
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>
