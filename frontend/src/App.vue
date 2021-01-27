<template>
  <div id="app">
    <login/>
    <router-view/>
  </div>
</template>

<script>
import Login from '@/views/Login'
export default {
  components: { Login },
  name: 'App'
}
</script>