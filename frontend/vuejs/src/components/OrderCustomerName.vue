<template>
  <v-list-item-subtitle class="text--primary">
    {{ customerName }}
  </v-list-item-subtitle>
</template>

<script>
export default {
  name: 'OrderCustomerName',
  props: {
    customerName: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped>

</style>