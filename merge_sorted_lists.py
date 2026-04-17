def sortArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    print("Let's sort")
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
        
    return merged
        
    
arr1 = [1, 3, 6]
arr2 = [2, 4, 5, 7]
print(sortArrays(arr1, arr2))


        
