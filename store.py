from products import PharmacyStore

class StoreManager:
    def __init__(self, store_instance):
        self.store = store_instance

    def _get_all_products(self):
        return (
            self.store.medicines +
            self.store.skincare +
            self.store.haircare +
            self.store.bodycare +
            self.store.mother_and_child
        )

    def search_products(self, keyword):
        results = []
        clean_keyword = keyword.strip().lower()

        for product in self._get_all_products():
            if clean_keyword in product["name"].lower():
                results.append({
                    "id": product["id"],
                    "name": product["name"],
                    "price": product["price"],
                    "stock": product["stock"],
                    "expiry_date": product["expiry_date"],
                    "description": product.get("description", ""),
                    "ingredients": product.get("ingredients", [])
                })
        return results

    def get_product_details(self, product_id):
        for product in self._get_all_products():
            if product["id"] == product_id:
                return {
                    "id": product["id"],
                    "name": product["name"],
                    "price": product["price"],
                    "stock": product["stock"],
                    "expiry_date": product["expiry_date"],
                    "description": product.get("description", ""),
                    "ingredients": product.get("ingredients", [])
                }
        return None