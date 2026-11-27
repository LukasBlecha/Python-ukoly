
# převod DEC do jiné číselné soustavy
def fromDEC(cislo, zaklad):    # zaklad HEX je 16, zaklad BIN je 2
    prevedene_cislo = ""
    while cislo > 0:
        zbytek = cislo % zaklad
        cislo //= zaklad       #  cislo = cislo // zaklad
        prevedene_cislo = str(zbytek) + prevedene_cislo
    return prevedene_cislo

print(fromDEC(6,2))      # prevedu 6 na dvojkové číslo
print(fromDEC(255,16))     # prevedu 6 na HEX číslo

def cifra_na_znak(hodnota):
    if hodnota >= 0 and hodnota <= 9:
        return str(hodnota)
    elif hodnota == 10:
        return "A"
    elif hodnota == 11:
        return "B"
    elif hodnota == 12:
        return "C"
    elif hodnota == 13:
        return "D"
    elif hodnota == 14:
        return "E"
    elif hodnota == 15:
        return "F"
    else:
        return ""


def je_platny_zaklad_it(zaklad):
    return zaklad == 2 or zaklad == 8 or zaklad == 16


def preved_soustavu(cislo, zaklad):
    if cislo < 0:
        return None
    if not je_platny_zaklad_it(zaklad):
        return None
    if cislo == 0:
        return "0"

    vysledek = ""
    while cislo > 0:
        zbytek = cislo % zaklad
        cifra = cifra_na_znak(zbytek)
        vysledek = cifra + vysledek
        cislo = cislo // zaklad

    return vysledek


# --- Část 2: Hlavní tělo programu ---

od_cisla = 0
do_cisla = 20

print("\nDEC | BIN      | OCT | HEX")
print("----------------------------")

aktualni = od_cisla
while aktualni <= do_cisla:
    bin_val = preved_soustavu(aktualni, 2)
    oct_val = preved_soustavu(aktualni, 8)
    hex_val = preved_soustavu(aktualni, 16)
    print(str(aktualni) + " | " + bin_val + " | " + oct_val + " | " + hex_val)
    aktualni = aktualni + 1

print("\nTest neplatného čísla:", preved_soustavu(-5, 2))
print("Test neplatného základu:", preved_soustavu(10, 5))