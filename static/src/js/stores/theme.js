import { ref } from 'vue'

const themeKey = 'theme'
const defaultValue = 'light'

const theme = ref(localStorage.getItem(themeKey) || defaultValue)

function setTheme(t) {
  theme.value = t
  localStorage.setItem(themeKey, t)
  updateBodyClass()
}

function toggleTheme() {
  if (theme.value === 'light') setTheme('dark')
  else setTheme('light')
}

function updateBodyClass() {
  document.body.classList[theme.value === 'dark' ? 'add' : 'remove']('dark')
}

updateBodyClass(theme)

export { theme, toggleTheme }
