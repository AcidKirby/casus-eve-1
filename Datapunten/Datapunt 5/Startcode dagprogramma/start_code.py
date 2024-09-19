from pathlib import Path
import json

bestand_pad = Path(__file__).parent / 'persoonlijk_programma_bezoeker_1.json' # i.v.m. working directory problemen
json_bestand = open(bestand_pad) # open en leest het bestand
 
json_dict = json.load(json_bestand) # zet het om naar een Python-dictionary
 
print(json_dict["naam"]) # nu kunnen we het gebruiken als een dict!

json_bestand.close() # sluit het bestand indien niet meer nodig