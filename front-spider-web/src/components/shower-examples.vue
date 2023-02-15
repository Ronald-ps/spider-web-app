<template>
    <bmTextInput class="tw-w-9/12 tw-mx-auto" />
    <selectSimple />
    <linkShower :links-list="linksList" />
    <fileInfosShower :file-infos-list="fileInfosList" class="tw-max-h-0.5" />
</template>

<script setup>
import bmTextInput from './documents/base-modules/bm-text-input.vue'
import selectSimple from './user-interface/menu-selects/select-simple.vue'
import linkShower from './documents/base-modules/links-list-shower.vue'
import fileInfosShower from './documents/base-modules/file-infos-shower.vue'

import { linksList, fileInfosList } from '../../mock-environment/apis/spider-web/db/teste'
</script>
