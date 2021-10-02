# add = lambda a , b: a + b
# print(add(1, 2))
# print(add(1.0, 2.0))
# print(add(True, True))

# print((lambda a, b: a + b)(1, 2))

print((lambda *args: args)(1, 2, 'hi'))

# def check_sense(a, b, comparator):
#     if comparator(a, b):
#         print('Statements are same')
#     else:
#         print('Statements are different')
#
# def check_h(a):
#     return 'h' in a
# 
# check_sense('hi', 'hello', lambda a, b: check_h(a) and check_h(b))
# check_sense('hi', 'hello', lambda a, b: a[0] == a[0])
