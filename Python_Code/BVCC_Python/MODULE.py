from asyncio.windows_events import NULL
import re


#Method for finding all factors of a given number
def number_factors(number):
    numList = []
    for i in range(1, number+1):
        if number % i == 0:
            numList.append(i)
    return numList


#Method for checking if when given a word is an anagram
def anagram(word, match):
    if word is NULL or match is NULL:
        return False
    if word in "1234567890!@#$%^&*()_+-=,<>./?;:{[}]|\~`' " or match in "1234567890!@#$%^&*()_+-=,<>./?;:{[}]|\~`'":
        return False
    wordTemp = re.sub("^\\s+|\\s+$|\\s+", "", word.lower())
    matchTemp =  re.sub("^\\s+|\\s+$|\\s+", "", match.lower())
    if(sorted(wordTemp)== sorted(matchTemp)):
        return True
    else:
        return False

#Method for returning the factorial of a given number
def factorial(number):
    if number < 2:
        return 1
    else:
        return number * factorial(number - 1)






