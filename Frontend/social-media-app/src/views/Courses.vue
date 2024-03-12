<template>  
  <Navbar/>
  <div class="container mt-5">
    <div class="row">
      <div class="col-4">
        <CoursesFilter @updateCourses="updateCourses" @applysort="applysort" @applycategoryfilter="applycategoryfilterr"/>
      </div>
      <div class="col-8">
        <ListCourses :filters="filteredCourses" :sort="sortfillter" :category="categoryfilter"/>
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
  data() {
    return {
      filteredCourses: [],
      sortfillter:[],
      categoryfilter:[]
    };
  },
  methods: {
    updateCourses(result) {
      this.filteredCourses = result;
    },

    applysort(sort){
      this.sortfillter =sort
    },

    applycategoryfilterr(categories){
     this.categoryfilter = categories;
     console.log(`you are in the courses and the data is ${categories}`)
    }
  },
};
</script>


<style>
</style>
