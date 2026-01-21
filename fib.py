
from typing import Dict


memo: Dict[int, int] = {0: 0, 1: 1}
#Using memoitization
def fib3(n: int) -> int:
    if n not in memo:
        print(f"Calling fib3({n})")
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]

def fib(fib_val:int)-> int:
    if fib_val < 2:
        return fib_val
    return fib(fib_val -1) + fib(fib_val -2 )

def fib2(n: int) -> int:
    print(f"Calling fib2({n}).")
    if n < 2: # base case
         return n
    return fib2(n - 2) + fib2(n - 1) # recursive case

#print(fib2(20))
# This would never complete without memoitization
print(fib3(999))
