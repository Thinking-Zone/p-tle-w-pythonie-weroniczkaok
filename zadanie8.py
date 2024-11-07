nie_count = 0

while True:
   
    odpowiedz = input("Czy pada? (tak/nie/nie wiem): ").strip().lower()

   
    if odpowiedz == "tak":
        break 
    elif odpowiedz == "nie":
        nie_count += 1 
    elif odpowiedz == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.") 
    else:
        print("Nie rozumiem odpowiedzi. Proszę wpisać 'tak', 'nie' lub 'nie wiem'.")


print(f"Liczba odpowiedzi 'nie': {nie_count}")
