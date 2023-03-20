<template>
    <div class="tw-flex tw-h-min-[192px] tw-h-[240px] tw-outline tw-outline-blue-200">
        <div class="tw-max-h-12 tw-min-h-7 tw-w-10/12 tw-flex tw-justify-end tw-relative tw-top-1/3">
            <extInput
                class="tw-w-9/12 tw-inline-block"
                placeholder="Pesquisa por"
                @input="(event) => (search_text = event.target.value)"
                @keyup.enter="$emit('click-search', search_text)"
            />
            <extButton class="tw-w-2/12 tw-ml-3" @click="$emit('click-search', search_text)"> Pesquisar </extButton>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

import extInput from '../external-component/forms/ext-input.vue'
import extButton from '../external-component/atomic/ext-button.vue'

const search_text = ref('')

// let timer
// function debounce(_function, time) {
//     clearTimeout(timer)
//     timer = setTimeout(_function, time)
// }

// const emitClickSearch = debounce(function () {
//     this.emit('click-search', search_text)
// }, 100)

defineEmits(['click-search'])
</script>
