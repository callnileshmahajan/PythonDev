farm_animals = {"sheep", "cow", "hen"}

for animal in farm_animals:
    print(animal)

even = set(range(0, 40, 2))
print(even)

print(len(even))

sq_tuple = (4,6,9,16,25)
square = set(sq_tuple)

print(square)
print(len(square))

print(even.union(square))
print(len(even.union(square)))