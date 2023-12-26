<template>
  <v-list two-line>
    <v-list-item-group
        v-model="selected"
        active-class="pink--text"
    >
      <template v-for="(order, index) in orders">
        <v-list-item :key="order._id">
          <template v-slot:default="{ active }">
            <order-quantity-avatar :quantity="order.quantity"/>
            <v-list-item-content>
              <order-product-name :product-name="order.product_name"/>
              <order-customer-name :customer-name="order.customer_name"/>
              <order-date :timestamp="order.date"/>
            </v-list-item-content>
            <v-list-item-action>
              <order-price :price="order.total_price"/>
              <v-icon
                  v-if="!active"
                  color="grey lighten-1"
              >
                mdi-star-outline
              </v-icon>
              <v-icon
                  v-else
                  color="yellow darken-3"
              >
                mdi-star
              </v-icon>
            </v-list-item-action>
          </template>
        </v-list-item>
        <v-divider
            v-if="index < orders.length - 1"
            :key="index"
        ></v-divider>
      </template>
    </v-list-item-group>
  </v-list>
</template>

<script>
import OrderQuantityAvatar from "@/components/OrderQuantityAvatar.vue";
import OrderProductName from "@/components/OrderProductName.vue";
import OrderCustomerName from "@/components/OrderCustomerName.vue";
import OrderDate from "@/components/OrderDate.vue";
import OrderPrice from "@/components/OrderPrice.vue";

export default {
  name: 'OrdersList',
  components: {OrderQuantityAvatar, OrderProductName, OrderCustomerName, OrderDate, OrderPrice},
  props: {
    value: {
      type: Number,
      default: null,
    },
    orders: {
      type: Array,
      default: () => ([])
    }
  },
  computed: {
    selected: {
      get() {
        return this.value
      },
      set(value) {
        this.$emit('input', value)
      }
    }
  }
}
</script>

<style scoped>

</style>