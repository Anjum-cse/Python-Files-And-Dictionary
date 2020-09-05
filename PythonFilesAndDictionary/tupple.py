## 4. Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]

res = [t_check[2] for t_check in lst_tups]
print(res)

## 5. Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called seconds

tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]
res = [seconds[1] for seconds in tups]
print (res)

## If you remember, the .items() dictionary method produces a sequence of tuples. Keeping this in mind, we have provided you a dictionary called pokemon. For every key value pair, append the key to the list p_names, and append the value to the list p_number. Do not use the .keys() or .values() methods.


pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names= []
p_number= []

for i in pokemon:
    p_names.append(i)
    p_number.append(pokemon[i])

print(p_names)
print(p_number)

## Define a function called info with the following required parameters: name, age, birth_year, year_in_college, and hometown. The function should return a tuple that contains all the inputted information.


def info():
    personalInfo =()
    name = input("Enter name:")
    age  = input("Enter Age:")
    birth_year =  input("Birth Year")
    year_in_college =  input("YiC:")
    hometown = input("town:")
    personalInfo =  (name, age, birth_year, year_in_college, hometown)
    return(personalInfo)
print(info())






##  Define a function called information that takes as input, the variables name, birth_year, fav_color, and hometown. It should return a tuple of these variables in this order.

def information():
    data = ()
    name = input('Enter your name: ')
    yob = input('Enter your year of birth: ')
    fav_color = input('Enter your favourite colour: ')
    hometown = input('Enter your hometown: ')

    data = (name, yob, fav_color, hometown)
    return data
print(information())

