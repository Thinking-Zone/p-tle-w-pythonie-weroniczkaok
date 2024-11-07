import random
pogoda= random. choice([1,0])

while True:
    odpowiedz = input("czy pada? (tak/nie): ").strip().lower()
    if (odpowiedz == "tak" and pogoda ==1) or (odpowiedz == "nie" and pogoda == 0):
        print("yay zgadłeś!")
        break
    else:
        print("niepoprawna odp." )
