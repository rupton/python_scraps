'''
    This is a simple bubble sort
'''
def bubble_sort_list(arr):
    n = len(arr)
    print(f"Original is {arr}")
    for i in range(n):
        for j in range(0, n - i -1): 
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1], arr[j]
        print(f" Interation \n {arr}")
    return arr
           
print(bubble_sort_list([4,5,6,9,0]))