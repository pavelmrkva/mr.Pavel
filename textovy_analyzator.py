"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Pavel Mrkva

email: palon@seznam.cz

discord: pavel_58358

"""

print("$ python projekt1.py")

# registrovaní uživatelé a jejich hesla
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
separator = ("-" * 40)

# přihlášení do programu
name = input("enter a login name:")
password = input("enter password:")

if users.get(name) == password:
    print(separator, "Welcome to the app " + name, "We have 3 texts to be analyzed.", separator, sep="\n")
else:
    print("unregistered user, terminating the program..")
    exit()

# texty pro analyzu
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# vstup pro výběr textu
try:
    selected_text = int(input("Enter a number btw. 1 and 3 to select: "))
    if selected_text < 1 or selected_text > 3:
        print("Invalid input,terminating the program..")
        exit()
    else:
        selected_text -= 1
except ValueError:
    print("Input is not a number,terminating the program..")
    exit()

print(separator)

# analýza textu
analyze = TEXTS[selected_text].split()
word_count = len(analyze)

title_case = 0
upper_case = 0
lower_case = 0 
number_count = 0 
number_sum = 0

for word in analyze:
    
    if word.istitle():
        title_case += 1
    elif word.isupper() and word.isalpha():
        upper_case += 1
    elif word.islower():
        lower_case += 1
    elif word.isnumeric():
        number_count += 1
        number_sum += int(word)
        
print("There are", word_count, "words in the selected text.")
print("There are", title_case, "titlecase words.") 
print("There are", upper_case, "uppercase words.")        
print("There are", lower_case, "lowercase words.")
print("There are", number_count, "numeric strings.")
print("The sum of all the numbers", number_sum, ".")

print(separator, "LEN|    OCCURENCES    |NR.", separator, sep="\n")

# funkce pro četnost délek slov
word_length = {}
for word in analyze:
    length = len(word.strip(".,!?"))
    if length not in word_length:
        word_length[length] = 1
    else:
        word_length[length] += 1

word_length_sorted = sorted(word_length.keys())

for key in word_length_sorted:
    print(f"{key:>2} | {"*" * word_length[key]:<16} | {word_length[key]}")
