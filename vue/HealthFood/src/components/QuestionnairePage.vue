<template>
  <h1 style="font-size: 40px">설문 문항</h1>
  <div class="survey-container">
    <ul>
      <li
        v-for="(question, index) in questionnaires"
        :key="index"
        class="survey-question"
      >
        <div class="question-text">{{ question[1] }}</div>
        <div class="radio-buttons">
          <input
            type="radio"
            :id="'yes' + index"
            :name="'answer' + index"
            :value="true"
            v-model="answers[index]"
          />
          <label :for="'yes' + index">예</label>
          <input
            type="radio"
            :id="'no' + index"
            :name="'answer' + index"
            :value="false"
            v-model="answers[index]"
          />
          <label :for="'no' + index">아니오</label>
        </div>
      </li>
    </ul>
    <button class="complete-button" @click="checkAndSubmit">설문 완료</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["questionnaires"],
  data() {
    return {
      answers: new Array(this.questionnaires.length).fill(null),
    };
  },
  methods: {
    async submitQuestionnaires() {
      try {
        // Extract the indices from the questionnaires
        const indices = this.questionnaires.map((quest) => quest[0]);

        // Create a map to store the count of yes and no for each unique id
        const countMap = {};

        indices.forEach((id, index) => {
          if (!countMap[id]) {
            countMap[id] = { id: id, yes: 0, no: 0 };
          }
          if (this.answers[index] === true) {
            countMap[id].yes += 1;
          } else if (this.answers[index] === false) {
            countMap[id].no += 1;
          }
        });

        // Convert the countMap to an array
        const structuredData = Object.values(countMap);

        const response = await axios.post(
          "http://10.10.51.12:8765/api/submit_questionnaires",
          { answers: structuredData }
        );

        if (response.data.status === "success") {
          this.materials = response.data.data;
          console.log("Questionnaires submitted successfully");
          this.$emit("materials-loaded", this.materials);
          this.$emit("questionnaire-sent");
        } else {
          alert("요청 실패. 홈으로 이동하세요")
          console.error(
            "Error submitting questionnaires:",
            response.data.message
          );
        }
      } catch (error) {
        console.error("Error submitting questionnaires:", error);
      }
    },

    checkAndSubmit() {
      // 모든 문항이 선택되었는지 확인
      // console.log("Answers:", this.answers);
      // this.answers.forEach((answer, index) => {
      //   console.log(`Index ${index}: Value: ${answer}, Type: ${typeof answer}`);
      // });
      if (
        this.answers.some(
          (answer) => answer === undefined || answer === null || answer === ""
        )
      ) {
        alert("모든 항목을 선택해야 합니다!");
      } else {
        // Confirm dialog 띄우기
        if (confirm("선택하신 항목으로 설문을 제출하시겠습니까?")) {
          this.submitQuestionnaires();
        }
      }
    },
  },
};
</script>

<style scoped>
.survey-container {
  max-width: 1000px; /* 좌우 폭을 조정합니다 */
  margin: 0 auto; /* 가운데 정렬합니다 */
  font-size: 20px;
  font-family: Dotum;
}

.survey-question {
  display: flex;
  align-items: center; /* 설문 질문과 라디오 버튼을 수직으로 중앙 정렬합니다. */
  margin-bottom: 15px; /* 설문 항목 간의 간격을 조정합니다. */
}

.question-text {
  flex-grow: 1; /* 설문 질문이 가능한 최대 크기로 확장됩니다. */
  text-align: left; /* 설문 질문 텍스트를 왼쪽으로 정렬합니다. */
}

.radio-buttons {
  display: flex;
  margin-left: 40px;
  min-width: 150px;
}

.radio-buttons input[type="radio"] {
  margin-right: 5px; /* 라디오 버튼 사이의 간격을 조정합니다. */
}

.complete-button {
  background-color: #ccbde6;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 20px;
  margin-top: 20px;
  cursor: pointer;
  border-radius: 12px;
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
