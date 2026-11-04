import random

def spustit_hru():
    # Krok 1: Priprava nahodneho cisla
    tajne_cislo = random.randint(1, 20)
    pokusy = 0
    max_pokusu = 5
    tip = 0

    print("==================================")
    print("   Vitej ve hre UHADNI CISLO!     ")
    print("==================================")
    print(f"Myslim si cislo od 1 do 20.")
    print(f"Mas k dispozici maximalne {max_pokusu} pokusu. Hodne stesti!\n")

    # Hlavni cyklus hry (Cil A: hlida se i pocet pokusu)
    while tip != tajne_cislo and pokusy < max_pokusu:
        try:
            # Nacitani vstupu od uzivatele
            tip = int(input(f"Pokus {pokusy + 1}/{max_pokusu} - Zadej svuj tip: "))
        except ValueError:
            print("Neplatny vstup! Zadej prosim cele cislo.")
            continue

        # Cil B: Kontrola rozsahu vstupu (neplatny tip se nezapocita)
        if tip < 1 or tip > 20:
            print("Zadal jsi cislo mimo rozsah (1–20)!\n")
            continue

        # Pocitadlo pokusu (zapocita se az po ucesne kontrole rozsahu)
        pokusy += 1

        # Porovnani tipu s tajemnym cislem (podminky if / elif / else)
        if tip < tajne_cislo:
            print("Moje cislo je VETSI!\n")
        elif tip > tajne_cislo:
            print("Moje cislo je MENSI!\n")
        else:
            # Uspesne uhodnuti
            print(f"\nGratuluji! Uhodl jsi cislo {tajne_cislo} na {pokusy}. pokus.")
            break

    # Kontrola prohry – pokud cyklus skoncil a hrac neuhodl
    if tip != tajne_cislo:
        print(f"\nBohuzel ti dosly pokusy! Tajne cislo bylo {tajne_cislo}.")

# Spusteni hry
if __name__ == "__main__":
    spustit_hru()
