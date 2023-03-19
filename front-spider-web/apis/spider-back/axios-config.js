import axios from 'axios'

const _axios = axios.create({
    baseURL: 'http://localhost:8999/',
    xsrfHeaderName: 'X-CSRFToken',
    xsrfCookieName: 'csrftoken',
    withCredentials: true,
    AccessControlAllowCredentials: true,
})

export default _axios
