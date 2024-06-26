menu = [
    {
        "name": "Spanakopita",
        "description": "Flaky phyllo pastry filled with spinach, feta cheese, and aromatic herbs, baked to golden perfection.",
        "imageUrl": "spanakopita_image.jpg",
        "price": 8.99
    },
    {
        "name": "Souvlaki",
        "description": "Grilled skewers of marinated meat (chicken, pork, or lamb) served with pita bread, tzatziki sauce, and grilled vegetables.",
        "imageUrl": "souvlaki_image.jpg",
        "price": 10.99
    },
    {
        "name": "Tzatziki",
        "description": "Creamy Greek yogurt blended with cucumbers, garlic, olive oil, and herbs, served with warm pita bread.",
        "imageUrl": "tzatziki_image.jpg",
        "price": 6.99
    },
    {
        "name": "Calamari",
        "description": "Tender rings of squid lightly seasoned and fried to crispy perfection, served with lemon wedges and marinara sauce.",
        "imageUrl": "calamari_image.jpg",
        "price": 11.99
    },
    {
        "name": "Moussaka",
        "description": "Layers of eggplant, potato, and ground meat topped with béchamel sauce, baked to perfection.",
        "imageUrl": "moussaka_image.jpg",
        "price": 14.99
    },
    {
        "name": "Pastitsio",
        "description": "Greek-style baked pasta dish layered with ground meat, béchamel sauce, and pasta topped with cheese.",
        "imageUrl": "pastitsio_image.jpg",
        "price": 13.99
    },
    {
        "name": "Lamb Gyro",
        "description": "Slow-roasted lamb wrapped in warm pita bread with tzatziki sauce, lettuce, tomatoes, and onions.",
        "imageUrl": "lamb_gyro_image.jpg",
        "price": 15.99
    }
]

'''
Task 1: Print number of items in the menu as follows:
Items Available: X
'''
print("Items Available: ", len(menu))

'''
Task 2: Print name and price of each menu item as mentioned below:
Name: X
Price: Y
'''

for i in menu:
    print("Name: ", i["name"])
    print("Price: ", i["price"])

'''
Task 3: Create a receipt for the user who bought: Spanakopita, Calamari and Moussaka
Print each item's name and price followed by order total.
Name: X1, Price: $Y1
Name: X2, Price: $Y2
Name: X3, Price: $Y3
Total: Z
'''

#print("Name: ", menu[0]["name"], "Price: ", menu[0]["price"])
#print("Name: ", menu[3]["name"], "Price: ", menu[3]["price"])
#print("Name: ", menu[4]["name"], "Price: ", menu[4]["price"])

total = 0

for i in menu:
    if (i["name"] == "Spanakopita") or (i["name"] == "Calamari") or (i["name"] == "Moussaka") :
        print("Name: ", i["name"], ", Price: ", i["price"])
        total = total + i["price"]
        print("Total So Far: ", total)

print("Total: ", total)
'''
Task 4: Get total of first four items.
'''
sum = 0
for i in range(0,4):
    sum = sum + menu[i]["price"]

print("Sum: ", sum)


