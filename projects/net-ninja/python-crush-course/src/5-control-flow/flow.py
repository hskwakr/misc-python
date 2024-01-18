# print(5 > 4)

# # if statements
# condition = 5 > 4

# if condition:
#     print("correct result")
# elif 2 > 1 and 5 > 1:
#     print("some other result")
# else:
#     print("incorrect result")

# print("test")

# # while loop
# counter = 0

# while counter < 10:
#     print(counter)
#     counter += 1

# print("while loop has finished")

# # for loop
# # test_list = [1,2,3,4,5]
# test_list = {1:2, 3:4, 5:6}
# for k, v in test_list.items():
#     print(k, v)

# truthy and falsy
# if 0:
#     print("truthy")
# else:
#     print("falsy")

# if 1:
#     print("truthy")
# else:
#     print("falsy")

# if []:
#     print("truthy")
# else:
#     print("falsy")

# if [1]:
#     print("truthy")
# else:
#     print("falsy")

# if '':
#     print("truthy")
# else:
#     print("falsy")

# if ' ':
#     print("truthy")
# else:
#     print("falsy")

# exercise
a_list = [1, 2, 3, 4, 5]

for x in a_list:
    if x == 5:
        counter = 0
        while counter < 6:
            print("last item")
            counter += 1
    elif x == 2:
        print("the value is 2")
    else:
        print("the value is not 2")
