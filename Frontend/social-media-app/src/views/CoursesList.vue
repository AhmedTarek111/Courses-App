<template>
    <div class="container mt-5">
      <div class="row">
        <div class="col-4">
          <CoursesFilter />
        </div>
        <div class="col-8">
          <!-- Add content for the course list -->
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import CoursesFilter from '../components/Filter.vue';
  
  export default {
    name: 'course-list',
    components: {
      CoursesFilter, 
    },
  }
  </script>
  
  <style>
  </style>
  