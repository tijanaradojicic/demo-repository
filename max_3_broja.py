a = 42
b = 93
c = 21

# if a > b:
#     if a > c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b > c:
#         print(b)
#     else:
#         print(c)

if a > b and a > c:
    print(a)
elif c > a and c > b:
    print(c)
else:
    print(b)
