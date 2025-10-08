"""Kis- és nagybetűssé alakítás – névformázás
Feladat: Kérj be egy felhasználónevet a regisztrációhoz, majd jelenítsd meg háromféleképpen:
nagybetűs (pl. címkén vagy azonosítóban),


kisbetűs (pl. email összehasonlításhoz),


csak az első betű nagy (személyes üdvözlésnél).
"""

felhasznalonev = input("Adj meg egy felhasználónevet")

nagybetus = felhasznalonev.upper()
print(f"Csupa nagybetűs:{nagybetus}")

kisbetus = felhasznalonev.lower()
print(f"Csupa kisbetűs: {kisbetus}")

nagykezdobetus = felhasznalonev.capitalize()
print(f"Nagy kezdőbetűs: {nagykezdobetus}")
