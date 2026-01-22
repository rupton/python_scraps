
from typing import Dict

total_calls = 0
memo: Dict[int, int] = {0: 0, 1: 1}
#Using memoitization
def fib3(n: int) -> int:
    global total_calls 
    total_calls += 1
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]

def fib(fib_val:int)-> int:
    global total_calls 
    total_calls += 1
    if fib_val < 2:
        return fib_val
    return fib(fib_val -1) + fib(fib_val -2 )

def fib2(n: int) -> int:
    global total_calls 
    total_calls += 1
    print(f"Calling fib2({n}).")
    if n < 2: # base case
         return n
    return fib2(n - 2) + fib2(n - 1) # recursive case

#print(fib2(20))
# This would never complete without memoitization
print(f"The 999th number in the Fibonacci Sequence is {fib3(999)} and it took us {total_calls} calls to calculate it using memoitization")
