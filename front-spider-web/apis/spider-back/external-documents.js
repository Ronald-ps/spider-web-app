import api from './axios-config'

const putDocument = async (id, name, path, description) => {
    const params = { name, description, path }
    const response = await api.put(`/external-documents/${id}/`, params)
    return response.data
}

export { putDocument }
