<template>
  <div id="app">
    <navbar/>
  </div>
  
  <div>
    <router-view />
  </div>
</template>

<script>
import CoursesList from './views/CoursesList.vue';
import navbar from './components/navbar.vue';

export default {
  name: 'app',
  components: {
    navbar,
    CoursesList,
  }
}
</script>

<style>
/* Add any necessary styling */
</style>
