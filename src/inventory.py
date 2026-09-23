"""Simple Inventory Management application for DevOps CI assignment."""

inventory = {}

def add_product(product_id, name, quantity, price):
    if quantity < 0 or price < 0:
        raise ValueError("Quantity and price cannot be negative")
    inventory[product_id] = {"name": name, "quantity": quantity, "price": price}

def update_stock(product_id, quantity):
    if product_id not in inventory:
        raise KeyError("Product not found")
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")
    inventory[product_id]["quantity"] = quantity

def remove_product(product_id):
    if product_id not in inventory:
        raise KeyError("Product not found")
    del inventory[product_id]

def get_stock(product_id):
    if product_id not in inventory:
        raise KeyError("Product not found")
    return inventory[product_id]["quantity"]

def inventory_value():
    return sum(item["quantity"] * item["price"] for item in inventory.values())

if __name__ == "__main__":
    add_product("P001", "Keyboard", 10, 750)
    add_product("P002", "Mouse", 20, 450)
    print("Inventory Management System - Resolved")
    for product_id, item in inventory.items():
        print(product_id, item["name"], "Stock:", item["quantity"])
    print("Total Inventory Value:", inventory_value())
