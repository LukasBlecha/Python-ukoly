import urllib.request
url = "https://voskh.cz/envirotyden/index.php?lokalita=kutnahora"

odpoved = urllib.request.urlopen(url)  # zahájení komunikace (odkaz na komunikační objekt)
celkem_srazky = 0
pocet_dni = 0
radek = odpoved.readline()             # přečtení bajtů řádku (až do kodu 13)

while bool(radek):
   text_radku =  radek.decode("utf-8") # string
   denni_srazky = float(text_radku)    # float číslo
   if denni_srazky >= 0:
       celkem_srazky += denni_srazky
       pocet_dni += 1
   radek = odpoved.readline()

odpoved.close()                        # ukončení komunikace
print(celkem_srazky / pocet_dni)

