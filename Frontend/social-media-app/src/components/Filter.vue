<template>
  
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
     <div class="dropdown mt-3">
       <button class="btn dropdown-toggle " type="button" data-bs-toggle="dropdown" style="background-color: #A435F0; color:white;">
           Sort 
       </button>
       <!-- name filter a -> z -->
       <ul class="dropdown-menu mt-2">
         <div class="btn-group-vertical ms-2" role="group" aria-label="Vertical radio toggle button group">
           <li class="mt-3">
              
               <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio1" autocomplete="off" @click="sort('-name')" >
               <label class="fillter-button" for="vbtn-radio1">name(a-z)</label>
             </li>
             <li>  
               <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio2" autocomplete="off" @click="sort('name')">
               <label class="fillter-button" for="vbtn-radio2">name(z-a)</label>
             </li> 
             <!-- end name -->
     
             <!-- price filter high -> low -->    
             <li>
               <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio3" autocomplete="off" @click="sort('-price')" >
               <label class="fillter-button" for="vbtn-radio3">price <img src="../assets/img/arrow-up-solid.svg" width="15px" height="15px" class="ms-2 me-2"></label>
             </li>  
             <!-- price filter low -> high -->    
             <li>
               <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio4" autocomplete="off" @click="sort('price')">
               <label class="fillter-button" for="vbtn-radio4">price <img src="../assets/img/arrow-down-solid.svg" width="15px" height="15px" class="ms-2 me-2"></label>
             </li>
             </div>
             <!-- end price  -->
       </ul>
     </div>
    <div class="dropdown ms-2 mt-3">
      <button class="btn dropdown-toggle " type="button" data-bs-toggle="dropdown" style="background-color: #A435F0; color:white;" @click="listcategories">
        Categories 
      </button>
      <!-- name filter a -> z -->
      <ul class="dropdown-menu mt-2">
        <div class="btn-group-vertical ms-2" role="group" aria-label="Vertical radio toggle button group">
          <li class="mt-3" v-for="(category, index) in categories" :key="index">
            <input type="radio" class="btn-check" :name="'vbtn-radio' + index" :id="'vbtn-radio' + index" autocomplete="off">
            <label class="fillter-button" :for="'vbtn-radio' + index">{{ category.name }}</label>
          </li>
        </div>
      </ul>        
          <!-- end name -->
  
          <!-- price filter high -> low -->

  </div>
   </div>
  
        
          <!-- end name -->
  
          <!-- price filter high -> low -->
  
  
  
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
      categories:[]
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
    },

    watch:{
      sortfilter(newvalue){
        this.$emit('applysort',this.sortfilter)
      }
    },
    
  }
}
</script>


<style>
.fillter-button  {
  color: white;
  background-color:  #A435F0;
  padding: 10px 15px;
  margin-top: 5px;
  border-radius: 15px;
  border: solid #bb67f3;
  cursor: pointer;

}

</style>

