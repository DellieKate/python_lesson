# --- USE: Dictionary Example ---
print("--- DICTIONARY: USE PHASE ---")
# Product inventory: item_name -> quantity
inventory = {
    "laptop_stand": 20,
    "usb_c_hub": 35,
    "wireless_mouse": 50
}
print(f"Initial inventory: {inventory}")

# Accessing an item's quantity
item_to_check = "usb_c_hub"
if item_to_check in inventory: # Good practice to check existence
    print(f"Quantity of {item_to_check}: {inventory[item_to_check]}")
else:
    print(f"{item_to_check} not found in inventory.")

# Using .get() to safely access (avoids KeyError)
item_to_check_safe = "monitor_arm"
quantity_safe = inventory.get(item_to_check_safe, 0) # Default to 0 if not found
print(f"Quantity of {item_to_check_safe} (using .get()): {quantity_safe}")

# Adding a new item
inventory["ergonomic_keyboard"] = 15
print(f"Inventory after adding keyboard: {inventory}")

# Updating an existing item's quantity (e.g., a new shipment arrived)
inventory["laptop_stand"] += 10
print(f"Inventory after restocking laptop stands: {inventory}")

# Removing an item (e.g., discontinued)
if "wireless_mouse" in inventory:
    del inventory["wireless_mouse"]
    print(f"Inventory after removing wireless mouse: {inventory}")

# Getting all keys, values, or items
print(f"All product names (keys): {list(inventory.keys())}")
print(f"All quantities (values): {list(inventory.values())}")
print(f"All inventory entries (items): {list(inventory.items())}")
print("-" * 30 + "\n")



#  **Tasks:**
#     1.  **New Product & Sale:**
#         *   A new product "webcam" arrives with a stock of 25 units. Add it to the inventory.
#         *   A customer buys 3 "usb_c_hub". Update its quantity. What happens if they try to buy more than available? (Don't implement the check yet, just note the potential issue).

inventory["webcam"] = 25
print(f"Inventory after adding webcam: {inventory}")

inventory["usb_c_hub"] -= 3
print(f"Inventory after customer sale: {inventory}")

inventory["usb_c_hub"] -= 35
if inventory["usb_c_hub"] <= 0: 
    print(f"Not enough supplies")
    
#     2.  **Price Check:**
#         *   Create a *separate* dictionary called `product_prices` storing prices for at least "laptop_stand" ($25), "usb_c_hub" ($30), and "ergonomic_keyboard" ($75).
#         *   A customer asks for the price of "laptop_stand". Print its price.
#         *   What if they ask for the price of "webcam" which isn't in `product_prices` yet? Use `.get()` to print "Price not available" if it's not found.

product_prices = {
    "laptop_stand" : 25,
    "usb_c_hub" : 30,
    "ergonomic_keyboard": 75
}

print(f'Product price for "laptop_stand": ${product_prices ["laptop_stand"]}')

price_to_check = "webcam"
price_check = product_prices.get(price_to_check, 'not available') 
print(f"Price of {price_to_check} (using .get()): {price_check}")


#     3.  **Stock Alert:**
#         *   For the "laptop_stand" in the `inventory`, check if its quantity is below 15. If it is, print a message like "Alert: Low stock for laptop_stand! Current quantity: [quantity]".

inventory = {
    "laptop_stand": 20,
    "usb_c_hub": 35,
    "wireless_mouse": 50
}
if inventory['laptop_stand'] <= 14:
    print(f'"Alert: Low stock for laptop_stand! Current quantity: {inventory['laptop_stand']}')
else :
    print(f'Supplies are adequate')
    
