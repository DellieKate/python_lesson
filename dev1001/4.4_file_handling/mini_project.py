import csv
import json
with open("products.txt", "r") as f:
    products = csv.reader(f, delimiter=":")
    product_dict = []
    rows = []
    for row in products:
        rows.append(row)
        name, category, price = row
        print(f"Name: {name}, Category: {category}, Price:{float(price)}")
        product_dict.append({"name": name, "category": category, "price": price})
print(product_dict)
with open("products_export.json", "w") as (f):
    json.dump(product_dict, f, indent=4)
with open("product_export.csv", mode='w', newline='') as f:
    product_export = csv.writer(f)
    header = ["name", "category", "price"]
    product_export.writerows(rows)