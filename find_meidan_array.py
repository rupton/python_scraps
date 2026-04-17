def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    merged = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i = i + 1
        else:
            merged.append(nums2[j])
            j = j + 1
    
    while i < len(nums1):
        merged.append(nums1[i])
        i = i + 1
    
    while j < len(nums2):
        merged.append(nums2[j])   
        j = j + 1
    
    if len(merged) == 1:
        return merged[0] 
    elif len(merged) == 2:
        return (merged[0] + merged[1]) / 2
    mid = len(merged) // 2
    if mid % 2 == 0:
        a = merged[mid -1]
        b = merged[mid]
        return (a + b) / 2
    else:
        return float(merged[mid])
    
arr1 = [1, 3, 6]
arr2 = [2, 4, 5, 7]
print(findMedianSortedArrays(arr1, arr2))

arr1 = []
arr2 = [2,3]
print(findMedianSortedArrays(arr1, arr2))

arr1 = []
arr2 = [1,2,3,4,5,6]
print(findMedianSortedArrays(arr1, arr2))

arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10,11,12,13,14,15,16,17]
print(findMedianSortedArrays(arr1, arr2))