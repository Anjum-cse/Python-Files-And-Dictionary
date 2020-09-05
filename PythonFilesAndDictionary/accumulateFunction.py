## 1. Write a function named total that takes a list of integers as input, and returns the total value of all those integers added together.


def total(listofnum):
    add =0
    for number in listofnum:
        add = add + number
    return (add)
print(total([10,11,12]))


## 2. Write a function called count that takes a list of numbers as input and returns a count of the number of elements in the list.


def count(listofnum):
    add =0
    for number in listofnum:
        add = add + 1
    return (add)
print(count([10,11,12]))

