from database_wrapper import Database
from tkinter_wrapper import Scherm

# database aanmaken. 
db = Database(host="localhost", gebruiker="user", wachtwoord="password", database="attractiepark_software")
db.connect()

print()

# scherm aanmaken. Je mag de grootte van het scherm aanpassen.
scherm = Scherm("Attractie beheer", 1200, 800)

# attributen van een attractie
# deze attributen worden gebruikt om de tabel te maken en de juiste types mee te geven bij het bewerken scherm.
attributen_attractie = [
    {"naam": "Id",  "type": "int", "read-only": True},
    {"naam": "Naam", "type": "string", "verplicht": True},
    {"naam": "Type", "type": "options", "opties": ["Achtbaan", "Water", "Draaien", "Familie", "Simulator"], "verplicht": True},
    {"naam": "Minimale lengte", "type": "float"},
    {"naam": "Maximale lengte", "type": "float"},
    {"naam": "Minimale leeftijd", "type": "int"},
    {"naam": "Maximale gewicht", "type": "int"},
    {"naam": "Overdekt", "type": "boolean", "verplicht": True},
    {"naam": "Gem. wachttijd", "type": "int","verplicht": True},
    {"naam": "Doorlooptijd", "type": "int", "verplicht": True},
    {"naam": "Actief", "type": "boolean","verplicht": True},
]

attributen_horeca = [
     {"naam": "Id",  "type": "int", "read-only": True},
    {"naam": "Naam", "type": "string", "verplicht": True},
    {"naam": "Type", "type": "options", "opties": ["Horeca", "Winkel"], "verplicht": True},
    {"naam": "Overdekt", "type": "boolean", "verplicht": True},
    {"naam": "Gem. wachttijd", "type": "int","verplicht": True},
    {"naam": "Doorlooptijd", "type": "int", "verplicht": True},
    {"naam": "Actief", "type": "boolean","verplicht": True},
    {"naam": "Productaanbod", "type": "string", "verplicht": True}

]



def attracties_ophalen():
    
    Attractieresults = db.execute_query('SELECT id, naam, type, overdekt, geschatte_wachttijd, doorlooptijd, actief, attractie_min_lengte, attractie_max_lengte, attractie_min_leeftijd, attractie_max_gewicht FROM voorziening WHERE NOT type = "horeca" AND NOT type = "winkel" ;')
    # vervang de voorbeeld data, door data uit de database.
    return Attractieresults

def horeca_ophalen():

    Horecaresults = db.execute_query('SELECT id, naam, type, overdekt, geschatte_wachttijd, doorlooptijd, actief, productaanbod FROM voorziening WHERE type = "horeca" OR type = "winkel" ORDER BY type = "horeca"')
    return Horecaresults




def voorziening_bewerken(bewerkte_voorziening, rij_index):
    print(f"Gewijzigde voorziening: {bewerkte_voorziening}")
    
   
def voorziening_verwijderen(verwijderde_voorziening, rij_index):
    print(f"Verwijderde voorziening: {verwijderde_voorziening}")


# attracties ophalen
attracties = attracties_ophalen()
horeca_gelegenheden = horeca_ophalen()

# tabel aan het scherm toevoegen. Je mag de titel en locatie van de tabel aanpassen.
attractie_tabel = scherm.voeg_tabel_toe("Attracties", attributen_attractie, attracties, 0, 0, 1000, 300, voorziening_bewerken, voorziening_verwijderen)

horeca_tabel = scherm.voeg_tabel_toe("Winkels en Horeca", attributen_horeca , horeca_gelegenheden , 0, 350, 1000, 300, voorziening_bewerken, voorziening_verwijderen)



scherm.open()
    