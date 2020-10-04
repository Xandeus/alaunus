<template>
  <div class="posts">
    <md-button class="md-raised" v-on:click="getPosts()">Send Command</md-button>
    <br/>
    <div v-for="stripAnimation in stripAnimations" v-bind:key="stripAnimation.title">
      <p>
        <md-switch v-model="stripAnimation.isActive" @change="togglePost(stripAnimation.title, stripAnimation.isActive)">{{ stripAnimation.title }}</md-switch>
      </p>
    </div>
    <div>
      <md-button class="md-raised md-fab-top-left" v-on:click="trasmitRF('power_on')">Power Button</md-button>
      <md-button class="md-raised md-fab-top-center" v-on:click="transmitRF('red_button')">Red Button</md-button>
      <md-button class="md-raised md-fab-top-right" v-on:click="transmitRF('green_button')">Green Button</md-button>
    </div>
  </div>
</template>

<script>
import PostsService from '@/services/PostsService'
export default {
  name: 'posts',
  data () {
    return {
      message: '',
      isActive: false,
      posts: [],
      stripAnimations: []
    }
  },
  mounted () {
    this.$options.interval = setInterval(this.getPosts, 600000)
  },
  methods: {
    async getPosts () {
      console.log('Getting posts!')
      const userData = { command: 'ls', type: 'Hello' }
      const response = await PostsService.fetchPosts(userData)
      console.log(response.data)
      this.posts = response.data
      this.stripAnimations = response.data
    },
    async togglePost (toggleName, toggleState) {
      const data = { name: toggleName, state: toggleState }
      const response = await PostsService.fetchToggle(data)
      console.log(response.data)
      this.posts = response.data
    },
    async transmitRF (transmissionButtonName) {
      console.log('Tranmitting')
      const data = { name: transmissionButtonName }
      const response = await PostsService.fetchRFTransmit(data)
      console.log(response.data)
    }
  }
}
</script>
