import math as m
def solution(numbers):
    # TODO: implement this function
    n = len(numbers)
    results = []
    for num in range(n):
        #mean = round(m.sqrt(numbers[num] * numbers[n - num - 1]))
        results.append((numbers[num], round(m.sqrt(numbers[num] * numbers[n - num -1]),2 )))
        
    return results

print(solution([1,2,3,4,5]))