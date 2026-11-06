# Úvodní instrukce pro uživatele
print("=== HRA: Počítač háže číslo ===")
print("Mysli si číslo od 1 do 100. Já (počítač) se ho pokusím uhodnout.")
print("Odpovídej podle pokynů:")
print("  v - pokud je tvé číslo VĚTŠÍ než můj tip")
print("  m - pokud je tvé číslo MENŠÍ než můj tip")
print("  s - pokud je můj tip SPRÁVNĚ\n")

# Zavedení hranic intervalu a proměnných
dole = 1
nahore = 100
pokusy = 0
odpoved = ""

# Spuštění cyklu while
while odpoved != "s":
    # Výpočet středu intervalu jako tipu
    tip = (dole + nahore) // 2
    
    # Přičtení 1 k počítadlu pokusů
    pokusy += 1
    
    # Výpis tipu počítače a vyžádání odpovědi
    print(f"Pokus č. {pokusy}: Můj tip je {tip}")
    odpoved = input("Zadej odpověď (v / m / s): ").strip().lower()
    
    # Úprava hranic pomocí podmínek if / elif / else
    if odpoved == "v":
        dole = tip + 1
    elif odpoved == "m":
        nahore = tip - 1
    elif odpoved == "s":
        print("\nSkvěle! Uhodl jsem tvé číslo.")
    else:
        print("Neplatná odpověď! Zadej prosím pouze 'v', 'm' nebo 's'.")

# Po ukončení cyklu vypis celkový počet pokusů
print(f"Celkový počet pokusů, které jsem potřeboval: {pokusy}")
