<template>
  <div id="app">
    <navbar/>
  </div>
  
  <div>
    <router-view />
  </div>
</template>

<script>
import navbar from './components/navbar.vue';

export default {
  name: 'app',
  components: {
    navbar,
  }
}
</script>

<style>
/* Add any necessary styling */
</style>
