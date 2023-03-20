<template>
    <!-- Primeira home page criada. -->
    <div>
        <searchDocumentsBox @click-search="searchDocuments" />
        <listDocuments :items="documents" />
    </div>
</template>

<script setup>
import { ref } from 'vue'

import searchDocumentsBox from '@c/composted-block/search-documents-box.vue'
import listDocuments from '@c/composted-block/list-documents.vue'

import { apiSearchDocuments } from '#/spider-back/search'

let documents = ref({})

const searchDocuments = async function (search_text) {
    const data = await apiSearchDocuments(search_text, 2)
    documents.value = data
}
</script>
