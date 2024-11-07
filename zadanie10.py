#Napisz program, który:
#Wczytuje od użytkownika dwie liczby: a i b, które określają zakres (od a do b włącznie).
#Następnie, program ma zliczyć ile liczb parzystych oraz ile liczb nieparzystych znajduje się w tym zakresie (włącznie).
#Program wypisuje wynik na ekranie w postaci:
#Liczba liczb parzystych: X
#Liczba liczb nieparzystych: Y


a = int(input("Podaj pierwszą liczbę (a): "))
b = int(input("Podaj drugą liczbę (b): "))


parzyste = 0
nieparzyste = 0


for i in range(a, b + 1):
    if i % 2 == 0:
        parzyste += 1  
    else:
        nieparzyste += 1  


print(f"Liczba liczb parzystych: {parzyste}")
print(f"Liczba liczb nieparzystych: {nieparzyste}")

