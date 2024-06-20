<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      건기식 DB 데모버전 시연용 샘플 페이지
    </p>
    
  </div>
</template>

<script>
export default {
  name: 'InitialPage',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
p {
  font-size: 1.5em;
}
</style>
