<template>
    <div class="tw-mt-32">
        <ul class="tw-border tw-border-gray-200 tw-rounded tw-overflow-hidden tw-shadow-md">
            <li
                v-for="(link, index) in linksList"
                :key="index"
                class="tw-px-4 tw-py-2 tw-bg-white hover:tw-bg-sky-100 hover:tw-text-sky-900 tw-border-b tw-border-gray-200 tw-transition-all tw-duration-300 tw-ease-in-out"
            >
                <a :href="link.url">{{ link.text }}</a>
            </li>
        </ul>
    </div>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
    linksList: {
        type: Array,
        require: true,
        default: () => [],
    },
})
</script>
