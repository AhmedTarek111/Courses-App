<template>
  
  <button class="btn btn-primary py-3 px-4" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasExample" aria-controls="offcanvasExample" style="background-color: #A435F0;">
    Fillters
  </button>
  
  <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel">
    <div class="offcanvas-header">
      <h5 class="offcanvas-title" id="offcanvasExampleLabel">Offcanvas</h5>
      <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
    </div>
    <div class="offcanvas-body">
     <!-- search  -->
      <div class="d-flex mb-3">
        <input type="text" placeholder="search" class="form-control" name="search" v-model="searchinput">
        <button class="btn ms-2 " style="background-color: #A435F0; color:white;" @click="searchMethod(searchinput)">search</button>
      </div>
    <!-- fillters  -->
      <div class="dropdown mt-3">
        <button class="btn  dropdown-toggle" type="button" data-bs-toggle="dropdown" style="background-color: #A435F0; color:white;">
          Filters
        </button>
        <!-- name filtter a -> z -->
        <ul class="dropdown-menu">
          <li class="mt-3">
              <label class="ms-2" for="name(a-z)">name(a-z)</label>
              <input type="checkbox" name="name" id="name(a-z)" class="ms-5">
          </li>
          
          <li class="mt-3">      
              <label class="ms-2" for="name(z-a)">name(z-a)</label>
              <input type="checkbox" name="-name" id="name(z-a)" class="ms-5">
          </li>
          <!-- end name  -->

        <!-- price filtter high -> low  -->

          <li class="mt-3">
              <label class="ms-2" for="price">price</label>
              <img src="../assets/img/arrow-up-solid.svg" width="15px" height="15px" class="ms-2 me-2"></img>
              <input type="checkbox" name="price" id="name(a-z)" class="ms-5">
          </li>

          <li class="mt-3">
              <label class="ms-2" for="-price">price</label>
              <img src="../assets/img/arrow-down-solid.svg" width="15px" height="15px" class="ms-2 me-2" style="color: #A435F0;"></img>
              <input type="checkbox" name="-price" id="-price" class="ms-5">
          </li>
          <!-- end price fillters -->
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CoursesFilter',
  emits: ['updateCourses'],
  data() {
    return {
      searchinput: '',
    };
  },
  methods: {
    searchMethod() {
      if (this.searchinput.length > 0) {
        axios.get(`http://127.0.0.1:8000/courses/?search=${this.searchinput}`)
          .then(response => {
            this.$emit('updateCourses', response.data);
          })
          .catch(error => {
            console.error('Error fetching search result:', error);
          });
      }
    },
  },
};
</script>



