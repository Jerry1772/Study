<template>
  <div class="material-list">
    <h1 style="font-size: 40px">원료 목록</h1>
    <div v-if="materials && materials.length > 0">
      <table>
        <thead>
          <tr>
            <th class="column-category-title" @click="sortBy('category')">카테고리<span v-html="sortIcon('category')"></span></th>
            <th class="column-name-title" @click="sortBy('material_name')">원료명<span v-html="sortIcon('material_name')"></span></th>
            <th class="column-range-title" @click="sortBy('intake_low')">섭취 범위<span v-html="sortIcon('intake_low')"></span></th>
            <th class="column-marks-title" @click="sortBy('marks')">특이사항<span v-html="sortIcon('marks')"></span></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(material, index) in sortedMaterials"
            :key="index"
            class="material-item"
          >
            <td class="column-category">{{ material.category }}</td>
            <td class="column-name">{{ material.material_name }}</td>
            <td class="column-range">
              {{ material.intake_low }} ~ {{ material.intake_high }}
              {{ material.intake_unit }}
            </td>
            <td class="column-marks">{{ material.marks }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else>
      <p>데이터를 불러오는 중입니다...</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ["materials"],
  data() {
    return {
      sortKey: "",
      sortOrders: {}
    };
  },
  computed: {
    sortedMaterials() {
      const key = this.sortKey;
      const order = this.sortOrders[key] || 1;
      return this.materials.slice().sort((a, b) => {
        return order * (a[key] > b[key] ? 1 : -1);
      });
    }
  },
  methods: {
    sortBy(key) {
      this.sortKey = key;
      this.sortOrders[key] = this.sortOrders[key] === 1 ? -1 : 1;
    },
    sortIcon(key) {
      if (this.sortKey !== key) {
        return '';
      }
      return this.sortOrders[key] === 1 ? '▲' : '▼';
    }
  }
};
</script>

<style scoped>
.material-list {
  max-width: 1500px;
  margin: 0 auto;
  font-size: 20px;
  font-family: Dotum;
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12pt;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
  text-align: center;
}

.material-item {
  border-bottom: 1px solid #ccc;
}

.column-category {
  font-weight: bold;
  min-width: 80px;
  text-align: center;
}
.column-name {
  margin-top: 5px;
}
.column-range {
  margin-top: 5px;
}
.column-marks {
  margin-top: 5px;
}

.column-category-title span,
.column-name-title span,
.column-range-title span,
.column-marks-title span {
  display: inline-block;
  margin-left: 5px;
  font-size: 14px;
  vertical-align: middle;
}
</style>
