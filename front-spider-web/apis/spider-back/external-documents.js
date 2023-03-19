import api from './axios-config'
import { parametersToObject } from '../../utils/function-utils.js'

const putDocument = async (id, name, path, description) => {
    const params = parametersToObject({ name, path, description })
    const response = await api.put(`/external-documents/${id}/`, params)
    return response.data
}

export { putDocument }
