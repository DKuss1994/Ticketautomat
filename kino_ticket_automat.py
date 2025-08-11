# Ich will ein Kinoticket Automat erstellen. Es werden 3 Kategorien angezeigt Kind, Erwachsen, Senior. Ab insgesammt 10 Tickets soll man eine Rabatt bekommen.

# Werte

kind = 5 # Kinder sind von 0 - 17 Jahre
maxkind = 18 #max alter ist 18
erwachsen = 10 # Erwachsen sind zwischen 18 und 65
maxerwachsen = 65 #max alter 65
senior = 7.5 #Senioren sind ab 65

def alter_pruefung (alter):
  if alter < maxkind:
    preis = kind
    kategorie = "Kind"
  elif alter <= maxerwachsen:
     preis = erwachsen
     kategorie = "Erwachsen"
  else:
    preis = senior
    kategorie = "Senior"
  print(f"Sie sind {alter} alt. Das wäre dann {kategorie}. Da kostet ein Ticket {preis}")
  return preis, kategorie


def weiter_kaufen ():
  ende = input("Möchten Sie weitere Tickets kaufen? (j)")
  if ende != "j":
    
    return False
  return True
  
  
preis_stand = 0
anzahl_stand = 0
rabatt = 0.8 #20% Rabatt
while True:
  try:
    alter = int(input("Wie alt sind Sie? "))
    #Hier wird geprüft in welche Kategorie die Person ist.
    preis, kategorie = alter_pruefung(alter)
    #Hier wird nach der Anzahl wieviel Tickets er in der Kategorie haben will gefragt.
    anzahl = int(input(f"Wieviele Tickets wollen Sie haben in der Kategorie {kategorie}? "))
    # Hier wird im System die Aktuelle Anzahl und der Aktuelle Preis im durchlauf berechnet
    anzahl_stand += anzahl
    gesamt = anzahl*preis
    preis_stand += gesamt
    # Hier soll der Rabatt berchnet werden
    print(f"Ihr gesamt Preis beträgt {preis_stand} Euro")
    
    if anzahl_stand >= 10:
      print(f"Sie bekommen Gruppen Rabatt von 20% auf den Gesamtpreis")
    if not weiter_kaufen():
      break
      
    
    
  
       
      if not weiter_kaufen():
        break
  except ValueError:
    print("Bitte benutzten Sie Zahlen") 
if anzahl_stand >= 10:
  print(f"Sie bekommen Gruppen Rabatt von 20% auf den Gesamtpreis von {preis_stand} Euro. Somit ist ihr aktueller Preis {preis_stand*rabatt} Euro.")
else:
  print(f"Bitte bezahlen Sie den Betrag {preis_stand} Euro")

print("Viel Spaß im Film")
print("Ich hoffe Ihnen hat mein Programm gefallen. Ich bin offen für Verbesserung. Ich hab erst seit dem 22.07.2025 richtig angefangen programmieren zu lernen.")
  
