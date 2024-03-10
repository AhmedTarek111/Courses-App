<template>  
  <Navbar/>
  <div class="container mt-5">
    <div class="row">
      <div class="col-4">
        <CoursesFilter @updateCourses="updateCourses" @applysort="applysort"/>
      </div>
      <div class="col-8">
        <ListCourses :filters="filteredCourses" :sort="sortfillter"/>
      </div>
    </div>
  </div>
</template>

<script>
import CoursesFilter from '../components/Filter.vue';
import ListCourses from '@/components/ListCourses.vue';
import Navbar from '../components/navbar.vue';

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
      sortfillter:[]
    };
  },
  methods: {
    updateCourses(result) {
      this.filteredCourses = result;
    },

    applysort(sort){
      this.sortfillter =sort
    },
  },
};
</script>


<style>
</style>
