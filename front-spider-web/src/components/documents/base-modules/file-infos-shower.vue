<template>
    <ul class="tw-block">
        <li v-for="(fileInfo, index) in fileInfosList" :key="index" class="tw-flex tw-flex-wrap tw-justify-around">
            <div class="tw-aspect-square tw-border tw-border-gray-700 tw-px-5">{{ fileInfo.name }}</div>
            <div class="tw-aspect-square tw-border tw-border-gray-700 tw-px-5">{{ fileInfo.path }}</div>
            <div class="tw-aspect-square tw-border tw-border-gray-700 tw-px-5">{{ fileInfo.start_line }}</div>
            <div class="tw-aspect-square tw-border tw-border-gray-700 tw-px-5">{{ fileInfo.end_line }}</div>
        </li>
    </ul>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
    fileInfosList: {
        type: Array,
        required: true,
        default: () => [],
    },
})
</script>
