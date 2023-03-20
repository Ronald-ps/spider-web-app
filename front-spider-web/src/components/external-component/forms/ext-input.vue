<template>
    <!-- Componente externo que modifiquei tanto que já dá quase pra
    passar para os componentes próprios kkkk -->

    <div class="tw-w-inline-block">
        <label
            v-if="id && label"
            class="tw-mt-5 tw-block tw-mb-2 tw-text-sm tw-font-medium tw-text-gray-900 dark:tw-text-white"
            :for="id"
        >
            {{ label }}</label
        >
        <input
            :id="id"
            :placeholder="placeholder"
            class="tw-w-block tw-w-full tw-bg-gray-50 tw-border tw-border-gray-300 tw-text-gray-900 tw-text-sm tw-rounded-lg focus:tw-ring-blue-500 focus:tw-border-blue-500 tw-block tw-p-2.5 dark:tw-bg-gray-700 dark:tw-border-gray-600 dark:tw-placeholder-gray-400 dark:tw-text-white dark:tw-focus:ring-blue-500 dark:tw-focus:border-blue-500"
            @input="$emit('update:modelValue', $event.target.value)"
        />
    </div>
</template>

<script setup>
defineProps({
    label: {
        type: String,
        default: null,
    },
    id: {
        type: String,
        default: null,
    },
    placeholder: {
        type: String,
        default: '',
    },
    modelValue: {
        type: String,
        default: null,
    },
})

defineEmits(['update:modelValue'])
</script>
