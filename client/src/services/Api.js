import axios from 'axios'

export default() => {
  return axios.create({
    baseURL: `http://192.168.50.184:8081`
  })
}
