# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L.sort())
# print(L[0][0])

# age = 13
# if age > 18:
#     print(1)
# else:
#     print(2)

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# su = 0
# x = 99
# while x > 0:
#     su = su + x
#     x = x - 1
# print(su)

# L = ['Bart', 'Lisa', 'Adam']
for x in L:
    for y in x:
        print('Hello,', y)

