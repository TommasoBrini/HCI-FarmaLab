import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import RemoveItemView from '@/views/RemoveItemView.vue'
import HomeView from '@/views/HomeView.vue'
import AddItemView from '@/views/AddItemView.vue'
import ItemDetailsView from '@/views/ItemDetailsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/add-item',
      name: 'add-item',
      component: AddItemView
    },
    {
      path: '/remove-item/:id',
      name: 'remove-item',
      component: RemoveItemView
    },
    {
      path: '/item-details/:id',
      name: 'item-details',
      component: ItemDetailsView
    }
  ]
})

export default router