<template>
  <div>
    <input @click="getUser" type="button" value="DBからユーザー情報取得">
    <div>{{ users }}</div>
  </div>
</template>

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
