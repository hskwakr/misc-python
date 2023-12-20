# functions
# print('a value')
# print(input('ask for a value'))

# methods -> functions of datatypes
# print('value'.upper())
# print('VALUE'.lower())
# print('value'.replace('e', '3'))

# new functions
# print(abs(-1))
# print(max(10, 5))
# print(min(0, 1))
# print(len('test'))

# exercise
side_a = int(input('Width of the triangle: '))
side_b = int(input('Height of the triangle: '))

hypotenus = pow(side_a ** 2 + side_b ** 2, 1/2)

print('The hypotenus is', round(hypotenus, 2))
