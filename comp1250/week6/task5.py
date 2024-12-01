# You are a store own
# Create a dictionary of your inventory
#     The inventory should have 3 categories
#         Each category should have 2 items
my_inventory = {
    "fruits":["apple", "banana"],
    "dairy":["milk", "cheese"],
    "vegetables":["tomato", "potato"]
}
# You need to select a vendor
# Create a dictionary of the vendor's inventory
#     The inventory should have 3 categories
#         Each category should have 2 items
their_inventory = {
    "fruits":["orange", "banana"],
    "dairy":["milk", "yogurt"],
    "vegetables":["tomato", "potato"]
}
# Output the items that YOU have but the VENDOR does not have
my_items = []
for category, items in my_inventory.items():
    for item in items:
        if item not in their_inventory.get(category, []):
            my_items.append(item)
print("Ownder Only Items Are: ", my_items)
# Output the items that BOTH YOU and the VENDOR have
common_items = []
for category, items in my_inventory.items():
    common_items.append(set(items).intersection(set(their_inventory.get(category,[]))))
print(common_items)


# Ask the user for an item
user_item = input("Enter the item: ")
# Determine if the item is in STOCK (you have it)
is_in_stock = False
for items in my_inventory.values():
    if user_item in items:
        is_in_stock = True
        break
if is_in_stock:
    print("Item is in stock!")
else:
    print("Item is not in stock!")
# Determine if vendor carries the item (vendor has it)
is_in_stock = False
for items in their_inventory.values():
    if user_item in items:
        is_in_stock = True
        break
if is_in_stock:
    print("Item is in stock!")
else:
    print("Item is not in stock!")