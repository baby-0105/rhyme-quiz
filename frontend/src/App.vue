<script>
export default {
  data() {
    return {
      users: ""
    }
  },
  methods: {
    getUser() {
      this.axios
        .get("/users")
        .then((res) => {
          this.users = res.data
        })
        .catch((e) => {
          console.log('e:', e);
        })
    }
  }
}
</script>

<template>
  <h1>Hello World</h1>
  <input @click="getUser" type="button" value="DBからユーザー情報取得">
  <div>{{ users }}</div>
</template>

<style scoped>
</style>
