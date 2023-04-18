# using recursion function
# def find_hcf(x, y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller + 1):
#         if (x % i == 0) and (y % i == 0):
#             hcf = i
#     return hcf
#
#
# num1 = int(input("Enter num1 :"))
# num2 = int(input("Enter num2 :"))
#
# print("The H.C.F is :", find_hcf(num1, num2))

# by euclidean algorithm
def find_hcf(x, y):
    while(y):
        x, y = y, x % y
    return x


hcf = find_hcf(12, 14)
print("The hcf is", hcf)
