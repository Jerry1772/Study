<template>
  <div>
    <div>
      <h1>건강유형 선택</h1>
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
    <div v-if="showQuestionnaires">
      <h1>설문</h1>
      <ul>
        <li v-for="(question, index) in questionnaires" :key="index">
          {{ question }}
          <input
            type="radio"
            id="yes"
            name="answer"
            value="yes"
            v-model="answers[index]"
          />
          <label for="yes">예</label>
          <input
            type="radio"
            id="no"
            name="answer"
            value="no"
            v-model="answers[index]"
          />
          <label for="no">아니오</label>
        </li>
      </ul>
      <button class="complete-button" @click="submitQuestionnaires">
        설문 완료
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CategoryPage",
  data() {
    return {
      healthCategories: [],
      showList: false,
      showQuestionnaires: false,
      questionnaires: [],
      answers: [],
    };
  },
  methods: {
    async fetchHealthCategories() {
      try {
        const response = await axios.get(
          "http://10.10.51.12:8765/api/health_categories"
        );
        if (response.data.status === "success") {
          this.healthCategories = response.data.data;
          this.showList = true;
          this.$emit("start"); // Emit event to hide HelloWorld
        } else {
          console.error("Error fetching data:", response.data.message);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },
    async fetchQuestionnaires(category) {
      try {
        const response = await axios.get(
          `http://10.10.51.12:8765/api/questionnaires?category=${encodeURIComponent(
            category
          )}`
        );
        if (response.data.status === "success") {
          this.questionnaires = response.data.data;
          this.showQuestionnaires = true;
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
    async submitQuestionnaires() {
      try {
        const response = await axios.post(
          "http://10.10.51.12:8765/api/submit_questionnaires",
          { answers: this.answers }
        );
        if (response.data.status === "success") {
          console.log("Questionnaires submitted successfully");
        } else {
          console.error(
            "Error submitting questionnaires:",
            response.data.message
          );
        }
      } catch (error) {
        console.error("Error submitting questionnaires:", error);
      }
    },
  },
};
</script>

<style scoped>
.category-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  margin-top: 20px;
}

.category-button {
  background-color: #ccbde6; /* Medium Light Green */
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  font-size: 14px;
  cursor: pointer;
  border-radius: 8px;
  transition-duration: 0.3s;
  font-family: MangoDdobak;
}

.category-button:hover {
  background-color: #45a049;
}

.complete-button {
  background-color: #ccbde6; /* Medium Light Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 20px;
  margin-top: 20px;
  cursor: pointer;
  border-radius: 12px; /* Rounded corners */
  font-family: MangoDdobak;
}

.complete-button:hover {
  background-color: #45a049;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}
</style>
