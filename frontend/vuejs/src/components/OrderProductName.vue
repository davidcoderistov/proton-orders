<template>
  <v-list-item-title class="order-product-name">
    {{ productName }}
  </v-list-item-title>
</template>

<script>
export default {
  name: 'OrderProductName',
  props: {
    productName: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped>
.order-product-name {
  padding-bottom: 2px;
}
</style>