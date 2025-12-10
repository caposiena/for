# ESERCIZIO: stampa nomi con numero d'ordine usando enumerate()

nomi = ["Alice", "Bob", "Carla", "Diego"]

for numero, nome in enumerate(nomi, start=1):
    print(f"{numero}. {nome}")
