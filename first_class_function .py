# function can be assigned as regular variable


# def square(x):
#     return x*x
#
#
# f = square
# print(square)
# print(f)
# print(f(5))


# function can be passed as an argument

# def square(x):
#     return x*x
#
#
# def cube(x):
#     return x*x*x
#
#
# def my_map(func, args):
#     result = []
#     for arg in args:
#         result.append(func(arg))
#     return result
#
#
# squares = my_map(square, [1, 2, 3, 4, 5])
#
# print(squares)
#
#
# cubes = my_map(cube, [1, 2, 3, 4, 5])
#
# print(cubes)


# function can be retunre from another function

# # Example-1
# def logger(msg):
#     def log_message():
#         print('Log: ', msg)
#     return log_message
#
#
# log_hi = logger('Hi')
# log_hi()

# example-2
def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text


print_h1 = html_tag('h1')
print_h1('Test Headline')
print_h1('Another Headline')

print_h1 = html_tag('p')
print_h1('Test Paragraph')
