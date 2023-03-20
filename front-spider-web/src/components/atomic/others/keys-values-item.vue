<template>
    <!-- Componente utilizado para renderizar informações de chave e valor, de um mesmo elemento -->
    <div class="tw-pl-6 tw-pr-12 tw-py-8 tw-outline tw-outline-gray-400 tw-rounded-sm tw-inline-block">
        <p v-for="(value, key, index) in item" :key="index" class="tw-block tw-text-opacity-70 tw-font-light tw-text-lg">
            <span>{{ key }}</span> : <span>{{ value }}</span>
        </p>
    </div>
</template>

<script setup>
defineProps({
    item: {
        require: true,
        type: Object,
        default: () => {},
    },
})
</script>
