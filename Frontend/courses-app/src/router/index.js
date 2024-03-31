import { createRouter, createWebHistory } from 'vue-router'
import Courses from '../views/Courses.vue'
import CourseDetail from '../views/CourseDetail.vue'
import Addcourse from  '../views/createcourse.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Courses
    },
    {
      path: '/edit/:id/',
      name: 'coursedetail',
      component: CourseDetail
    },

    {
      path: '/add/course',
      name: 'addcourse',
      component: Addcourse
     
    },

  ]
})

export default router
