<template>
    <!-- Responsável por listar documentos. O items são passados e listados com um padrão chave: valor -->

    <div class="tw-px-3.5">
        <keysValuesItem v-for="(item, index) in items" :key="index" :item="item" class="tw-w-full tw-mt-3" />
    </div>
</template>
<script setup>
import keysValuesItem from '../atomic/others/keys-values-item.vue'

defineProps({
    items: {
        require: true,
        type: Object,
        default: () => {},
    },
})
</script>
