import random
getal = random.randint(1,10)
pogingen = 0

while True:
    gok= int(input("Raad het getal tussen 1 en 10: "))
    pogingen += 1
    if gok == getal:
        print(f"Gefeliciteerd! Je hebt het getal {getal} geraden in {pogingen} pogingen.")
        break
    elif gok < getal:
        print("Hoger!")
    else:
        print("Lager!")
        

