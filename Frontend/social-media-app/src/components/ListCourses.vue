<template>
  <div>
    <div class="row border-bottom border-top" v-for="course in courses" :key="course.id">
      <div class="col-4">
        <a :href="'edit/'+course.id"><img :src="course.image" alt="" class="img-fluid"></a>
      </div>
      <div class="col-6 my-auto">
        <h4>{{ course.name }} </h4>
        <p>{{ course.description }}</p>
        <span class="d-block mb-1">{{ course.user }}</span>
        <!-- rating -->
        ({{ course.avgrate }})
        <i v-if="course.avgrate > 0" class="star fas fa-star"></i>
        <i v-else class="star fa-regular fa-star"></i>
        <span class="rating" v-for="n in 4">
        
          <i v-if="course.avgrate  > n" class="star fas fa-star"></i>
          <i v-else class="star fa-regular fa-star"></i>
        </span>
        ({{ course.total_reviews }})
      </div>
      <div class="col-2 mt-4">
        <b>Price: {{ course.price }}$</b>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "ListCourses",
  data() {
    return {
      courses: [] 
    };
  },
  methods: {
    listCourses() {
      axios.get('http://127.0.0.1:8000/courses/')
        .then(response => {
          this.courses = response.data.results; 
        })
        .catch(error => {
          console.error('Error fetching courses: ', error);
        });
    }
  },
  mounted() {
    this.listCourses(); 
  }
};
</script>

<style>
.star {
  color: rgb(238, 238, 7);
  border-color: black;
}
</style>
