'''
   This is the implementation of FizBuzz, a popular game among programmers and often a staple of job interviews
   The rules are simple
   1. Start with a number and increment it by one each time
   2. If the number is divisible by three, print the word 'Fizz'
   3. If the number is divisible by five, print the word 'Buzz'
   4. If the number is divisible by BOTH three and five, print the word 'FizzBuzz'
   5. If the number isn't divisible by three, or five, print the number itself
'''

def fizzbuzz(num):
    try:
        num = int(num)
    except (ValueError, TypeError):
        return('Input must be an integer')
    #check for negative integer
    if num < 0:
        return 'You must provide a positive integer'
    
    if (num % 5 == 0) and (num % 3 == 0) :
        return('FizzBuzz')
    elif (num % 5 == 0):
        return('Buzz')
    elif (num % 3 == 0):
        return('Fizz')
    else:
        return(str(num))



