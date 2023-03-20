<template>
    <div>
        <extDocumentInfosForm @click-create-document="createDocument" />
    </div>
</template>

<script setup>
import extDocumentInfosForm from '../components/external-component/forms/ext-document-infos-form.vue'

import { apiCreateDocument } from '../../apis/spider-back/external-documents'

const createDocument = async (document) => {
    try {
        const { documentName, documentPath, documentDescription } = document
        console.log(document)
        await apiCreateDocument(documentName, documentPath, documentDescription)
        alert('Salvo com sucesso')
    } catch {
        alert('ocorreu um erro ao salvar')
    }
}
</script>
