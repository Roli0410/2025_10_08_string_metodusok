"""Szó keresése a szövegben – tartalom ellenőrzés
Feladat: Kérj be egy bejegyzést a közösségi oldalra, majd ellenőrizd, hogy szerepel-e benne a „Python” szó.
"""

bejegyzes = input("Írj egy bejegyzést:")

szoszam = bejegyzes.count("python")

print(f"A python szó ennyiszer van benne a szövegben: {szoszam}")