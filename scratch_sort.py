def swap(n1, n2, nums):
    tmp = nums[n1]
    nums[n1] = nums[n2]
    nums[n2] = tmp 

def sort(nums):
    for i in range(1, len(nums) ):
        for j in range(0, i):
            if nums[i] < nums[j]:
                swap(j, i, nums)
    return nums

print(sort([23, 45, 13, 12, 1]))
print(sort([100,1,58,2,63,0,10,9,2]))
