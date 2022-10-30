<template>
  <div>
    <input @click="getHelloWorld" type="button" value="ユーザー情報取得" class="text-red-500">
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
    getHelloWorld() {
      this.axios
        .get("/users")
        .then((res) => {
          this.users = res.data[0]
        })
        .catch((e) => {
          console.log('e:', e);
        })
    }
  }
}
</script>
