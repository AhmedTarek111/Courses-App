<template>  
  <nav class="navbar bg-body-tertiary ">
    <div class="container d-flex justify-content-center">
      <a class="navbar-brand" href="/">
        <img src="../assets/img/udemy.svg" alt="Bootstrap" width="91" height="34">
      </a>
    </div>
  </nav>
</template>

<script>

    export default {
      name: 'Navbar',
      data() {
        return {
          searchfilter: ''
        };
      },
      watch: {
        searchfilter() {
          this.$emit('updateSearchFilter', this.searchfilter);
        }
      }
    };
    </script>


<style>
.navLink:hover {
  color: #5624d0 !important; 
}
</style>
