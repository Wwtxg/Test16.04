zbozi = ["NVIDIA RTX 3070", "NVIDIA RTX 3070Ti", "NVIDIA RTX 3080", "NVIDIA RTX 3080Ti", "NVIDIA RTX 3090", "NVIDIA RTX 3090Ti"]

kosik = []

print ("-------------------------")

print ("Vitam v konfiguratoru PC")

print ("-------------------------")

def vypis_zbozi(zbozi):
    for x in range(len(zbozi)):
       print (f"{x+1} {zbozi[x]}")

def vypis_kosik(kosik):
    for x in range(len(kosik)):
       print (f"{x+1} {kosik[x]}")

print ("Zde si vyberte z naseho zbozi")
print ("Vybirat muzete pomoci nazvu nebo cisla")
print ("Pro vyber podle nazvu = 1, podle cisla = 2")
print ("Pro ukonceni zadejte prikaz dost")

print ("-------------------------")

moznost = int(input("Zadejte moznost vyberu: "))

print ("-------------------------")

if moznost == 1:
    for x in range (len(zbozi)):
        print ("Nabitka:")

        vypis_zbozi(zbozi)

        nazev_zbozi = str(input("Nazev zbozi: "))

        kosik.append (nazev_zbozi)

        zbozi.remove (nazev_zbozi)

        vypis_zbozi(zbozi)

        print ("Vas kosik: ")

        vypis_kosik(kosik)

        if not zbozi:
            print ("Seznam zbozi je prazdny")
            break

        Pokracovat = str(input("Chcete Pokracovat? Pro ukonceni zadejte prikaz dost: "))

        if Pokracovat == "dost":
            break

if moznost == 2:
    for x in range (len(zbozi)):
        print ("Nabitka:")

        vypis_zbozi(zbozi)

        cislo_zbozi = int(input("Cislo zbozi: "))

        kosik.append (zbozi[cislo_zbozi-1])

        zbozi.remove (zbozi[cislo_zbozi-1])

        vypis_zbozi(zbozi)

        print ("Vas kosik: ")

        vypis_kosik(kosik)

        if not zbozi:
            print ("Seznam zbozi je prazdny")
            break

        Pokracovat = str(input("Chcete Pokracovat? Pro ukonceni zadejte prikaz dost: "))

        if Pokracovat == "dost":
            break

#KONEC
if moznost == 3:
    for x in range (len(zbozi)):
        print ("Nabitka:")

        vypis_zbozi(zbozi)

        cislo_zbozi = int(input("Zbozi: "))

        if cislo_zbozi == 1 or 2 or 3 or 4 or 5 or 6:
            int(cislo_zbozi)
        else:
            str(cislo_zbozi)

        if cislo_zbozi == int:
            kosik.append (zbozi[cislo_zbozi-1])

            zbozi.remove (zbozi[cislo_zbozi-1])

        if cislo_zbozi == str:
            kosik.append (cislo_zbozi)

            zbozi.remove (cislo_zbozi)

        vypis_zbozi(zbozi)

        print ("Vas kosik: ")

        vypis_kosik(kosik)

        if not zbozi:
            print ("Seznam zbozi je prazdny")
            break

        Pokracovat = str(input("Chcete Pokracovat? Pro ukonceni zadejte prikaz dost: "))

        if Pokracovat == "dost":
            break