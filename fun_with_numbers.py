'''
    Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

    Example 1:

    Input: x = 123
    Output: 321
    Example 2:

    Input: x = -123
    Output: -321
    Example 3:

    Input: x = 120
    Output: 21

'''
def reverse(x: int) -> int:
    is_negative = x < 0
    upper = 2**31 -1
    lower = -(2**31)
    result = 0
    x = abs(x)   
    while x > 0:
        n = x % 10
        result = result * 10 + x % 10
        x //= 10
    result = -result if is_negative else result
    if result < lower or result > upper:
        return 0
    return result

def convert_roman_to_int(number_string: str)-> int:
    conversions={"i":1, "v":5, "x":10, "l":50, "c": 100, "d":500, "m":1000}
    number_string = number_string.lower()
    # result = conversions.get(number_string[0])
    result = 0 
    for n in range(len(number_string) - 1):
        current_val = conversions.get(number_string[n])
        next_val = conversions.get(number_string[n + 1])
        if current_val < next_val:
            result -=  current_val
        else:
            result += current_val
     
    result += conversions.get(number_string[-1])   
    return result
    
    
#print(reverse(-9098))
print(convert_roman_to_int("VII"))
print(convert_roman_to_int("VI"))
print(convert_roman_to_int("iv"))
print(convert_roman_to_int("iii"))
print(convert_roman_to_int("iv"))
print(convert_roman_to_int("lc"))
print(convert_roman_to_int("cl"))
