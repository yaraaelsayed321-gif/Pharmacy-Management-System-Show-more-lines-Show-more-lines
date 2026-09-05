class OrderManager:

    orders_list = []

    def __init__(self):
        pass

    def collect_checkout_info(self):

        print("\n----------------------------------")
        print("  CHECKOUT & SHIPPING DETAILS")
        print("----------------------------------")

        while True:
            name = input("Enter your full name: ").strip()
            if name != "":
               break  
            print(" Name cannot be empty!")

        while True:
            phone = input("Enter your phone number: ").strip()
            if phone != "":
               break  
            print(" Phone number cannot be empty!")

        print("\n--- Shipping Address ---")
        governorate = input("Enter Governorate: ").strip()
        city = input("Enter City/Area: ").strip()
        street = input("Enter Street Name & Building No: ").strip()

        address_dict = {
            "governorate": governorate,
            "city": city,
            "street": street
        }

        print("\n--- Select Payment Method ---")
        print("1. Cash on Delivery")
        print("2. Credit / Debit Card")



        methods = {"1": "Cash on Delivery", "2": "Credit Card"}

        while True:
              payment_choice = input("Choose payment method (1 or 2): ").strip()
              if payment_choice in methods:
                 payment_method = methods[payment_choice]
                 break
        print(" Invalid option! Please select 1 or 2.")

        customer_checkout_dict = {
            "name": name,
            "phone": phone,
            "address": address_dict,
            "payment_method": payment_method
        }

        return customer_checkout_dict

    def create_order(self, customer_info, cart_items):
        if len(cart_items) == 0:
            print(" Cannot create order. Cart is empty!")
            return None

        total_price = 0
        for item in cart_items:
            total_price += item["price"] * item["quantity"]

        order_number = len(OrderManager.orders_list) + 1
        order_id = "ORD-100" + str(order_number)

        order_dictionary = {
            "order_id": order_id,
            "customer": customer_info,
            "items": list(cart_items),
            "total_amount": total_price,
        }

        OrderManager.orders_list.append(order_dictionary)

        print("\n==================================")
        print("  ORDER CONFIRMED SUCCESSFULLY!")
        print("==================================")
        print(f" Order ID: {order_id}")
        print(f" Customer Name: {customer_info['name']}")
        print(f" Phone: {customer_info['phone']}")
        print(f" Delivery Address: {customer_info['address']['street']}, {customer_info['address']['city']}, {customer_info['address']['governorate']}")
        print(f" Payment Method: {customer_info['payment_method']}")
        print(f" Total Amount: ${total_price}")
        print("==================================")

        return order_dictionary

    def view_customer_order_history(self, customer_phone):
        print("\n----------------------------------")
        print("  YOUR ORDER HISTORY")
        print("----------------------------------")

        found = False

        for order in OrderManager.orders_list:
            if order["customer"]["phone"] == customer_phone:
                found = True
                print(f"Order ID: {order['order_id']}")
                print(f"Payment: {order['customer']['payment_method']}")
                print(f"Address: {order['customer']['address']['city']}, {order['customer']['address']['governorate']}")
                print("Items Purchased:")

                for item in order["items"]:
                    item_total = item["price"] * item["quantity"]
                    print(
                        f"  - {item['name']} | Qty: {item['quantity']} | Price: ${item['price']} | Subtotal: ${item_total}"
                    )
                print(f"Total Amount: ${order['total_amount']}")
                print("-" * 35)

        if not found:
            print(" No previous orders found for this phone number.")

    
# manager = OrderManager()

#     # 2. محاكاة سلة مشتريات القادمة من الشخص الرابع (Dummy Cart)
# dummy_cart = [
#         {"name": "Panadol Extra", "price": 25, "quantity": 2},
#         {"name": "Moist One Cream", "price": 85, "quantity": 1},
#     ]

# print("--- STARTING TEST ---")

#     # 3. تجربة جمع بيانات الشراء والتوصيل
# user_info = manager.collect_checkout_info()

#     # 4. تجربة تأكيد وإنشاء الأوردر
# manager.create_order(user_info, dummy_cart)

#     # 5. تجربة عرض سجل طلبات العميل
# manager.view_customer_order_history(user_info["phone"])

