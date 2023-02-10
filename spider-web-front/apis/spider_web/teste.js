import api from './config'

export default {
  get() {
    api.get("/").then(r => r.data)
  }
}
