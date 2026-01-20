class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = []
        called = []
        running = ''
        
        for c in s:
            if not c in called:
                print(f"{c} has not been called. Called = {called} and running = {running}")
                called.append(c)
                running = running + c
            else:
                print(f"{c} has already been called. Called = {called} and running else = {running}")
                dict.append(running)
                running = c
        longest = -1
        for str in dict:
            if len(str) > longest:
                longest = len(str)


        print(dict)
        return longest

if __name__ == "__main__":
    solution = Solution()
    test_string1 = 'abcabcbb'
    longest_substring = solution.lengthOfLongestSubstring(test_string1)
    print(longest_substring)
    test_string2 = 'pwwkew'
    longest_substring2 = solution.lengthOfLongestSubstring(test_string2)
    print(longest_substring2)