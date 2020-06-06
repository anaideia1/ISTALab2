import Vue from 'vue';
import VueRouter from 'vue-router';
import Books from '../views/Books.vue';
import Countries from '../views/Countries.vue';
import Cities from '../views/Cities.vue';
import Genres from '../views/Genres.vue';
import Authors from '../views/Authors.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'books',
    component: Books,
  },
  {
    path: '/countries',
    name: 'Countries',
    component: Countries,
  },
  {
    path: '/cities',
    name: 'Cities',
    component: Cities,
  },
  {
    path: '/genres',
    name: 'Genres',
    component: Genres,
  },
  {
    path: '/authors',
    name: 'Authors',
    component: Authors,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
