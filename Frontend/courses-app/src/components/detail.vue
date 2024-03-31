<template>
  <head>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  </head>
  <body>
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
          <p class="d-inline-flex gap-1">
            <button class="btn btn-primary ms-4" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
              Add Review
            </button>
          </p>
          <div class="collapse" id="collapseExample">
            <div class="card card-body">
              <form>
                <div class="mb-3">
                  <label for="exampleInputEmail1" class="form-label">Review</label>
                  <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="reveiw" v-model="review">
                  <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                </div>
                <div>
                  <div class="mb-3 form-check">
                    <select class="form-select" aria-label="Default select example" v-model="selectedRate">
                      <option :value="x" v-for="x in 5" :key="x">{{ x }}</option>
                    </select>
                  </div>
                </div>
           
                <button type="submit" class="btn btn-success" @click="addreview(review ,selectedRate)">Submit</button>
                <div v-if="message" class="alert alert-success" role="alert" mt-3>
                  {{ message }}
                </div>
              </form>
            </div>
          </div>
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
        <div v-if="reviewdeletemessage" class="alert alert-success mt-2" role="alert" mt-3>
          {{ reviewdeletemessage }}
        </div>
        <ul class="list-group">
          <li class="my-2 list-group-item" v-for="review in details.reviews" :key="review.id">
            <div class="d-flex justify-content-between">
              <!-- reveiw  -->
              <div>{{ review.review }}</div>

              <!-- rating -->
              <div>
                <i v-if="review.rate > 0" class="star fas fa-star"></i>
                <i v-else class="star fa-regular fa-star"></i>
                <span class="rating" v-for="n in 4">
                  <i v-if="review.rate > n" class="star fas fa-star"></i>
                  <i v-else class="star fa-regular fa-star"></i>
                </span>
              </div>  
              
              <div class="d-flex">
                <div class="mt-2">{{ review.user }} </div>
                <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="reivewId = review.id">
                  <img src="../assets/img/trash-solid.svg" alt="" width="15px" class="ms-2">
                </button>
              </div>  

              <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                      <span class="d-block">Are you sure you want to delete the review?</span>
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                      <button type="button" class="btn btn-danger" @click="deletereview(reivewId)" data-bs-dismiss="modal">Yes</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </body>
  
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
            details: null,
            user:'',
            message: '',
            reviewdeletemessage:'',
            reivewId:null
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
        },
        addreview(review,selectedRate){
          axios({
            url:`http://127.0.0.1:8000/courses/create&delete/review/${this.details.id}/`,
            method:'post',
            data:{
              review:review,
              rate:selectedRate,
              user_id: this.user.id
            }
          }).then(
          response => {
          this.message = 'Review added successfully!';
          this.coursedetail(); 
          this.review = ''
          this.rate=1
          setTimeout(() => {
            this.message = '';
          }, 3000); 
        })
        },
        deletereview(reviewid){
          axios({
            url:`http://127.0.0.1:8000/courses/create&delete/review/${reviewid}/`,
            method:'delete'
          }).then(response => {
            this.coursedetail()
            this.reviewdeletemessage = 'Review Deleted successfully!';
            this.reivewId =null
            setTimeout(() => {
            this.reviewdeletemessage = '';
          }, 3000); 
          

          })
        }
    },

 mounted(){
    this.coursedetail
 }
}
</script>
