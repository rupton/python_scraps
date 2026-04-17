def sum_them(*nums):
    total = 0
    for n in nums:
        total += n
    return total

def sum_setstat(start, *nums):
    total = start
    for n in nums:
        total += n
    return total

print(sum_them(10,45,50,60))
print(sum_setstat(10, 10,20,30))