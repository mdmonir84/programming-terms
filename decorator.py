# first Class function

# Example-1
# def outer_func():
#     message = 'Hi'
#
#     def inner_func():
#         print(message)
#     return inner_func
#
#
# my_func = outer_func()
# print(my_func)
# print(my_func.__name__)
# my_func()


# closures
# def outer_func(msg):
#     message = msg
#
#     def inner_func():
#         print(message)
#     return inner_func
#
#
# hi_func = outer_func('Hi')
# hello_func = outer_func('Hello')
# hi_func()
# hello_func()


# # decorator
# def decorator_func(original_func):
#     def wrapper_func():
#         print('warpper executed this before {}'.format(original_func.__name__))
#         return original_func()
#     return wrapper_func
#
#
# @decorator_func
# def display():
#     print('display function ran')
#
#
# display()
#
# # Here @decorator_func ---> display = decorator_func(display)

# decorator
def decorator_func(original_func):
    def wrapper_func(*args, **kargs):
        print('warpper executed this before {}'.format(original_func.__name__))
        return original_func(*args, **kargs)
    return wrapper_func


@decorator_func
def display():
    print('display function ran')


@decorator_func
def display_info(name, age):
    print('display info ran with arguments ({}, {})'.format(name, age))


display_info('MD', 36)
display()

# Here @decorator_func ---> display = decorator_func(display)
