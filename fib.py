def fib(fib_val:int)-> int:
    if fib_val < 2:
        return fib_val
    return fib(fib_val -1) + fib(fib_val -2 )

def fib2(n: int) -> int:
    if n < 2: # base case
         return n
    return fib2(n - 2) + fib2(n - 1) # recursive case

print(fib2(20))
