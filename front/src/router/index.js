import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/main/Home.vue'
import Signup from '@/views/accounts/Signup.vue'
import Login from '@/views/accounts/Login.vue'
import Profile from '@/views/accounts/Profile.vue'
import Movielist from '@/views/movies/Movielist.vue'
import Moviedetail from '@/views/movies/Moviedetail.vue'
import Moviereviews from '@/views/movies/Moviereviews.vue'
import Moviereviewsdelete from '@/views/movies/Moviereviews.vue'
import Moviereviewsupdate from '@/views/movies/Moviereviewsupdate.vue'
import Moviereviewswrite from '@/views/movies/Moviereviewswrite.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'Home',
    component: Home,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/profile',
    name: 'Profile',
    component: Profile,
    props: true

  },
  {
    path: '/movies',
    name: 'Movielist',
    component: Movielist
  },
  {
    path: '/movies/:movie_pk',
    name: 'Moviedetail',
    component: Moviedetail,
    props: true
  },
  {
    path: '/movies/:movie_pk/Moviereviews/:review_pk',
    name: 'Moviereviews',
    component: Moviereviews,
    props: true
  },
  {
    path: '/movies/:movie_pk/Moviereviewsupdate/:review_pk',
    name: 'Moviereviewsupdate',
    component: Moviereviewsupdate,
    props: true
  },
  {
    path: '/movies/:movie_pk/Moviereviewsdelete/:review_pk',
    name: 'Moviereviewsdelete',
    component: Moviereviewsdelete,
    props: true
  }, 
  {
    path: '/movies/:movie_pk/Moviereviewswrite',
    name: 'Moviereviewswrite',
    component: Moviereviewswrite,
    props: true
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
