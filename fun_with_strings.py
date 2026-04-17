def longest_common_prefix(strings_to_compare : list[str] )-> str:
    longest_prefix = ""
    for i in range(len(strings_to_compare[0])):
        for string in strings_to_compare:
            if i >= len(string):
                return longest_prefix
            else:
                if string[i] != strings_to_compare[0][i]:
                    return longest_prefix 
        longest_prefix += strings_to_compare[0][i]
    return longest_prefix          

def valid_parenthesis(string: str)->bool:
    parenthesis_stack = []
    opening_parens = ['(','[','{']
    matches = {")":"(", "]":"[", "}": "{"}
    for char in string:
        if char in opening_parens:
            parenthesis_stack.append(char)
        else:
            if not parenthesis_stack:
                return False
            if matches.get(char) == parenthesis_stack[-1]:
                parenthesis_stack.pop()
            else:
                return False
    
    return len(parenthesis_stack) == 0
         
         


print(valid_parenthesis("{[(){()}]}")  ) # valid
print(valid_parenthesis("{[(){()}}]")  ) # invalid
#print(valid_parenthesis("()[]{[}{}")  )  

()
'''   
# Should return "fl"
print(longest_common_prefix(["flower", "flow", "flight"]))

# Should return "" (no common prefix)
print(longest_common_prefix(["dog", "racecar", "car"]))

# Should return "abc"
print(longest_common_prefix(["abc", "abcdef", "abcd"]))

# Should return "a"
print(longest_common_prefix(["a"]))

# Edge case: should return "test"
print(longest_common_prefix(["test", "test", "test"]))
'''