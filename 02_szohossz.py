"""Szóhossz meghatározása – tweet vagy SMS ellenőrzés
Feladat: Kérj be egy üzenetet a felhasználótól, majd írd ki, hány karakterből áll.
 Hasznos lehet például Twitter/SMS hosszkorlátozás ellenőrzéséhez.
"""

uzenet = input("Írj egy üzenetet:")

uzenenet_hossza = uzenet.__len__()
uzenenet_hosszaB = len(uzenet)

print(f"Az üzeneted hossza:{uzenenet_hossza} karakter")
print(f"Az üzeneted hossza:{uzenenet_hosszaB} karakter")