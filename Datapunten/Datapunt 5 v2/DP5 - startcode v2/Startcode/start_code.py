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
bestand_pad = Path(__file__).parent / 'persoonlijke_voorkeuren_bezoeker_3.json'

# open het JSON-bestand 
json_bestand = open(bestand_pad)
 
# zet het om naar een Python-dictionary
json_dict = json.load(json_bestand)

# nu kunnen we het gebruiken als een dict! dit is "dataset #1"
print(json_dict["naam"]) 
typeattractievoorkeur = json_dict["voorkeuren_attractietypes".lower()]

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

#lege lijst van gekozen voorzieningen
gekozen_voorziening = []


tijd_over = json_dict["verblijfsduur"]
persoons_lievelingsattractie = json_dict["lievelings_attracties"]

#bijhouden of de voorziening al in de lijst staat
voorziening_bijhouden = set()

#bijhouden hoevaak de lievelings attractie voorkomt
aantal_lievelingsattractie = []

#voorzieningen splitten in 3 lijsten

lievelingsattracties = []
andere_attracties = []
winkels_en_horeca = []

for voorkeuren in list_met_voorzieningen:
    if voorkeuren["type"].lower() == typeattractievoorkeur:
        lievelingsattracties.append(voorkeuren)
    elif voorkeuren["type"].lower() == "winkels" or voorkeuren["type"].lower() == "horeca":
        winkels_en_horeca.append(voorkeuren)
    else: 
        andere_attracties.append(voorkeuren)



#voegt attracties aan het dagprogramma
def attracties_toevoegen (list_met_voorzieningen):
    global tijd_over
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

     if  voorkeuren["naam"] not in voorziening_bijhouden :
      gekozen_voorziening.append(voorkeuren) 
      voorziening_bijhouden.add(voorkeuren["naam"])
      tijd_over -= totale_tijd_nodig


attracties_toevoegen(lievelingsattracties)

attracties_toevoegen(andere_attracties)

print(gekozen_voorziening)
   

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

