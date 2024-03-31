<template>
    <Navbar/>
    <div>
      <div class="container">
        <div class="text-center my-3 me-3">
          <span class="fs-2 text fw-light badge text-bg-success"> Add course</span>
        </div>
        <form @submit.prevent="submitForm">
          <!-- name input -->
          <div class="input-group mb-3">
            <span class="input-group-text" id="inputGroup-sizing-default">Name</span>
            <input type="text" class="form-control" v-model="courseData.name" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
          </div>
          <!-- subtitle input -->
          <div class="input-group mb-3">
            <span class="input-group-text" id="inputGroup-sizing-default">Subtitle</span>
            <input type="text" class="form-control" v-model="courseData.subtitle" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
          </div>
          <!-- Description input -->
          <div class="input-group mb-3">
            <span class="input-group-text" id="inputGroup-sizing-default">Description</span>
            <input type="text" class="form-control" v-model="courseData.description" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
          </div>
          <!-- price input -->
          <div class="input-group mb-3">
            <span class="input-group-text">price</span>
            <input type="text" class="form-control" v-model="courseData.price" aria-label="Amount (to the nearest dollar)">
            <span class="input-group-text">$</span>
          </div>
          <!-- category -->
          <div class="input-group mb-3">
            <label class="input-group-text" for="inputGroupSelect01">Categories</label>
            <select class="form-select" id="inputGroupSelect01" v-model="courseData.category">
              <option selected disabled>Choose...</option>
              <option v-for="category in categories" :value="category.id">{{ category.name }}</option>
            </select>
          </div>
          <!-- Image input -->
          <div class="mb-3">
            <label for="formFileSm" class="form-label">Image</label>
            <input class="form-control form-control-sm" id="formFileSm" type="file" @change="handleFileUpload">
          </div>
          <!-- submit button -->
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </template>
  
<script>
import Navbar from '../components/navbar.vue';
import axios from 'axios';

export default {
  name: 'createCourse',
  components: {
    Navbar
  },
  data() {
    return {
      courseData: {
        name: '',
        subtitle: '',
        description: '',
        price: '',
        image: null,
        category: null
      },
      categories: [],
    };
  },
  methods: {
    handleFileUpload(event) {
      this.courseData.image = event.target.files[0];
    },
    submitForm() {
      
      const formData = new FormData();
      formData.append('name', this.courseData.name);
      formData.append('subtitle', this.courseData.subtitle);
      formData.append('description', this.courseData.description);
      formData.append('price', this.courseData.price);
      formData.append('category', this.courseData.category);
      formData.append('image', this.courseData.image);

      axios.post('http://127.0.0.1:8000/courses/createCourse/', formData)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    },
    listCategories() {
      axios.get('http://127.0.0.1:8000/courses/categories/')
        .then(response => {
          this.categories = response.data.results;
        })
        .catch(error => {
          console.error(error);
        });
    },

  },
  mounted() {
    this.listCategories();
  }
}
</script>
