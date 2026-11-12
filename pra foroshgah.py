name = input("Please enter your name: ")

product = ["Apple", "Banana", "Orange", "Milk", "Bread"]

for All in product:
    print(All)

vorodi = input("Please enter your product: ")

if vorodi == "Apple":
    price = 30000

elif vorodi == "Banana":
    price = 20000

elif vorodi == "Orange":
    price = 25000

elif vorodi == "Milk":
    price = 40000

elif vorodi == "Bread":
    price = 35000

else:
    price = 0
    print("Product not found!")

if price > 0:
    print(f"Customer name: {name}")
    print(f"Purchased product: {vorodi}")
    print(f"Price: {price} Toman")