fruits = {"orange": "a sweet orange citrus fruit",
"apple": "good for making cider",
"lemon": "a sour, yellow citrus fruit",
"grape": "a small, sweet fruit growing in bunches",
"lime" : "a sour, green citrus fruit"}

#print(furits)
for fruit in fruits:
    print(fruits[fruit])

fruits["tomato"] = "A red fruit"

print(fruits["tomato"])

del fruits["tomato"]
for fruit in fruits:
    print(fruits[fruit])
