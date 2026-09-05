from datetime import datetime
import json
class AdminProductManager:
    def __init__(self, store):
        self.store = store

    def products(self):
        return (
            self.store.medicines
            + self.store.skincare
            + self.store.haircare
            + self.store.bodycare
            + self.store.mother_and_child
        )

    def add(self):
        id = int(input("ID: "))
        name = input("Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        expiry = input("Expiry (YYYY-MM-DD): ")
        description = input("Description: ")

        print("1. Medicine")
        print("2. Skin Care")
        print("3. Hair Care")
        print("4. Body Care")
        print("5. Mother & Child Care")

        choice = int(input("Category: "))

        if choice < 1 or choice > 5:
            print("Invalid category")
            return

        categories = [
            self.store.medicines,
            self.store.skincare,
            self.store.haircare,
            self.store.bodycare,
            self.store.mother_and_child
        ]

        categories[choice - 1].append({
            "id": id,
            "name": name,
            "price": price,
            "stock": stock,
            "expiry_date": expiry,
            "description": description
        })

        print("ADDED SUCCESSFULLY")

    def delete(self):
        id = int(input("Product ID: "))
        categories = [
            self.store.medicines,
            self.store.skincare,
            self.store.haircare,
            self.store.bodycare,
            self.store.mother_and_child
        ]
        
        for category in categories:
            for product in category:
                if product["id"] == id:
                    category.remove(product)
                    print("Deleted")
                    return

        print("SORRY, Not found")

    def save_products(self):
        with open("products.json", "w", encoding="utf-8") as f:
            json.dump(
                self.products(),
                f,
                indent=4,
                ensure_ascii=False
            )

    def update(self):
        id = int(input("Product ID: "))

        for product in self.products():
            if product["id"] == id:
                product["price"] = float(input("New price: "))
                product["stock"] = int(input("New stock: "))
                self.save_products()
                print("Updated")
                return
        print("SORRY, Not found")

    def low_stock(self):
        for product in self.products():
            if product["stock"] <= 5:
                print(product["name"], product["stock"])

    def expired(self):
        today = datetime.now().date()
        found_expired = False

        for product in self.products():
            try:
                exp_date = datetime.strptime(product["expiry_date"], "%Y-%m-%d").date()
                if exp_date < today:
                    print(f"⚠️ {product['name']} - Expired on: {product['expiry_date']}")
                    found_expired = True
            except ValueError:
                continue

        if not found_expired:
            print(" No expired products found.")