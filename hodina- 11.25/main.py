def ctverec(strana):
    """A: Vyplněný čtverec."""
    if strana <= 0: return None
    r = 0
    while r < strana:
        print("*" * strana)
        r += 1


def obdelnik(a, b):
    """B: Vyplněný obdélník (a = šířka, b = výška)."""
    if a <= 0 or b <= 0: return None
    r = 0
    while r < b:
        print("*" * a)
        r += 1


def nevyplneny_ctverec(strana):
    """C: Nevyplněný čtverec."""
    if strana <= 0: return None
    r = 0
    while r < strana:
        # Horní a dolní hrana plná, jinak kraje '*' a uprostřed mezery
        print("*" * strana if r in (0, strana - 1) else "*" + " " * max(0, strana - 2) + ("*" if strana > 1 else ""))
        r += 1


def nevyplneny_obdelnik(a, b):
    """D: Nevyplněný obdélník (a = šířka, b = výška)."""
    if a <= 0 or b <= 0: return None
    r = 0
    while r < b:
        print("*" * a if r in (0, b - 1) else "*" + " " * max(0, a - 2) + ("*" if a > 1 else ""))
        r += 1


def levy_trojuhelnik(zakladna):
    """E: Levý pravoúhlý trojúhelník."""
    if zakladna <= 0: return None
    r = 1
    while r <= zakladna:
        print("*" * r)
        r += 1


def pravy_trojuhelnik(zakladna):
    """F: Pravý pravoúhlý trojúhelník."""
    if zakladna <= 0: return None
    r = 1
    while r <= zakladna:
        print(" " * (zakladna - r) + "*" * r)
        r += 1


def rovnoramenny_trojuhelnik(zakladna):
    """G: Rovnoramenný trojúhelník (lichá i sudá základna)."""
    if zakladna <= 0: return None
    # Liché začínají na 1 hvězdičce, sudé na 2
    hv = 1 if zakladna % 2 else 2
    while hv <= zakladna:
        print(" " * ((zakladna - hv) // 2) + "*" * hv)
        hv += 2


def hlavni_program():
    """Hlavní smyčka programu."""
    print("VÍTEJ V PROGRAMU PRO KRESLENÍ GEOMETRICKÝCH TVARŮ")
    while True:
        volba = input("Jaký obrazec chceš vykreslit? (c, o, cn, on, tpl, tpp, tr): ").strip().lower()
        res = None
        if volba in ("c", "cn"):
            s = int(input("Jak velká má být jeho strana? "))
            res = ctverec(s) if volba == "c" else nevyplneny_ctverec(s)
        elif volba in ("o", "on"):
            a, b = int(input("Zadej a: ")), int(input("Zadej b: "))
            res = obdelnik(a, b) if volba == "o" else nevyplneny_obdelnik(a, b)
        elif volba in ("tpl", "tpp", "tr"):
            z = int(input("Zadej délku základny / výšku: "))
            res = levy_trojuhelnik(z) if volba == "tpl" else (pravy_trojuhelnik(z) if volba == "tpp" else rovnoramenny_trojuhelnik(z))
        else:
            print("Neznámý obrazec.")

        if volba in ("c", "o", "cn", "on", "tpl", "tpp", "tr") and res is None:
            print("Rozměr musí být větší než 0.")

        if input("Chceš vykreslit další obrazec? ").strip().lower() != "ano":
            break
    print("DĚKUJI ZA POUŽITÍ PROGRAMU")


if __name__ == "__main__":
    hlavni_program()

