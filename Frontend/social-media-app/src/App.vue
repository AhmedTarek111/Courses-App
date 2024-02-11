
<template>
  <navbar/>
  <div class="container">
    <div class="row">
      <!-- filter -->
      <div class="col-lg-4">

      </div>
      <!-- courses -->
      <div class="col-lg-8">

      </div>
      <!--  -->
    </div>
  </div>
  <RouterView />
</template>

<style>


</style>
<script >
import { RouterLink, RouterView } from 'vue-router'
import navbar from './components/navbar.vue';
export default {
  name:'app',
  components:{
    navbar,
  }
}

</script>
