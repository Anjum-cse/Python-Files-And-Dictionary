## 1. The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of credits taken this semester and assign it to the variable credits. Do not hardcode this – use dictionary accumulation!


Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
list = []
for k in Junior:
    list.append(Junior[k])
credits =sum(list)
print(credits)


## 2. Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.


str1 = "peter piper picked a peck of pickled peppers"

counts = {} # start with an empty dictionary
for c in str1:
    if c not in counts:
        # we have not seen this character before, so initialize a counter for it
        counts[c] = 0

    #whether we've seen it before or not, increment its counter
    counts[c] = counts[c] + 1

for c in counts.keys():
    print(c + ": " + str(counts[c]) + " occurrences")

## 3 Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.
print('\n')


s1 = "hello"

counts = {} # start with an empty dictionary
for c in s1:
    if c not in counts:
        # we have not seen this character before, so initialize a counter for it
        counts[c] = 0

    #whether we've seen it before or not, increment its counter
    counts[c] = counts[c] + 1

for c in counts.keys():
    print(c + ": " + str(counts[c]) + " occurrences")
    print('\n')
##Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
def word_count(str):
    freq_words = dict()
    words = str.split()

    for word in words:
        if word in freq_words:
            freq_words[word] += 1
        else:
            freq_words[word] = 1

    return freq_words


word_counts = word_count(str1)
print(word_counts)



## Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.


sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

wrd_d  = word_count(sent)
print(wrd_d)


 ## Create the dictionary characters that shows each character from the string sally and its frequency.
## Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.
sally = "sally sells sea shells by the sea shore"
characters = {}
for i in sally:
    characters[i] = characters.get(i, 0) + 1

sorted(characters.items(), key=lambda x: x[1])
best_char = sorted(characters.items(), key=lambda x: x[1])[-1][0]
print(best_char)


print('\n or another way')

sally = "sally sells sea shells by the sea shore"
characters = {}# start with an empty dictionary
for c in sally:
    if c not in characters:
        # we have not seen this character before, so initialize a counter for it
        characters[c] = 0

    #whether we've seen it before or not, increment its counter
    characters[c] = characters[c] + 1

for c in characters.keys():
    print(c + ": " + str(characters[c]) + " occurrences")

best_char = max(characters.keys(), key=(lambda k: characters[k]))
print(best_char)

## Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char.


sally = "sally sells sea shells by the sea shore and by the road"

characters = {}
for i in sally:
    characters[i] = characters.get(i, 0) + 1

sorted(characters.items(), key=lambda x: x[1])
worst_char = sorted(characters.items(), key=lambda x: x[1])[-13][0]
print(worst_char)





## Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case


string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
letter_counts={}
for i in string1.lower():
    if i not in letter_counts:
        letter_counts[i]=0
    letter_counts[i]=letter_counts[i]+1

print(letter_counts)

## Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.


p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d={}
for i in p.lower():
    if i not in low_d:
        low_d[i]=0
    low_d[i]=low_d[i]+1
print(low_d)