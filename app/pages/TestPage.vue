<template>
  <div class="test-form">
    <router-link to="/" class="back-link">BACK</router-link>
    <div class="test-input">
          <p>
            <input type="text" v-model="token">
            {{token}}
          </p>
          <button class="add-button" @click="getAllSongs">Get Songs</button>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  export default {
    data: () => ({
        errors: [],
        token: 'Test'
      }),
    mounted () {
      //this.getAllSongs()
    },
    computed: {
      ...mapGetters([
        'allSongs'
      ])
    },
    methods: {
      ...mapActions([
        'getAllSongs'
      ])
    }
  }
</script>

<style>
</style>
