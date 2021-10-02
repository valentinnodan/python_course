# def f():
#     print(a)
#
# a = 1
# f()

# def f():
#     a = 1
#
# f()
# print(a)

# def f():
#     a = 1
#     print(a)
#
# a = 0
# f()
# print(a)

# def f():
#     print(a)
#     if False:
#         a = 0
#
# a = 1
# f()

# x = "super_global"
#
# def outer():
#     x = "local"
#
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)
#
#     def inner_global():
#         global x
#         x = "global"
#         print("inner:", x)
#
#     inner()
#     print("outer:", x)
#
# print(x)
# outer()
# print(x)

