<template>
    <form class="tw-flex tw-flex-col tw-rounded-lg tw-ring-2 tw-ring-blue-100 tw-p-7">
        <extInput id="document-name-input" v-model="documentName" type="text" label="Nome do documento" />
        <extInput id="document-path-input" v-model="documentPath" type="text" label="Path do documento" />
        <extInput id="document-description-input" v-model="documentDescription" type="text" label="descrição do documento" />
        <extButton
            class="tw-mt-4 tw-group tw-relative tw-flex tw-w-1/5 tw-justify-center"
            type="submit"
            @click.prevent="$emit('click-create-document', { documentName, documentPath, documentDescription })"
        >
            Salvar
        </extButton>
    </form>
</template>

<script setup>
import { ref } from 'vue'
import extInput from './ext-input.vue'
import extButton from '../atomic/ext-button.vue'

let documentName = ref('')
let documentPath = ref(null)
let documentDescription = ref(null)

defineEmits(['click-create-document'])
</script>
