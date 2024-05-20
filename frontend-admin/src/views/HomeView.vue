<script setup>
import { mdiChartTimelineVariant } from '@mdi/js'
import SectionMain from '@/components/SectionMain.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiChartTimelineVariant" title="Администраторски панел" main>
      </SectionTitleLineWithButton>
    </SectionMain>
  </LayoutAuthenticated>
</template>
