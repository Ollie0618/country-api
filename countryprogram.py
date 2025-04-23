import requests

def search_api(country):
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return

    data = response.json()
    if not data:
        return

    land_info = data[0]
    return land_info


    
country = input("Indtast et land: ")
result = search_api(country)
if result == None:
    print("Ingen data fundet.")

befolkning = result.get("population", "Ukendt")
print(f"Befolkning i {country}: {befolkning}")