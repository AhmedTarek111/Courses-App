<template>
    <div class="container mt-5">
      <div class="row">
        <div class="col-4">
          <CoursesFilter />
        </div>
        <div class="col-8">
          <ListCourses/>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import CoursesFilter from '../components/Filter.vue';
  import ListCourses from '@/components/ListCourses.vue';
  export default {
    name: 'courses',
    components: {
      CoursesFilter, 
      ListCourses
    },

  }
  </script>
  
  <style>
  </style>
  