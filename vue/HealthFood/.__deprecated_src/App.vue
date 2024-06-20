<template>
  <div id="app">
    <img alt="Predict Health logo" src="./assets/bg_predict.png" width="500" />
    <InitialPage v-if="stageInt == 0" msg="건기식 DB 데모" />
    <StartButton  @start="getStarted" />
  </div>
</template>

<script>
import InitialPage from "./components/InitialPage.vue";
import StartButton from "./components/StartButton.vue";
// import CategoryPage from "./components/CategoryPage.vue";

export default {
  name: "App",
  components: {
    InitialPage,
    StartButton,
    // CategoryPage,
  },
  data() {
    return {
      stageInt: 0,
    };
  },
  methods: {
    getStarted() {
      this.stageInt = 1;
    },
    selectCetegory() {
      this.stageInt = 1;
    },
  },
};
</script>

<style>
@font-face {
  font-family: "MangoDdobak";
  src: url("~@/assets/fonts/MangoDdobak-R(ttf).ttf");
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
  src: url("~@/assets/fonts/KoPub Dotum Medium.ttf");
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
