shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == "spam":
        continue
    
    print("Buy " + item)


for i in range(0, 100, 7):
    if i != 0 and i % 11 == 0:
        break
    print(i)