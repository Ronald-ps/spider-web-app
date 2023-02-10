import axios from 'axios'

const api = axios.create({
  baseURL: "http://127.0.0.1:8001",
  xsrfHeaderName: 'X-XSRF-TOKEN',
  xsrfCookieName: 'XSRF-TOKEN',
})

export default api
