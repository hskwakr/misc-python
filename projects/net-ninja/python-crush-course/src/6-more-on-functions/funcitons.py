# # create a function
# def print_x_times(value="loop", x=5):
#     counter = 1
#     while counter <= x:
#         print(counter, value)
#         counter += 1
#     return "something else"

# # call
# print_x_times('test', 1)
# v = print_x_times()
# print(v)

# # from #3
# def calc_hypotenus(side_a = 1, side_b = 1):
#     hypotenus = pow(side_a ** 2 + side_b ** 2, 1/2)

#     return round(hypotenus, 2)

# print(calc_hypotenus(1, 1))
# print(calc_hypotenus(side_a=5, side_b=4))

# excercise
def shout(message = "orange", times = 3):
    r = 'done'

    if times >= 10:
        print('you are too loud')
        return r
    
    uppper = message.upper()
    for _ in range(times):
        print(uppper)

    return r

shout()
shout('hi', 10)
