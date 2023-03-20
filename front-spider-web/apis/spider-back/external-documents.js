import api from './axios-config'

const apiPutDocument = async (id, name, path, description) => {
    const params = { name, description, path }
    const response = await api.put(`/external-documents/${id}/`, params)
    return response.data
}

const apiCreateDocument = async (name, path, description) => {
    const params = { name, description, path }
    const response = await api.post('/external-documents/', params)
    return response.data
}

export { apiPutDocument, apiCreateDocument }
