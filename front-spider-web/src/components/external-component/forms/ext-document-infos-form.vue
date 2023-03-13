<template>
    <form class="tw-flex tw-flex-col tw-rounded-lg tw-ring-2 tw-ring-blue-100 tw-p-7">
        <label
            class="tw-block tw-mb-2 tw-text-sm tw-font-medium tw-text-gray-900 dark:tw-text-white"
            for="document-name-input"
            >Nome do Documento</label
        >
        <extInput id="document-name-input" type="text" />

        <label
            class="tw-mt-5 tw-block tw-mb-2 tw-text-sm tw-font-medium tw-text-gray-900 dark:tw-text-white"
            for="document-path-input"
            >Path do documento</label
        >
        <extInput id="document-path-input" type="text" />

        <extButton class="tw-mt-4 tw-group tw-relative tw-flex tw-w-1/5 tw-justify-center" type="submit"> Salvar </extButton>
    </form>
</template>

<script setup>
import extInput from './ext-input.vue'
import extButton from '../atomic/ext-button.vue'
</script>
