""" digits = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]
number = ''
for i in range(0, len(digits)):
    number += str(digits[i])

result = int(number)
result = result + 1
resultList = [int(x) for x in str(result)]


print(resultList) """

digits = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]
new_digits = digits[::2]
print(new_digits)