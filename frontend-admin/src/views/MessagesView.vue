<script setup>
import {  mdiTableBorder } from '@mdi/js'
import SectionMain from '@/components/SectionMain.vue'
import TableMessages from '@/components/TableMessages.vue'
import CardBox from '@/components/CardBox.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiTableBorder" title="Потребителски мнения" main>
      </SectionTitleLineWithButton>
      <CardBox class="mb-6" has-table>
        <TableMessages />
      </CardBox>
    </SectionMain>
  </LayoutAuthenticated>
</template>
