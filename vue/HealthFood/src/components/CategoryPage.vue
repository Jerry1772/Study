<template>
  <div>
    <h1>설문 페이지</h1>
    <div class="category-container" v-if="healthCategories.length > 0">
      <h2>건강 유형 선택</h2>
      <p>관심 있는 건강유형을 선택해주세요</p>
      <div class="category-list">
        <button
          v-for="category in healthCategories"
          :key="category"
          class="category-button"
          @click="fetchQuestionnaires(category)"
        >
          {{ category }}
        </button>
      </div>
    </div>
    <div v-else>
      <p>데이터를 불러오는 중입니다...</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      questionnaires: [],
    };
  },
  props: ["healthCategories"],
  methods: {
    async fetchQuestionnaires(category) {
      try {
        const response = await axios.get(
          `http://10.10.51.12:8765/api/questionnaires?category=${encodeURIComponent(
            category
          )}`
        );
        if (response.data.status === "success") {
          this.questionnaires = response.data.data;
          this.$emit("questionnaire-loaded", this.questionnaires);
          this.$emit("category-selected");
        } else {
          console.error(
            "Error fetching questionnaires:",
            response.data.message
          );
        }
      } catch (error) {
        console.error("Error fetching questionnaires:", error);
      }
    },
  },
};
</script>

<style scoped>
.category-container {
  max-width: 1000px;
  margin: 0 auto;
}
.category-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  align-items: flex-start;
  margin-top: 20px;
}

.category-button {
  background-color: #ccbde6;
  border: none;
  color: white;
  width: 240px;
  height: 50px;
  text-align: center;
  text-decoration: none;
  font-size: 20px;
  cursor: pointer;
  border-radius: 8px;
  transition-duration: 0.3s;
  font-family: MangoDdobak;
}

.category-button:hover {
  background-color: #45a049;
}
</style>


