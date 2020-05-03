import Api from '@/services/Api'

export default {
  fetchPosts (data) {
    return Api().post('posts', data)
  }
}
