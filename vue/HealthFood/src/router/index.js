import { createRouter, createWebHistory } from 'vue-router';

import InitialPage from '../components/InitialPage.vue';
import CategoryPage from '../components/CategoryPage.vue';
import QuestionnairePage from '../components/QuestionnairePage.vue';
import MaterialPage from '../components/MaterialPage.vue';

const routes = [
  { path: '/', name: 'Initial', component: InitialPage },
  { path: '/categories', name: 'Categories', component: CategoryPage },
  { path: '/questionnaires', name: 'Questionnaires', component: QuestionnairePage },
  { path: '/materials', name: 'Materials', component: MaterialPage },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
