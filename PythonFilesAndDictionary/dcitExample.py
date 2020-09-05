## 1. The dictionary travel contains the number of countries within each continent that Jackie has traveled to. Find the total number of countries that Jackie has been to, and save this number to the variable name total. Do not hard code this!

travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa": 1, "Antarctica": 0, "Australia": 1}

list = []
for k in travel:
    list.append(travel[k])
total =sum(list)
print(total)



## 2. schedule is a dictionary where a class name is a key and its value is how many credits it was worth. Go through and accumulate the total number of credits that have been earned so far and assign that to the variable total_credits. Do not hardcode.


schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}
list = []
for k in schedule:
    list.append(schedule[k])
total_credits =sum(list)
print(total_credits)

## 1. Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

lett_d = {} # start with an empty dictionary
for c in placement:
    if c not in lett_d:
        # we have not seen this character before, so initialize a counter for it
        lett_d[c] = 0

    #whether we've seen it before or not, increment its counter
    lett_d[c] = lett_d[c] + 1

for c in lett_d.keys():
    print(c + ": " + str(lett_d[c]) + " occurrences")

min_value = min(lett_d.keys(), key=(lambda k: lett_d[k]))
print("Min Occur Key", min_value+"\n")



## 5. Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value


product = "iphone and android phones"
lett_d = {} # start with an empty dictionary
for c in product:
    if c not in lett_d:
        # we have not seen this character before, so initialize a counter for it
        lett_d[c] = 0

    #whether we've seen it before or not, increment its counter
    lett_d[c] = lett_d[c] + 1

for c in lett_d.keys():
    print(c + ": " + str(lett_d[c]) + " occurrences")

max_value = max(lett_d.keys(), key=(lambda k: lett_d[k]))
print("Max Occur Key", max_value)