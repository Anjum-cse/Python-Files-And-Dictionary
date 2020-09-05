## 11. Write a function called change that takes one number as its input and returns that number, plus 7.
def change(num):
    #num = input("Enter Number: ")
    sum = int(num) + 7
    return(sum)
print(change(7))

## 8. Write a function named same that takes a string as input, and simply returns that string.

def same(str):
    #name = input("Enter Your Name:")
    return(str)
print(same("anjum"))


## 9. Write a function called same_thing that returns the parameter, unchanged.

def same_thing(age):
    return(age)


print(same_thing(25))


## 10. Write a function called subtract_three that takes an integer or any number as input, and returns that number minus three.

def subtract_three(num):
    sub = num - 3
    return (sub)


print(subtract_three(5))


## 13. Write a function called s_change that takes one string as input and returns that string, concatenated with the string ” for fun.”.

def s_change(str):
    con = str + " " + "for fun"
    return (con)


print(s_change('Coding'))


## 12. Write a function named intro that takes a string as input. Given the string “Becky” as input, the function should return: “Hello, my name is Becky and I love SI 106.”


def intro(str):
    output = "Hello, my name is" + " " + str + " " + "and I love SI 106."
    return (output)


print(intro("Becky"))



## 14. Write a function called decision that takes a string as input, and then checks the number of characters. If it has over 17 characters, return “This is a long string”, if it is shorter or has 17 characters, return “This is a short string”.


def decision(str):
    length = len(str)
    if length > 17:
        return ("This is a long string")
    else:
        return ("This is a short string")


print(decision("i am Anjum"))
print(decision("i am Anjum and i am from Cumilla"))

