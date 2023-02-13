import api from './axios-config'

const helloWord = () => {
    return api.get('').then((response) => response.data)
}

export default {
    helloWord,
}
