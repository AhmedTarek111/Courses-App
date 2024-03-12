<template>
  
  <div class="d-flex">
  <!-- sort  -->
  <button class="btn btn-primary py-3 px-4" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasExample" aria-controls="offcanvasExample" style="background-color: #A435F0;">
    Fillters
  </button> 
  <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel">
    <div class="offcanvas-header">
      <h5 class="offcanvas-title" id="offcanvasExampleLabel">filters</h5>
      <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
    </div>
    <div class="offcanvas-body">
     <!-- search  -->
      <div class="d-flex mb-3">
        <input type="text" placeholder="search" class="form-control" name="search" v-model="searchinput">
        <button class="btn ms-2 " style="background-color: #A435F0; color:white;" @click="searchMethod(searchinput)">search</button>
      </div>
    <!-- fillters  -->
    
      <div class="d-flex">
        <!-- sort  -->
        <div class="dropdown mt-3">
          <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" style="background-color: #A435F0; color:white;">
              sort
          </button>
          <!-- name filter a -> z -->
          <ul class="dropdown-menu">
            <div class="btn-group-vertical ms-2" role="group" aria-label="Vertical radio toggle button group">
              <li class="mt-3">
                 
                  <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio1" autocomplete="off" @click="sort('name')" >
                  <label class="btn btn-outline-secondary" for="vbtn-radio1">name(a-z)</label>
                </li>
                <li>  
                  <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio2" autocomplete="off" @click="sort('-name')">
                  <label class="btn btn-outline-secondary" for="vbtn-radio2">name(z-a)</label>
                </li> 
                <li>
                  <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio3" autocomplete="off" @click="sort('price')" >
                  <label class="btn btn-outline-secondary" for="vbtn-radio3">price <img src="../assets/img/arrow-up-solid.svg" width="15px" height="15px" class="ms-2 me-2"></label>
                </li>  
                <li>
                  <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio4" autocomplete="off" @click="sort('-price')">
                  <label class="btn btn-outline-secondary" for="vbtn-radio4">price <img src="../assets/img/arrow-down-solid.svg" width="15px" height="15px" class="ms-2 me-2"></label>
                </li>
                </div>
      
            
              <!-- end name -->
      
              <!-- price filter high -> low -->
      
          
          </ul>
      </div>

      <!-- filter by categories  -->
      <div class="dropdown mt-3 ms-3">
        <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" style="background-color: #A435F0; color:white;" @click="listcategories">
          categories
        </button>
        <!-- name filter a -> z -->
        <ul class="dropdown-menu">
          <div class="btn-group-vertical ms-2" role="group" aria-label="Vertical radio toggle button group">
            <li class="mt-3" v-for="category in categories">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" :value="category.name" id="flexCheckDefault" v-model="categoryfilter" :key="category.id">
                <label class="form-check-label" for="flexCheckDefault">
                  {{ category.name }}
                </label>
              </div>
              
              </li>
              
              </div>
    
          
            <!-- end name -->
    
            <!-- price filter high -> low -->
    
        
        </ul>
    </div>

      </div>
  
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
      sortfilter:'',
      categories:'',
    };
  },
  methods: {
    searchMethod() {
      if (this.searchinput.length > 0) {
        axios.get(`http://127.0.0.1:8000/courses/?search=${this.searchinput}`)
          .then(response => {
            this.$emit('updateCourses', response.data);
          })
      }
    },

    sort(sort){
      axios({
        url:`http://127.0.0.1:8000/courses/?ordering=${sort}`,
        method:'get',
      }).then(response => {this.sortfilter = response.data;})
    },

    listcategories(){
      axios({
        url:'http://127.0.0.1:8000/courses/categories/',
        method:'get',
      }).then(response => this.categories = response.data.results)
    }
  
  },

  watch:{
    sortfilter(newvalue){
      this.$emit('applysort',this.sortfilter)
    },
    categoryfilter(newValue){
      this.$emit('categoryfilter',this.categoryfilter)
    }
  }
};
</script>



