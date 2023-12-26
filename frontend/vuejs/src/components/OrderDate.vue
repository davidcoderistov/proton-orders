<template>
  <v-list-item-action-text :class="{ 'order-date': !dense }">
    {{ timestamp | date }}
  </v-list-item-action-text>
</template>

<script>
export default {
  name: 'OrderDate',
  props: {
    dense: {
      type: Boolean,
      default: false,
    },
    timestamp: {
      type: Number,
      default: 0,
    }
  },
  filters: {
    date(value) {
      let date = new Date()
      if (value) {
        date = new Date(value * 1000)
      }
      const day = date.getDate()
      const month = date.toLocaleString('default', {month: 'short'})
      const year = date.getFullYear()

      return `${day} ${month} ${year}`
    }
  }
}
</script>

<style scoped>
.order-date {
  padding-top: 2px;
}
</style>