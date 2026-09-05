from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from datetime import datetime
import builtins
from contextlib import contextmanager

from products import PharmacyStore
from order import OrderManager
from store import StoreManager
from cart import cart
from admin import AdminProductManager

app = Flask(__name__)
app.secret_key = "pharmacy-management-system"

# The same object structure used by the original PharmacyApp.
store_db = PharmacyStore()
order_manager = OrderManager()
store_manager = StoreManager(store_db)
user_cart = cart(store_db, order_manager)
admin_manager = AdminProductManager(store_db)

CATEGORIES = {
    "medicines": ("Medicines", "medicine", "bi bi-capsule-pill"),
    "skincare": ("Skin Care", "skincare", "bi bi-droplet"),
    "haircare": ("Hair Care", "haircare", "bi bi-stars"),
    "bodycare": ("Body Care", "bodycare", "bi bi-heart"),
    "mother_and_child": ("Mother & Child", "mother_and_child", "bi bi-balloon-heart"),
}


def all_products():
    return store_db.get_all_product()


def product_category(product_id):
    for key, (label, _, _) in CATEGORIES.items():
        items = getattr(store_db, key)
        if any(p["id"] == product_id for p in items):
            return key, label
    return None, None


def product_by_id(product_id):
    return store_manager.get_product_details(product_id)


def low_stock_products():
    return [p for p in all_products() if p["stock"] <= 5]


def expired_products():
    today = datetime.now().date()
    result = []
    for p in all_products():
        try:
            if datetime.strptime(p["expiry_date"], "%Y-%m-%d").date() < today:
                result.append(p)
        except (KeyError, ValueError):
            pass
    return result


@contextmanager
def web_input(values):
    """Feed form values to an unchanged console method without changing its source."""
    iterator = iter(values)
    original_input = builtins.input
    builtins.input = lambda prompt="": str(next(iterator))
    try:
        yield
    finally:
        builtins.input = original_input


def run_admin_add(form):
    values = [form["id"], form["name"], form["price"], form["stock"], form["expiry"], form["description"], form["category"]]
    try:
        with web_input(values):
            admin_manager.add()
        return True, "Product added successfully."
    except (ValueError, StopIteration):
        return False, "Please enter valid product data."


def run_admin_update(form):
    try:
        with web_input([form["id"], form["price"], form["stock"]]):
            admin_manager.update()
        return True, "Product updated successfully."
    except (ValueError, StopIteration):
        return False, "Please enter valid update data."


def run_admin_delete(product_id):
    try:
        with web_input([product_id]):
            admin_manager.delete()
        return True, "Delete operation completed."
    except (ValueError, StopIteration):
        return False, "Invalid product ID."


def checkout_with_existing_logic(form):
    # Preserve cart.checkout() and OrderManager.collect_checkout_info()/create_order()
    # exactly as implemented, while supplying values from the browser form.
    values = [
        "yes",
        form["name"],
        form["phone"],
        form["governorate"],
        form["city"],
        form["street"],
        "1" if form["payment_method"] == "Cash on Delivery" else "2"
    ]
    before = len(OrderManager.orders_list)
    with web_input(values):
        user_cart.checkout()
    if len(OrderManager.orders_list) > before:
        return OrderManager.orders_list[-1]
    return None


def login_required():
    return "role" in session


def admin_required():
    return session.get("role") == "admin"


@app.context_processor
def globals_for_templates():
    return {
        "cart_count": sum(i["quantity"] for i in user_cart.cart),
        "current_role": session.get("role"),
        "current_name": session.get("name", "Guest"),
        "categories": CATEGORIES,
    }


