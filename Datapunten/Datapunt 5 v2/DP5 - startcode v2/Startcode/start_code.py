from pathlib import Path
import json
from database_wrapper import Database

def overzicht_attracties():
    # altijd verbinding openen om query's uit te voeren
    db.connect()

    select_query = "SELECT naam, type, geschatte_wachttijd, doorlooptijd, attractie_min_lengte, attractie_max_lengte, attractie_min_leeftijd, attractie_max_gewicht FROM voorziening"
    results = db.execute_query(select_query)

    # altijd verbinding sluiten met de database als je klaar bent
    db.close()

    return results

# maak zoals gewoonlijk connectie met de database
db = Database(host="localhost", gebruiker="user", wachtwoord="password", database="attractiepark_software")

# navigeer naar het JSON-bestand, let op: er zijn ook andere persoonlijke voorkeuren om te testen! en maak vooral ook je eigen persoonlijke voorkeuren :-)
bestand_pad = Path(__file__).parent / 'persoonlijke_voorkeuren_bezoeker_1.json'

# open het JSON-bestand 
json_bestand = open(bestand_pad)
 
# zet het om naar een Python-dictionary
json_dict = json.load(json_bestand)

# nu kunnen we het gebruiken als een dict! dit is "dataset #1"
print(json_dict["naam"]) 
typeattractievoorkeur = str(print(json_dict["voorkeuren_attractietypes"]))

# en haal alle voorzieningen op, dit is een lijst met dicts. dit is "dataset #2"
list_met_voorzieningen = overzicht_attracties()
print()

#print("Eerste rij:")
#print(list_met_voorzieningen[0]["type"])

json_bestand.close() # sluit het bestand indien niet meer nodig

# DE OPDRACHT
# Met die 2 datasets moet je tot een persoonlijke programma komen voor de bezoeker
# Zorg dat je een algoritme ontwikkelt, conform eisen in het ontwerpdocument
# Zorg dat het persoonlijke programma genereert/output naar een .json bestand, dat weer ingelezen kan worden in een webomgeving (zie acceptatieomgeving website folder)
# Hieronder een begin...

# dit moet worden gevuld door een algoritme

voorkeuren = str("")

gekozen_voorziening = []

tijd_over = json_dict["verblijfsduur"]


for voorkeuren in list_met_voorzieningen :

    totale_tijd_nodig = voorkeuren["geschatte_wachttijd"] + voorkeuren["doorlooptijd"]
   
    if totale_tijd_nodig > tijd_over:
        continue
    
    if voorkeuren["attractie_min_lengte"] and json_dict["lengte"] < voorkeuren["attractie_min_lengte"]:
        continue
    if voorkeuren["attractie_max_lengte"] and json_dict["lengte"] > voorkeuren["attractie_max_lengte"]:
        continue
    if voorkeuren["attractie_min_leeftijd"] and json_dict["leeftijd"] < voorkeuren["attractie_min_leeftijd"]:
        continue
    if voorkeuren["attractie_max_gewicht"] and json_dict["gewicht"] > voorkeuren["attractie_max_gewicht"]:
        continue

    gekozen_voorziening.append(voorkeuren) 
    tijd_over -= totale_tijd_nodig


    
    
  
        
print(gekozen_voorziening)
    
 #   if (voorkeuren.lower()) == (typeattractievoorkeur.lower()) :
 #       continue
 #   print(voorkeuren, "Is de zelfde type")
   

  

    




dagprogramma = {
    "voorkeuren": {
      "naam" : json_dict["naam"],
      "gender" : json_dict["gender"],
      "leeftijd" : json_dict["leeftijd"],
      "voorkeuren eten" : json_dict["voorkeuren_eten"],
      "voorkeuren type attracties" : json_dict["voorkeuren_attractietypes"],
      "lievelings attracties" : json_dict["lievelings_attracties"],
      "verblijfsduur" : json_dict ["verblijfsduur"]



    },
     "voorzieningen": [
        
        
    ]
}

for gekozen_lijst in gekozen_voorziening :
    dagprogramma["voorzieningen"].append(gekozen_lijst)

# uiteindelijk schrijven we de dictionary weg naar een JSON-bestand
with open('persoonlijk_programma_bezoeker_x.json', 'w') as json_bestand:
    json.dump(dagprogramma, json_bestand)

