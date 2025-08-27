"""Weight converter"""

def grams_to_kilograms(grams):
    kilograms = int(grams) / 1000
    print(f"{kilograms} kg")


grams_to_kilograms(input("Grams: "))
