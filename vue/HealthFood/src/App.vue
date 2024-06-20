<template>
  <div id="app">
    <img alt="Predict Health logo" src="./assets/bg_predict.png" width="500" />
    <router-view
      @start="moveToCategoryPage"
      @categories-loaded="passCategories"
      @category-selected="moveToQuestionnairePage"
      @questionnaire-loaded="passQuestionnaires"
      @questionnaire-sent="moveToMaterialPage"
      @materials-loaded="passMaterials"
      :healthCategories="healthCategories"
      :questionnaires="questionnaires"
      :materials="materials"
    />
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      healthCategories: [],
      questionnaires: [],
      materials: [],
    };
  },
  methods: {
    moveToCategoryPage() {
      this.$router.push({ name: 'Categories' });
    },
    moveToQuestionnairePage() {
      this.$router.push({ name: 'Questionnaires' });
    },
    moveToMaterialPage() {
      this.$router.push({ name: 'Materials'});
    },
    passCategories(categories) {
      this.healthCategories = categories;
    },
    passQuestionnaires(questionnaires) {
      this.questionnaires = questionnaires;
    },
    passMaterials(materials) {
      console.log(materials)
      this.materials = materials;
    }
  },
};
</script>

<style>
@font-face {
  font-family: "MangoDdobak";
  src: url("~@/assets/fonts/MangoDdobak.otf");
  font-weight: 800;
  font-style: normal;
}
@font-face {
  font-family: "Nanum";
  src: url("~@/assets/fonts/NanumBarunGothic.ttf");
  font-weight: 800;
  font-style: normal;
}
@font-face {
  font-family: "Dotum";
  src: url("~@/assets/fonts/KoPub Dotum_Pro Medium.otf");
  font-weight: 800;
  font-style: normal;
}

#app {
  font-family: MangoDdobak, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
