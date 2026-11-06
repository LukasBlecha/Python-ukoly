# Úvodní příběh a instrukce pro císařský dvůr
print("=== FIBONACCI NA DVOŘE FRIDRICHA II. == simulace množení králíků ===")
print("Píše se 13. století. Císař Fridrich II. zkoumá růst populace na svém královském ostrově.\n")

# Vstup od uživatele: počet měsíců simulace
pocet_mesicu = int(input("Zadej počet měsíců simulace (např. 1 až 12): "))

# Inicializace proměnných pro Fibonacciho posloupnost
# a = počet párů v předchozím měsíci, b = počet párů v aktuálním měsíci
a = 1
b = 1
mesic = 1

print("\n--- VÝVOJ POPULACE KRÁLÍKŮ ---")

# Výpočet pomocí cyklu while
while mesic <= pocet_mesicu:
    # Pro první dva měsíce je počet párů fixně 1 (podle pravidel)
    if mesic == 1 or mesic == 2:
        aktualni_pary = 1
    else:
        # Výpočet dalšího členu pomocí dočasné (pomocné) proměnné
        dopredu = a + b
        a = b
        b = dopredu
        aktualni_pary = b

    # Vizualizace: vykreslení čísla měsíce, počtu párů a emoji králíka (násobení řetězce)
    kralici_emoji = "🐰" * aktualni_pary
    print(f"Měsíc {mesic:2d}: {aktualni_pary:3d} pár(ů) králíků -> {kralici_emoji}")

    # Zvětšování čítače měsíců, aby cyklus Neskončil v nekonečné smyčce
    mesic += 1

print("\nSimulace pro císaře Fridricha II. byla úspěšně dokončena!")