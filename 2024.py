print("Scegli la figura geometrica da calcolare \n")
print("1 per quadrato \n")
print("2 per cerchio \n")
print("3 per rettangolo \n")

scelta = input("Inserisci il numero corrispondente alla figura geometrica: ")

if scelta  == "1":
    lato = int(input("Inserisci la lunghezza del lato: "))
    perimetro = lato * 4
    print(f"Il perimetro del quadrato è: {perimetro}")

elif scelta  == "2":
    raggio = int(input("Inserisci il raggio del cerchio: "))
    pigreco = 3.14
    circonferenza = 2 * pigreco * raggio
    print(f"Il perimetro del quadrato è: {circonferenza}")

elif scelta  == "3":
    base = int(input("Inserisci la base del rettangolo: "))
    altezza = int(input("Inserisci l'altezza del rettangolo: "))
    perimetro = base*2 + altezza*2
    print(f"Il perimetro del quadrato è: {perimetro}")
       



