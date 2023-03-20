<template>
    <div class="tw-w-[900px] tw-m-auto tw-mt-[100px]">
        <searchDocumentsBox />
        <listDocuments />
    </div>
</template>

<script setup>
import searchDocumentsBox from './composted-block/search-documents-box.vue'
import listDocuments from './composted-block/list-documents.vue'

import { putDocument } from '#/spider-back/external-documents.js'
import { searchDocuments } from '../../apis/spider-back/search'

console.log(putDocument(1, 'ronald', 'azul de novembro', 'conexao é simples e 5g velocidade'))
console.log(searchDocuments('ronald conexao', 2))
</script>
