
"""Fonction permettant de vpirr si un mot est un palindrome"""
import string
from unidecode import unidecode

#### Fonction secondaire

def ispalindrome(s):

    """Vérifie si le mot passé est un palindrome"""
    s = unidecode(s.replace(" ","").lower())
    s = s.translate(str.maketrans("","",string.punctuation))
    return s== s[::-1]

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici
    """Voici une fonction permettant de tester la fonction ispalindrome"""
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
