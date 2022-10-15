# 0(2^n) | 0(n) space
# def nthFib(n):
#     if n == 2:
#         return 1
#     elif n == 1:
#         return 0
#     else:
#         return nthFib(n-1) + nthFib(n-2)


# print(nthFib(6))

def nthFib(n):
    if n ==2:
        return 1
    elif n == 1:
        return 0

    tot = [0,1]
    count = 3
    while count <= n:
        next = tot[0] + tot[1]
        tot[0] = tot[1]
        tot[1] = next
        count += 1
    
    return tot[1]

print(nthFib(6))