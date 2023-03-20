<script setup>
import homeAddDocument from './pages/home-add-document.vue'
import homeWithSearch from './pages/home-with-search.vue'
</script>

<template>
    <div class="tw-w-full tw-min-h-screen tw-flex tw-justify-center tw-flex-wrap">
        <div class="tw-w-3/4">
            <p class="tw-mb-5 tw-text-[38px]">Pesquise por um documento!</p>
            <homeWithSearch class="tw-mr-auto tw-w-8/12" />
        </div>
        <div class="tw-w-3/4">
            <p class="tw-mb-5 tw-text-[38px]">Adicione um novo documento!</p>
            <homeAddDocument class="tw-mr-auto tw-w-8/12" />
        </div>
    </div>
</template>
