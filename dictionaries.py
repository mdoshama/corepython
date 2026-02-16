# Creating a dictionary with name, price, stock , later increasing price by 100, adding new key "brand", printing all details using loop

product = {
    "name" : "Laptop",
    "price" : 800,
    "stock": 5
}

product["price"] = 1000
product["brand"] = "Apple"

for key, value in product.items():
    print(key,":",  value)

#complete