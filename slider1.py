def find_max(arr, k):
    if len(arr) == 1 or k <=1:
        return arr[0]
    
    # Safe to assume k < len(arr)
    i = 0
    sum = 0
    while k <= len(arr):
        count = 0
        for x in range(i,k):
            count += arr[x]
        print(f"Count is currently {count}")
        if count > sum:
            sum = count
            print("Found a bigger value")
        i += 1
        k +=1
    return sum

print(find_max([10,23,1,5,60,3], 3))