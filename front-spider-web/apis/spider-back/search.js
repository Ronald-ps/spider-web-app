import api from './axios-config'

const apiSearchDocuments = async (search_text, max_result_quantity) => {
    const params = { search_text, max_result_quantity: max_result_quantity || 12 }
    const response = await api.get(`/search-documents/`, { params })
    return response.data
}

export { apiSearchDocuments }
