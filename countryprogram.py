import requests
import tkinter as tk
from tkinter import messagebox

# Indsæt din API-nøgle her
API_KEY = "C569ZZph5JtB6kqrbZ+IZg==leBwkjfo89yV29gW"

def hent_befolkning():
    land_navn = input_felt.get().strip()
    if not land_navn:
        messagebox.showwarning("Advarsel", "Indtast venligst et land.")
        return

    url = f"https://api.api-ninjas.com/v1/population?country={land_navn}"

    headers = {
        "X-Api-Key": API_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if "population" in data:
            befolkning = data["population"]
            resultat_label.config(text=f"Befolkningstal for {land_navn.title()}:\n{befolkning:,} personer")
        else:
            resultat_label.config(text="Ingen befolkningstal fundet for det angivne land.")
    except requests.exceptions.RequestException as e:
        resultat_label.config(text=f"Fejl ved forespørgsel:\n{e}")

# GUI-opsætning
root = tk.Tk()
root.title("Landets Befolkning")
root.geometry("400x220")
root.configure(padx=20, pady=20)

tk.Label(root, text="Indtast et land:").pack()
input_felt = tk.Entry(root, width=40)
input_felt.pack(pady=5)

søg_knap = tk.Button(root, text="Søg", command=hent_befolkning)
søg_knap.pack(pady=10)

resultat_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=350, justify="center")
resultat_label.pack(pady=10)

root.mainloop()
