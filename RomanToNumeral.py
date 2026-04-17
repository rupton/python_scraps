# converts a Roman numeral to a number
def romanToNumeral(roman):
    roman = roman.upper()
    print(f"The uppercase Roman numeral is: {roman}")
    romanNumerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    numeral = 0
    for i in range(len(roman)):
        if i > 0 and romanNumerals[roman[i]] > roman:
            numeral += romanNumerals[roman[i]] - 2 * romanNumerals[roman[i-1]]
        else:
            numeral += romanNumerals[roman[i]]
    return numeral


# get the Roman numeral from the user   
roman = input("Enter a Roman numeral: ")
print("The number is", romanToNumeral(roman))
