<script setup>
import { mdiBed } from '@mdi/js'
import SectionMain from '@/components/SectionMain.vue'
import TableRooms from '@/components/TableRooms.vue'
import CardBox from '@/components/CardBox.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'
import BaseButton from '@/components/BaseButton.vue'
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiBed" title="Стаи" main>
      </SectionTitleLineWithButton>
      <CardBox class="mb-6" has-table>
        <TableRooms />
      </CardBox>
      <BaseButton to="rooms/-1" color="success" label="Добави стая" />
    </SectionMain>
  </LayoutAuthenticated>
</template>
