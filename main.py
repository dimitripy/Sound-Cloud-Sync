
import scdl
import subprocess
import os

eingabe = input("Link verwenden: ")
# Prüfen, ob "https://" im eingegebenen Text vorhanden ist
if "https://" in eingabe:
    # Aufteilen des Strings am "https://" und Auswahl des letzten Teils
    soundcloud_link = "https://" + eingabe.split("https://")[-1]
else:
    # Verwenden der Standardeingabe, falls kein "https://" gefunden wurde
    #soundcloud_link = "https://soundcloud.com/ageq/likes"
    soundcloud_link = "https://soundcloud.com/ageq/sets/party"

#Zielpfad: 
#ziel_pfad = "storage/music"
ziel_pfad = os.path.join(os.getcwd(), "music")


os.makedirs(ziel_pfad, exist_ok=True) 
# Befehl als Liste von Argumenten
command = ["scdl", "-l", soundcloud_link, "-c","-f", "--path", ziel_pfad]

subprocess.run(command)
