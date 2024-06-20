<template>
  <button class="start-button" @click="fetchHealthCategories">시작하기</button>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
        healthCategories: [],
    }
  },
  methods: {
    async fetchHealthCategories() {
      try {
        const response = await axios.get(
          "http://10.10.51.12:8765/api/health_categories"
        );
        if (response.data.status === "success") {
          this.healthCategories = response.data.data;
          this.$emit("categories-loaded", this.healthCategories);
          this.$emit("start");
        } else {
          console.error("Error fetching data:", response.data.message);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },
  },
};
</script>

<style scoped>
.start-button {
  background-color: #ccbde6;
  border: none;
  color: white;
  padding: 15px 24px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 24px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
  border-radius: 12px;
  font-weight: 1000;
  font-family: MangoDdobak;
}

.start-button:hover {
  background-color: white;
  color: black;
  border: 2px solid #ccbde6;
  border-radius: 12px;
}
</style>
