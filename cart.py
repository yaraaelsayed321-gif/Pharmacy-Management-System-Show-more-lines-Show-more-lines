from products import PharmacyStore
from order import OrderManager

class cart:
    def __init__(self, store_instance=None, order_instance=None):
        self.p1 = store_instance if store_instance else PharmacyStore()
        self.o1 = order_instance if order_instance else OrderManager()
        self.cart = []

    def addCart(self, product_name, quantity=1):
        for item_info in self.p1.get_all_product():
            if product_name.strip().lower() == item_info["name"].strip().lower():
                if quantity <= item_info["stock"]:
                    for item in self.cart:
                        if product_name.strip().lower() == item["product"].strip().lower():
                            item["quantity"] += quantity
                            print("Add successfully")
                            return
                    self.cart.append({
                        "product": item_info["name"],
                        "price": item_info["price"],
                        "quantity": quantity
                    })
                    print("Add successfully")
                    return
                else:
                    print("Out of stock")
                    return
        print("Product invalid")

    def removeCart(self, product):
        for item in self.cart:
            if product == item["product"]:
                self.cart.remove(item)
                print("Removed")
                return

    def update_quantity_of_item(self, products, value):
        for item in self.cart:
            if products == item["product"]:
                if item["quantity"] + value <= self.p1.get_stock(item["product"]):
                    item["quantity"] += value
                else:
                    print("Out of stock")
                    return

    def total_price_items(self):
        total_price = 0
        for item in self.cart:
            total_price += (item["price"] * item["quantity"])
        return total_price

    def checkout(self):
        if self.cart:
            for item in self.cart:
                if item["quantity"] > self.p1.get_stock(item["product"]):
                    print("Invalid stock")
                    return
            print(f"Total: ${self.total_price_items()}")
            ask = input("Do you want to complete purchase? (yes/no): ").lower()
            if ask == "yes":
                customer_info = self.o1.collect_checkout_info()
                choice = self.o1.create_order(customer_info, self.cart)

                print("CHOICE =", choice)
                print("ORDERS =", OrderManager.orders_list)

                if choice:
                    print("Order completed successfully")
                    for item in self.cart:
                        current_stock = self.p1.get_stock(item["product"])
                        self.p1.set_stock(item["product"], current_stock - item["quantity"])
                    self.cart.clear()
        else:
            print("The cart is empty")