names = ["Ronaldo", "Messi", "Neymar", "Bale", "Benzema"]

here = input("Footballer name: ")

if here in names:
    print(here, "Is amongst the football greats")
elif here == "Mbappe":
    print(here, "is a great player but not amongst the greats yet")
elif here not in names:
    print(here, "is not available")
