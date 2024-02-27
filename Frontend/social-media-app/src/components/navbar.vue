<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid ms-5">
          <a class="navbar-brand" href="#">
            <img src="../assets/img/udemy.svg" alt="Bootstrap" width="91" height="34">
          </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">      
                   
              <li class="nav-item">
                <a class="nav-link navLink" href="#" >Categories</a>
              </li>
            </ul>
            <div class="container-fluid">
              <form class="d-flex" role="search">
                <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" style="width: 60%;">
              </form>
            </div>
          
            
            
          </div>
        </div>
      </nav>
        

</template>
<script>
export default {
    name:'navbar',
    
}
</script>

<style>

.navLink:hover {
  color: #5624d0 !important; 
}

</style>