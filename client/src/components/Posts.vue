<template>
  <div class="posts">
    <h1>Posts</h1>
    <input v-model="message" placeholder="edit me">
    <p>Message is: {{ message }}</p>
    <md-button class="md-raised" v-on:click="getPosts()">Send Command</md-button>
    <div v-for="post in posts" v-bind:key="post.title">
      <p>
        <span><b>{{ post.title }}</b></span><br />
        <span>{{ post.description }}</span>
      </p>
    </div>
    <md-switch v-model="isActive">Send Command</md-switch>
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
      posts: []
    }
  },
  mounted () {
    this.getPosts()
  },
  methods: {
    async getPosts () {
      const userData = { command: 'ls', type: 'Hello' }
      const response = await PostsService.fetchPosts(userData)
      this.posts = response.data
    }
  }
}
</script>
