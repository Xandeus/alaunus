import axios from 'axios'

export default() => {
  return axios.create({
    baseURL: `http://10.0.0.37:8081`
  })
}
