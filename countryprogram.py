import requests

def find_befolkning_og_flag():
    country = input("Indtast et land: ")
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Fejl: Kunne ikke finde data for '{country}'.")
        return

    data = response.json()
    if not data:
        print("Ingen data fundet.")
        return

    land_info = data[0]
    befolkning = land_info.get("population", "Ukendt")

    print(f"Befolkning i {country}: {befolkning}")

find_befolkning_og_flag()