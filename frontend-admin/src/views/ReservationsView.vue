<script setup>
import { mdiBed } from '@mdi/js'
import SectionMain from '@/components/SectionMain.vue'
import TableReservations from '@/components/TableReservations.vue'
import CardBox from '@/components/CardBox.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'
import BaseButton from '@/components/BaseButton.vue'
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiBed" title="Резервации" main>
      </SectionTitleLineWithButton>
      <CardBox class="mb-6" has-table>
        <TableReservations />
      </CardBox>
      <BaseButton to="reservations/-1" color="success" label="Добави резервация" />
    </SectionMain>
  </LayoutAuthenticated>
</template>
