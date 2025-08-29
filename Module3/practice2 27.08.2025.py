customer_type = input("What is your type (Elf, Wizard, Ghost)?").strip().capitalize()
age = int(input("How is your age?"))

products = ["sparkling water"]
if customer_type == "Elf":
    if age > 100:
        products.append("Leaf Drinks")

elif customer_type == "Wizard":
    if age > 21:
        products.append("Wine")

elif customer_type == "Ghost":
    products.append("dust cookies")

print("You can buy " + " and ".join(products))