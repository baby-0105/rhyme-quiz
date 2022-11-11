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
  <div class="text-center">
    <p class="text-rose-500 text-3xl">Hello World</p>
    <button class="border p-1" @click="getUser" type="button">DBからユーザー情報取得</button>
    <div>{{ users }}</div>
  </div>
</template>

<style scoped>
</style>
