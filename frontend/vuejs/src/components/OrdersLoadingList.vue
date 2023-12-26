<template>
  <div>
    <div v-for="index in items" :key="index">
      <v-skeleton-loader type="list-item-avatar-two-line"/>
      <v-divider v-if="index < items.length - 1"/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OrdersLoadingList',
  props: {
    size: {
      type: Number,
      default: 0,
    }
  },
  computed: {
    items() {
      return [...Array(this.size).keys()]
    }
  }
}
</script>

<style scoped>

</style>