@app.route("/")
def index():
    return redirect(url_for("login")) if not login_required() else redirect(url_for("dashboard"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        role = request.form.get("role", "user")
        if role == "admin":
            username = request.form.get("username", "").strip().lower()
            password = request.form.get("password", "")
            if username == "admin" and password == "1234":
                session.update(role="admin", name="Administrator")
                return redirect(url_for("dashboard"))
            flash("Invalid administrator credentials.", "danger")
        else:
            name = request.form.get("name", "").strip()
            if name:
                session.update(role="user", name=name)
                return redirect(url_for("dashboard"))
            flash("Name cannot be empty.", "warning")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    if not login_required(): return redirect(url_for("login"))
    products = all_products()
    orders = OrderManager.orders_list
    revenue = sum(o["total_amount"] for o in orders)
    return render_template("dashboard.html", products=products, orders=orders, revenue=revenue,
                           low_stock=low_stock_products(), expired=expired_products())


@app.route("/main-menu")
def main_menu():
    if not login_required(): return redirect(url_for("login"))
    return render_template("main_menu.html")


@app.route("/admin-management", methods=["GET", "POST"])
def admin_management():
    if not admin_required(): abort(403)
    if request.method == "POST":
        action = request.form.get("action")
        if action == "add":
            ok, msg = run_admin_add(request.form)
        elif action == "update":
            ok, msg = run_admin_update(request.form)
        elif action == "delete":
            ok, msg = run_admin_delete(request.form.get("id"))
        else:
            ok, msg = False, "Unknown action."
        flash(msg, "success" if ok else "danger")
        return redirect(url_for("admin_management"))
    return render_template("admin_management.html", products=admin_manager.products())


@app.route("/store")
def store():
    if not login_required(): return redirect(url_for("login"))
    q = request.args.get("q", "").strip()
    products = store_manager.search_products(q) if q else all_products()
    return render_template("store.html", products=products, query=q, title="Store")


@app.route("/categories")
def categories_page():
    if not login_required(): return redirect(url_for("login"))
    counts = {key: len(getattr(store_db, key)) for key in CATEGORIES}
    return render_template("categories.html", counts=counts)


def category_page(key):
    if not login_required(): return redirect(url_for("login"))
    if key not in CATEGORIES: abort(404)
    label, _, icon = CATEGORIES[key]
    products = getattr(store_db, key)
    return render_template("category.html", products=products, category=key, label=label, icon=icon)


app.add_url_rule("/medicines", "medicines", lambda: category_page("medicines"))
app.add_url_rule("/skin-care", "skin_care", lambda: category_page("skincare"))
app.add_url_rule("/hair-care", "hair_care", lambda: category_page("haircare"))
app.add_url_rule("/body-care", "body_care", lambda: category_page("bodycare"))
app.add_url_rule("/mother-child", "mother_child", lambda: category_page("mother_and_child"))


@app.route("/product/<int:product_id>")
def product_details(product_id):
    if not login_required(): return redirect(url_for("login"))
    product = product_by_id(product_id)
    if not product: abort(404)
    key, label = product_category(product_id)
    return render_template("product_details.html", product=product, category=key, category_label=label)


@app.route("/cart", methods=["GET", "POST"])
def cart_page():
    if not login_required(): return redirect(url_for("login"))
    if request.method == "POST":
        action = request.form.get("action")
        name = request.form.get("product", "")
        if action == "add":
            try:
                user_cart.addCart(name, int(request.form.get("quantity", 1)))
                flash("Cart updated.", "success")
            except ValueError:
                flash("Quantity must be a number.", "danger")
        elif action == "remove":
            user_cart.removeCart(name)
            flash("Item removed.", "success")
        elif action == "change":
            delta = int(request.form.get("delta", 0))
            if delta < 0:
                current = next((i["quantity"] for i in user_cart.cart if i["product"] == name), 0)
                for _ in range(min(-delta, max(0, current - 1))): user_cart.update_quantity_of_item(name, -1)
            else:
                for _ in range(delta): user_cart.update_quantity_of_item(name, 1)
            flash("Quantity updated.", "success")
        return redirect(url_for("cart_page"))
    return render_template("cart.html", items=user_cart.cart, total=user_cart.total_price_items())


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if not login_required(): return redirect(url_for("login"))
    if not user_cart.cart:
        flash("Your cart is empty.", "warning")
        return redirect(url_for("cart_page"))
    if request.method == "POST":
        required = ["name", "phone", "governorate", "city", "street", "payment_method"]
        if any(not request.form.get(k, "").strip() for k in required):
            flash("Please complete all checkout fields.", "danger")
            return render_template("checkout.html", items=user_cart.cart, total=user_cart.total_price_items())
        order = checkout_with_existing_logic(request.form)
        print("ORDER =", order)
        print("ORDERS LIST =", OrderManager.orders_list)
        if order:
            session["last_order_id"] = order["order_id"]
            return redirect(url_for("order_confirmation", order_id=order["order_id"]))
        flash("The order could not be completed. Please check stock.", "danger")
    return render_template("checkout.html", items=user_cart.cart, total=user_cart.total_price_items())


@app.route("/order-confirmation/<order_id>")
def order_confirmation(order_id):
    if not login_required(): return redirect(url_for("login"))
    order = next((o for o in OrderManager.orders_list if o["order_id"] == order_id), None)
    if not order: abort(404)
    return render_template("order_confirmation.html", order=order)


@app.route("/customer-management")
def customer_management():
    if not admin_required(): abort(403)
    print("ORDERS =", OrderManager.orders_list)
    customers = {}
    for order in OrderManager.orders_list:
        c = order["customer"]
        customers[c["phone"]] = c
    return render_template("customer_management.html", customers=list(customers.values()), orders=OrderManager.orders_list)


@app.route("/order-history", methods=["GET", "POST"])
def order_history():
    if not login_required(): return redirect(url_for("login"))
    phone = request.values.get("phone", "").strip()
    if session.get("role") == "user" and not phone:
        # User login has no phone in the original system; allow searching by form instead.
        pass
    orders = [o for o in OrderManager.orders_list if not phone or o["customer"]["phone"] == phone]
    return render_template("order_history.html", orders=orders, phone=phone)


@app.route("/reports")
def reports():
    if not admin_required(): abort(403)
    orders = OrderManager.orders_list
    category_totals = {label: 0 for label, _, _ in CATEGORIES.values()}
    for p in all_products():
        _, label = product_category(p["id"])
        category_totals[label] += 1
    return render_template("reports.html", orders=orders, products=all_products(), revenue=sum(o["total_amount"] for o in orders),
                           category_totals=category_totals, low_stock=low_stock_products(), expired=expired_products())


@app.route("/stock-management")
def stock_management():
    if not admin_required(): abort(403)
    return render_template("stock_management.html", products=all_products(), low_stock=low_stock_products(), expired=expired_products())


@app.errorhandler(403)
def forbidden(_):
    return render_template("error.html", code=403, message="You do not have permission to access this module."), 403


@app.errorhandler(404)
def not_found(_):
    return render_template("error.html", code=404, message="The requested page was not found."), 404
print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
