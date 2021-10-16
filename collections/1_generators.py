# gen = (x ** 2 for x in range(0, 3))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))





# gen = (x + y for x in range(0, 5) for y in range(0, 5) if x == y)
# for i in gen:
#     print(i)
# for i in gen:
#     print(i)





# def f_gen(m):
#     s = 1
#     for n in range(1,m):
#         yield n ** 2, s
#         s += 1
#
# for i in f_gen(5):
#     print(i)
#
# for i in f_gen(5):
#     print(i)




# def m_gen(n):
#     for i in range(n):
#         yield i
#     yield from range(n)
#
# for i in m_gen(3):
#     print(i)
#
# for i in m_gen(3):
#     print(i)



# def s_gen():
#     yield 'Hello, world!'
#     yield from 'No, goodbye...'
#
# for i in s_gen():
#     print(i)

# def inf_gen():
#     i = 2
#     while True:
#         yield i
#         i *= 2
#
# # is it bad?
# for i in inf_gen():
#     if i > 1e10:
#         break
#     print(i)

