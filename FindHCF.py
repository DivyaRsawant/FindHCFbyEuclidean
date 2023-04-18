# using recursion function

# by euclidean algorithm
def find_hcf(x, y):
    while(y):
        x, y = y, x % y
    return x


hcf = find_hcf(12, 14)
print("The hcf is", hcf)
