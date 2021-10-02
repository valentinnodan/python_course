# def make_addition(x):
#     def add(n):
#         return x + n
#     return add
#
# adder = make_addition(100)
# print(adder(1))
# print(adder(2))

# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# def max_def(a, b = 0):
#     if a > b:
#         return a
#     else:
#         return b

# def max_strange(a = 0, b):
#     if a > b:
#         return a
#     else:
#         return b

# print(max(3, 5))
# print(max(5, 3))
# print(max(int(input()), int(input())))
# print(max(a = 5, b = 3))
# print(max(b = 8))


# def get_args(*args):
#     return args
#
# print(get_args(1, 2, 3, 'hello'))
# print(get_args())
# print(get_args('hi'))


def get_named_args(**kwargs):
    return kwargs

print(get_named_args(num = 1, s = 'ha'))
print(get_named_args())