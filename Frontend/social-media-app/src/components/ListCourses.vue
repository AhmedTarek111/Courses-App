<template>
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body>
  
  <div>
    <div class="row border-bottom border-top border-3 my-2" v-for="course in courses" :key="course.id">
      <!-- Course Details -->
      <div class="col-4">
        <a :href="'edit/'+course.id"><img :src="course.image" alt="" class="img-fluid my-2"></a>
      </div>
      <div class="col-6 my-auto">
        <h4>{{ course.name }}</h4>
        <p>{{ course.description }}</p>
        <span class="d-block mb-1">{{ course.user }}</span>
        <!-- Rating -->
        ({{ course.avgrate }})
        <i v-if="course.avgrate > 0" class="star fas fa-star"></i>
        <i v-else class="star fa-regular fa-star"></i>
        <span class="rating" v-for="n in 4">
          <i v-if="course.avgrate > n" class="star fas fa-star"></i>
          <i v-else class="star fa-regular fa-star"></i>
        </span>
        ({{ course.total_reviews }})
      </div>
      <!-- Price and Link -->
      <div class="col-2 mt-4">
        <b>Price: {{ course.price }}$</b>
        <a :href="'edit/'+course.id" class="text-decoration-none"><i class="fa-solid fa-circle-info d-block ms-5 mt-5" style="color: #A435F0;"></i></a>
      </div>
    </div>
  </div>

</body>
</template>

<script>
import axios from 'axios';

export default {
  name: "ListCourses",
  props: ['filters','sort','category'],
  data() {
    return {
      courses: [],
    };
  },
  methods: {

    listCourses() {
      axios.get('http://127.0.0.1:8000/courses/')
        .then(response => {
          this.courses = response.data.results;
        })
        
    },
  },
  watch: {
    filters: {
      handler(newValue) {
        
        this.courses = newValue.results || [];
      },
      immediate: false, 
    },

    sort: {
      handler(newValue) {
        
        this.courses = newValue.results || [];
      },
      immediate: false, 
    },

    category: {
      handler(newValue) {
        
        this.courses = newValue || [];
      },
      immediate: false, 
    },

  },
  mounted(){
   this.listCourses()
  }
};
</script>


<style>
.star {
  color: rgb(238, 238, 7);
  border-color: black;
}
</style>
