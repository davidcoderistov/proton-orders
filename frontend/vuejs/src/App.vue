<template>
  <v-app>
    <v-main>
      <div class="orders-container">
        <div class="orders-wrapper">
          <v-card :width="450">
            <v-toolbar
                color="pink"
                dark
            >
              <v-toolbar-title>Orders</v-toolbar-title>
            </v-toolbar>
            <orders-loading-list
                v-if="ordersLoading"
                :size="7"
            />
            <div v-else style="overflow-y: auto; max-height: 75vh;">
              <orders-list
                  v-model="selectedOrder"
                  :orders="orders"
              />
            </div>
          </v-card>
          <v-btn
              color="pink"
              class="align-self-center white--text"
              :disabled="ordersLoading"
              @click="onAddOrder"
          >
            Add Order
          </v-btn>
          <v-card :width="450">
            <v-toolbar
                color="pink"
                dark
            >
              <v-toolbar-title>Follow up Orders ({{ followUpOrdersCount }})</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-title>${{ followUpOrdersPrice }}</v-toolbar-title>
            </v-toolbar>
            <orders-loading-list
                v-if="ordersLoading"
                :size="7"
            />
            <div v-else style="overflow-y: auto; max-height: 75vh;">
              <follow-up-orders-list :orders="followUpOrders"/>
            </div>
          </v-card>
        </div>
      </div>
    </v-main>
  </v-app>
</template>

<script>
import OrdersLoadingList from "@/components/OrdersLoadingList.vue";
import OrdersList from "@/components/OrdersList.vue";
import FollowUpOrdersList from "@/components/FollowUpOrdersList.vue";

export default {
  name: 'App',
  components: {OrdersLoadingList, OrdersList, FollowUpOrdersList},
  data: () => ({
    orders: [],
    ordersLoading: true,
    followUpOrders: [],
    selectedOrder: null,
  }),
  computed: {
    followUpOrdersCount() {
      if (Array.isArray(this.followUpOrders)) {
        return this.followUpOrders.length
      }
      return 0
    },
    followUpOrdersPrice() {
      if (Array.isArray(this.followUpOrders) && this.followUpOrders.length > 0) {
        const price = this.followUpOrders
            .map(order => parseFloat(Number(order.total_price).toFixed(2)))
            .reduce((sum, price) => sum + price, 0)
        return price.toFixed(2)
      }
      return '0.00'
    }
  },
  methods: {
    fetchOrders() {
      this.ordersLoading = true
      fetch('http://localhost:80/api/orders')
          .then(response => response.json())
          .then(data => {
            if (Array.isArray(data)) {
              this.orders = Array.from(data)
            }
          })
          .catch(console.error)
          .finally(() => {
            this.ordersLoading = false
          })
    },
    onAddOrder() {
      const {selectedOrder, orders, followUpOrders} = this
      if (!isNaN(selectedOrder) && typeof selectedOrder === 'number' && selectedOrder >= 0 && selectedOrder < orders.length) {
        const order = {...orders[selectedOrder]}
        const newOrders = [...orders]
        const newFollowUpOrders = [...followUpOrders]

        newOrders.splice(selectedOrder, 1)
        newFollowUpOrders.push(order)

        this.orders = newOrders
        this.followUpOrders = newFollowUpOrders
      }
    }
  },
  created() {
    this.fetchOrders()
  }
};
</script>

<style scoped>
.orders-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.orders-wrapper {
  display: flex;
  flex-direction: row;
  column-gap: 90px;
}
</style>
