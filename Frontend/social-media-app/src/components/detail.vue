<template>
    <div class="row" v-if="details">
      <div class="col-lg-6">
        <img :src="details.image" alt="" class="img-fluid">
      </div>
      <div class="col-lg-6 border border-5">
        <span class="fs-2 fw-semibold d-block mt-3">{{ details.name }}</span>
        <span class="fs-4 fst-italic d-block mb-4">{{ details.subtitle }}</span>
        <p class="fw-light bg-body-secondary border" style="max-width: 500px;">{{ details.description }}</p>
        <div class="mt-4">
          <span class="me-5 badge bg-info text-wrap">Price : {{ details.price }}</span>
          <span class="ms-5 badge bg-success text-wrap">Category : {{ details.category }}</span>
        </div>
      </div>
    </div>
    
    <div v-else>
        <p>this course not avilable (-__-) </p>
    </div>

    <div v-if="details">
        <h2 class="my-5">
          <span class="reviews rounded p-3">Reviews <span class="badge bg-light text-secondary">{{ details.reviews.length }}</span></span>
        </h2>
        <ul class="list-group">
          <li class="my-2 list-group-item" v-for="review in details.reviews" :key="review.id">
            <div class="d-flex justify-content-between align-items-start">
              <div>{{ review.review }}</div>
              <div class="text-end">{{ review.user }}</div>
              <div class="text-end">{{ user }}</div>
            </div>
          </li>
        </ul>
      </div>
      <!-- <div class="" v-if="details.user == this.$route.">
        <p>asdlkfajhsdjkfahskdlfh</p>
      </div>
       -->
  </template>
  

<style scoped>
.reviews {
    background-color: #A435F0 ;
}
</style>

<script>
import axios from 'axios';

export default {
    name: 'detail-components',
    data() {
        return {
            details: null ,
            user:''
        }
    },
    created() {
    this.coursedetail()
    },
    methods: {
        coursedetail() {
            axios({
                method: 'get',
                url: `http://127.0.0.1:8000/courses/edit_courses/${this.$route.params.id}/`,
                
            }).then(response => {
              this.details = response.data,
              this.user = response.data.user

            })
        }
    },
 mounted(){
    this.coursedetail
 }
}
</script>
