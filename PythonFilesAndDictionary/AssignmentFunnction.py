## 1. Write a function called int_return that takes an integer as input and returns the same integer.

def int_return(value):
    return (value)
result = int_return(5)
print(result)


## 2.Write a function called add that takes any number as its input and returns that sum with 2 added.

def add(numb):
    sum = numb+2
    return (sum)
sumres = add(5)
print(sumres)

## 3.Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.

def change(strng):
    adds = strng + "Nice to meet you!"
    return (adds)

resultantstr = change('anjum ')
print(resultantstr)

## 4.Write a function, accum, that takes a list of integers as input and returns the sum of those integers.

def accum(list):
    sumlist= sum(list)
    return (sumlist)

resListSum = accum([1,2,3,4,5])
print(resListSum)

## 5. Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”

def length(list):
    if len(list) >= 5:
        return ("Longer than 5")
    else:
        return ("Less than 5")

resListlen = length([1,2,3,4,5])
print(resListlen)

## 6.You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.

def divide(n):
    return n/2
def sum(n):
    return n/2+6
print(sum(divide(10)))

