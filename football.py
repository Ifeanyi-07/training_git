names = ["Vini", "Mbappe", "Bellingham"]

here = input("Footballer name: ")

if here in names:
    print(here, "Is amongst the current football greats")
elif here == "Haaland":
    print(here, "is a great player but not amongst the greats yet")
elif here not in names:
    print("Who the hell is", here)
