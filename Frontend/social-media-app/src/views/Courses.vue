<template>  
  <Navbar/>
    <div class="container mt-5">
      <div class="row">
        <div class="col-4">
          <CoursesFilter  />
        </div>
        <div class="col-8">
          <ListCourses />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import CoursesFilter from '../components/Filter.vue';
  import ListCourses from '@/components/ListCourses.vue';
  import Navbar from '../components/navbar.vue';
  import axios from 'axios';
  export default {
    name: 'courses',
    components: {
      CoursesFilter, 
      ListCourses,
      Navbar
    },
  }
  </script>
  
  <style>
  </style>
  