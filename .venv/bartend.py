from random import choice
drink = ["whiskey", "rum", "vodka", "tequila", "gin", "sake", "wine", "beer", "brandy"]
afters = ["coke", "fanta", "tonic", "redbull", "cherry coke", "white monster", "apa minerala"]

# print(f"{choice(drink)} {choice(afters)}")
print("Hello, I am your virtual bartender")
name = input("how should I call you? ")

try:
    age = input("how old are you? ")
    age = int(age)
    legal = None
    country = input("Where are you from? ")
    if age < 14:
        Legal = False
    elif age <= 16:
        if country == "Austria":
            print("Fuck you Max")
            legal = True
        else:
            legal = False
    elif age < 18:
        if country == "Austria" or country == "Luxembourg":
            legal = True
        else:
            legal = False
    elif age < 21:
        if country == "USA" or country == "UAE":
            legal = False
        else:
            legal = True
    else:
        legal = True
    if legal:
        repeat = True
        while repeat:
            print(f"I will give you {choice(drink)} {choice(afters)}")
            check1 = input("Is that okay? ")
            if check1 == "yes":
                print("Here you go, enjoy")
                repeat = False
            else:
                repeat = True
    else:
        print(f"I can only serve you {choice(afters)}")
        check2 = input("do you want it? ")
        if check2 == "yes":
            print("Here you go, enjoy")
        else:
            print("Okay, Have a nice day")
except ValueError:
    print("err")