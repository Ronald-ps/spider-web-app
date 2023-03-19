<template>
    <div class="tw-w-[900px] tw-m-auto tw-mt-[100px]">
        <extDocumentInfosForm />
        <extLoginForm />
    </div>
</template>

<script setup>
import extDocumentInfosForm from './external-component/forms/ext-document-infos-form.vue'
import extLoginForm from './external-component/forms/ext-login-form.vue'
import { putDocument } from '#/spider-back/external-documents.js'

console.log(putDocument(1, 'ronald', 'azul de novembro', 'conexao é simples e 5g velocidade'))
</script>
