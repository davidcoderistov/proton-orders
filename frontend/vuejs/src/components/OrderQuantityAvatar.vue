<template>
  <v-list-item-avatar color="pink" size="44">
    <span class="white--text">{{ quantity }}x</span>
  </v-list-item-avatar>
</template>

<script>
export default {
  name: 'OrderQuantityAvatar',
  props: {
    quantity: {
      type: Number,
      default: 1,
    }
  }
}
</script>