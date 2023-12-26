<template>
  <v-list-item-action-text class="text--primary order-price">
    ${{ price | round }}
  </v-list-item-action-text>
</template>

<script>
export default {
  name: 'OrderPrice',
  props: {
    price: {
      type: Number,
      default: 0,
    }
  },
  filters: {
    round(value) {
      return Number(value).toFixed(2)
    }
  }
}
</script>

<style scoped>
.order-price {
  font-size: 16px;
}
</style>