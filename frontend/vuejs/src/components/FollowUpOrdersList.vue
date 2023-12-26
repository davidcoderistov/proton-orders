<template>
  <v-list two-line>
    <template v-for="(order, index) in orders">
      <v-list-item :key="order._id">
        <order-quantity-avatar :quantity="order.quantity"/>
        <v-list-item-content>
          <order-product-name :product-name="order.product_name"/>
          <order-customer-name :customer-name="order.customer_name"/>
        </v-list-item-content>
        <v-list-item-action>
          <order-price :price="order.total_price"/>
          <order-date
              :timestamp="order.date"
          />
        </v-list-item-action>
      </v-list-item>
      <v-divider
          v-if="index < orders.length - 1"
          :key="index"
      ></v-divider>
    </template>
  </v-list>
</template>

<script>
import OrderQuantityAvatar from "@/components/OrderQuantityAvatar.vue";
import OrderProductName from "@/components/OrderProductName.vue";
import OrderCustomerName from "@/components/OrderCustomerName.vue";
import OrderDate from "@/components/OrderDate.vue";
import OrderPrice from "@/components/OrderPrice.vue";

export default {
  name: 'FollowUpOrdersList',
  components: {OrderQuantityAvatar, OrderProductName, OrderCustomerName, OrderDate, OrderPrice},
  props: {
    orders: {
      type: Array,
      default: () => ([])
    }
  },
}
</script>

<style scoped>

</style>