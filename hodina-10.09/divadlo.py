# Zakladni cena jedne vstupenky
zakladni_cena = 500

# Vstupy od uzivatele
vek = float(input("Zadej vek navstevnika: "))
pocet_osob = int(input("Zadej pocet osob: "))

# Otazka na studenta se objevi jen tehdy, pokud ma navstevnik mene než 26 let
if vek < 26:
    student = input("Je student? (ano nebo ne): ")
else:
    student = "ne"  # Pokud je starsi, nemusi se ptat, automaticky neni student

# Urceni slevy podle podminek
if pocet_osob >= 4:
    nazev_slevy = "Rodinna sleva"
    procento_slevy = 0.25
elif student == "ano" and vek < 26:
    nazev_slevy = "Studentska sleva"
    procento_slevy = 0.30
elif vek >= 65:
    nazev_slevy = "Seniorska sleva"
    procento_slevy = 0.20
else:
    nazev_slevy = "Bez slevy"
    procento_slevy = 0.0

# Vypocet cen
cena_za_jednu = zakladni_cena * (1 - procento_slevy)
celkova_cena = cena_za_jednu * pocet_osob

# Vysledek
print("--- Vysledek ---")
print("Typ slevy:", nazev_slevy)
print("Cena za 1 listek:", cena_za_jednu, "Kc")
print("Celkova cena za vsechny listky:", celkova_cena, "Kc")