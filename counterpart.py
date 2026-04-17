'''
You are provided with a list of n integers, where n ranges from 2 to 200, inclusive. The task is to return a list of tuples, each containing a pair of an integer and its reverse counterpart.

In this context, the reverse counterpart of a number is the number with its digits reversed. For example, the reverse counterpart of 123 is 321.

'''

def solution(numbers):
    results = []
    for x in numbers:
        y = reverse(x)
        if(y in numbers):
            results.append((x, y))
    return results
      
def reverse(num):
    return int(str(num)[::-1])

seed_numbers = [x for x in range(2, 201)]
test1 = [12, 21, 34, 43, 56, 65]
print(solution(test1))