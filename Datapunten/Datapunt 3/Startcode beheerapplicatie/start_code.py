from database_wrapper import Database
from tkinter_wrapper import Scherm

# database aanmaken. 
db = Database(host="localhost", gebruiker="user", wachtwoord="password", database="attractiepark_software")
db.connect()

# scherm aanmaken. Je mag de grootte van het scherm aanpassen.
scherm = Scherm("Attractie beheer", 1250, 800)

# attributen van een attractie
# deze attributen worden gebruikt om de tabel te maken en de juiste types mee te geven bij het bewerken scherm.
attributen_attractie = [
    {"naam": "Id",  "type": "int", "read-only": True},
    {"naam": "Naam", "type": "string", "verplicht": True},
    {"naam": "Type", "type": "options", "opties": ["Achtbaan", "Water", "Draaien", "Familie", "Simulator"], "verplicht": True},
    {"naam": "Overdekt", "type": "boolean", "verplicht": True},
    {"naam": "Gem. wachttijd", "type": "int","verplicht": True},
    {"naam": "Doorlooptijd", "type": "int", "verplicht": True},
    {"naam": "Actief", "type": "boolean","verplicht": True},
    {"naam": "Minimale lengte", "type": "float"},
    {"naam": "Maximale lengte", "type": "float"},
    {"naam": "Minimale leeftijd", "type": "int"},
    {"naam": "Maximale gewicht", "type": "int"},
   
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




def voorziening_bewerken(Toegevoegde_voorziening,):
     if "Productaanbod" in Toegevoegde_voorziening:
        bewerk_query_horeca = """
        UPDATE voorziening 
        SET 
        naam = %s, 
        type = %s, 
        overdekt = %s, 
        geschatte_wachttijd = %s, 
        doorlooptijd = %s, 
        actief = %s, 
        productaanbod = %s
        WHERE 
        id = %s
        """
        params = (
            Toegevoegde_voorziening["Naam"],  
            Toegevoegde_voorziening["Type"],  
            1 if Toegevoegde_voorziening["Overdekt"] else 0,  
            Toegevoegde_voorziening["Gem. wachttijd"],  
            Toegevoegde_voorziening["Doorlooptijd"],  
            1 if Toegevoegde_voorziening["Actief"] else 0,  
            Toegevoegde_voorziening["Productaanbod"],
            Toegevoegde_voorziening["Id"],
        )
 
        db.execute_query(bewerk_query_horeca, params)
        scherm.herlaad_tabel(horeca_tabel, horeca_ophalen())
    
     else:
        bewerk_query_attractie = """
        UPDATE voorziening 
        SET 
        naam = %s, 
        type = %s, 
        overdekt = %s, 
        geschatte_wachttijd = %s, 
        doorlooptijd = %s, 
        actief = %s, 
        attractie_min_lengte = %s, 
        attractie_max_lengte = %s, 
        attractie_min_leeftijd = %s, 
        attractie_max_gewicht = %s
        WHERE 
        id = %s
        """

        params = (
            Toegevoegde_voorziening["Naam"],  
            Toegevoegde_voorziening["Type"],  
            1 if Toegevoegde_voorziening["Overdekt"] else 0,  
            Toegevoegde_voorziening["Gem. wachttijd"],  
            Toegevoegde_voorziening["Doorlooptijd"],  
            1 if Toegevoegde_voorziening["Actief"] else 0,  
            Toegevoegde_voorziening["Minimale lengte"],
            Toegevoegde_voorziening["Maximale lengte"],
            Toegevoegde_voorziening["Maximale lengte"],
            Toegevoegde_voorziening["Maximale gewicht"],
            Toegevoegde_voorziening["Id"],
        )
 
        db.execute_query(bewerk_query_attractie, params)
 
        scherm.herlaad_tabel(attractie_tabel,attracties_ophalen())
        scherm.herlaad_tabel(horeca_tabel, horeca_ophalen())
        print(f"Gewijzigde voorziening: {Toegevoegde_voorziening}")

    
   
def voorziening_verwijderen(verwijderde_voorziening, rij_index):

    antwoord =  scherm.toon_vraag_ja_nee_venster("Voorziening Verwijderen", "Weet je zeker?")

    if antwoord == True :

        db.execute_query("DELETE FROM voorziening WHERE id = %s", (verwijderde_voorziening["Id"],))
        scherm.toon_informatie_bericht("Let op!", "Voorziening is verwijderd.")
    

        print(f"Verwijderde voorziening: {verwijderde_voorziening}")
        scherm.herlaad_tabel(attractie_tabel,attracties_ophalen())
        scherm.herlaad_tabel(horeca_tabel, horeca_ophalen())
    
    else:
       scherm.toon_informatie_bericht("Let op!", "Voorziening niet verwijderd.")
       print("Niks is gewijzigd")


def Toevoegen_voorziening(Toegevoegde_voorziening,):
    if "Productaanbod" in Toegevoegde_voorziening:
        bewerk_query_horeca = """
        INSERT INTO voorziening (naam, type, overdekt, geschatte_wachttijd, doorlooptijd, actief, productaanbod)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        
        """
        params = (
            Toegevoegde_voorziening["Naam"],  
            Toegevoegde_voorziening["Type"],  
            1 if Toegevoegde_voorziening["Overdekt"] else 0,  
            Toegevoegde_voorziening["Gem. wachttijd"],  
            Toegevoegde_voorziening["Doorlooptijd"],  
            1 if Toegevoegde_voorziening["Actief"] else 0,  
            Toegevoegde_voorziening["Productaanbod"],
        )
 
        db.execute_query(bewerk_query_horeca, params)
        scherm.herlaad_tabel(horeca_tabel, horeca_ophalen())
    
    else:
        bewerk_query_attractie = """
        INSERT INTO voorziening (naam, type, overdekt, geschatte_wachttijd, doorlooptijd, actief, attractie_min_lengte, attractie_max_lengte, attractie_min_leeftijd, attractie_max_gewicht)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        
        """

        params = (
            Toegevoegde_voorziening["Naam"],  
            Toegevoegde_voorziening["Type"],  
            1 if Toegevoegde_voorziening["Overdekt"] else 0,  
            Toegevoegde_voorziening["Gem. wachttijd"],  
            Toegevoegde_voorziening["Doorlooptijd"],  
            1 if Toegevoegde_voorziening["Actief"] else 0,  
            Toegevoegde_voorziening["Minimale lengte"],
            Toegevoegde_voorziening["Maximale lengte"],
            Toegevoegde_voorziening["Maximale lengte"],
            Toegevoegde_voorziening["Maximale gewicht"],
        )
 
        db.execute_query(bewerk_query_attractie, params)
 
        scherm.herlaad_tabel(attractie_tabel,attracties_ophalen())
        scherm.herlaad_tabel(horeca_tabel, horeca_ophalen())
        print(f"toegevoegde voorziening: {Toegevoegde_voorziening}")
   
   
   


      
    
    

# attracties ophalen
attracties = attracties_ophalen()
horeca_gelegenheden = horeca_ophalen()

# tabel aan het scherm toevoegen. Je mag de titel en locatie van de tabel aanpassen.
attractie_tabel = scherm.voeg_tabel_toe("Attracties", attributen_attractie, attracties, 0, 0, 1000, 300, voorziening_bewerken, voorziening_verwijderen )

horeca_tabel = scherm.voeg_tabel_toe("Winkels en Horeca", attributen_horeca , horeca_gelegenheden , 0, 350, 1000, 300, voorziening_bewerken, voorziening_verwijderen)

#toevoeg knopjes

scherm.voeg_nieuwe_voorziening_knop_toe("Toevoegen attractie", 1050, 50, attributen_attractie, opslaan_callback=Toevoegen_voorziening)

scherm.voeg_nieuwe_voorziening_knop_toe("Toevoegen winkel en of horeca", 1030, 400, attributen_horeca, opslaan_callback=Toevoegen_voorziening)



scherm.open()
    