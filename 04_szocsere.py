"""Szó cseréje másikra – ételrendelés módosítása
Feladat: A rendelésben az „alma” helyett cseréld „körtére”, ha a boltban nincs alma.
"""

rendeles = input("Add meg a rendelésed és kicserélem az almát körtére vagy a körtét almára. \n")

if "alma" in rendeles:
    valtozott = rendeles.replace("alma", "körte")

    print(f"megváltozott rendelés: {valtozott}  ")


elif "körte" in rendeles:
    valtozott2 = rendeles.replace("körte", "alma")

    print(f"megváltozott rendelés: {valtozott2} ")
