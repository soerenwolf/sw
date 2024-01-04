# Erstelle ein eigenes Steckbrief als dictionary
steckbrief = {
    "Name": "Sören Wolf",
    "Alter": 46,
    "Stadt": "Tüßling",
    "Hobbies": ["V8/US Car Szene", "Tiere", "Kochen"],
}

# Ergänze deine Hobbies um ein weiteres
steckbrief["Hobbies"].append("mein Dodge RAM")

# Lass dein erstes Hobby ausgeben
print("Erstes Hobby:", steckbrief["Hobbies"][0])

# Ergänze das dictionary um einen Spitznamen
steckbrief["Spitzname"] = "gibt`s keinen"

# Entferne einen Key
del steckbrief["Alter"]

# Prüfe ob Hobbies vorhanden sind
if "Hobbies" in steckbrief:
    print("Hobbies sind vorhanden.")
else:
    print("Keine Hobbies gefunden.")

# Ändere dein zweites Hobby
steckbrief["Hobbies"][1] = "Gartenarbeit"

print(steckbrief)