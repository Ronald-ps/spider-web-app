import axios from 'axios'

const _axios = axios.create({
    baseURL: 'http://localhost:8001/',
    xsrfHeaderName: 'X-XSRF-TOKEN',
    xsrfCookieName: 'XSRF-TOKEN',
    withCredentials: true,
    AccessControlAllowCredentials: true,
})

export default _axios
