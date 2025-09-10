class Automat:
  def __init__(self):
    self.preis_stand = 0
    self.preis_ticket = 0
    self.anzahl_stand = 0
    self.rabatt = 0
    self.rabatt_anzahl = 0
    self.admincode = "6666"
  def admin_check(self, eingabe):
    return eingabe == self.admincode
  def admin_modus(self):
    while True: 
      funktion = input("a für Admin-Einstellungen, c für Admin-Codewort ändern und n für Programm beenden(a/c/n) ").strip().lower()
      if funktion == "a":
        print ("Admin-Einstellungen werden aufgerufen. ")
        self.automat_einrichten()
      elif funktion == "c":
        print("Neues Codewort wird erstellt!")
        while True:
          
          pw1 = input("Neues Passwort eingeben.")     
          pw2 = input ("Passwort bestätigen.")         
          if pw1 == pw2:
            self.admincode = pw1
            print(f"Neues Admin Passwort ist {self.admincode}")
            return self.admincode
            
          else:
            print ("Passwörter stimmen nicht überein")
            continue
      elif funktion == "n":
        print ("Adminmodus wurde beendet")
        return self.admincode
  def eingabe(self,frage:str,typ):
    eingabe = str(input(frage))
    try:
      if self.admin_check(eingabe):
        self.admin_modus()
      elif typ == int:
        return int(eingabe)
      elif typ == float:
        return float(eingabe)
      elif typ == str:
        return str(eingabe)
    except ValueError:
      print(f"Bitte eine gültige {typ.__name__} machen.")
      
  def preis(self):
    self.preis_stand = self.preis_ticket*self.anzahl_stand
    return self.preis_stand
  def anzahl_tickets(self):
    stand = self.eingabe("Wieviele Tickets möchtest du haben ? ",int)
    self.anzahl_stand += int(stand)
  def rabatt_berechnen(self):
    if self.anzahl_stand >= self.rabatt_anzahl:
      print(f"Sie bekommen ein Rabbat von {self.rabatt}% auf Ihre Tickets")
      self.preis_stand = self.preis_stand - (self.preis_stand*self.rabatt/100)
      print(f"Deine Tickets kosten aktuell {self.preis_stand} Euro.")
  def beenden (self):
    while True:
      stop = self.eingabe(f"Möchtest du noch weitere Tickets kaufen? Du hast aktuell {self.anzahl_stand} Tickets die kosten {self.preis_stand} (j/n)",str).strip().lower()
      if stop == "n":
        print(f"Bitte bezahlen Sie den Betrag von {self.preis_stand} Euro.")
        return False
        break
      elif stop == "j":
        break

      else:
        print("Bitte gibt j für ja und n für nein ein! ")
        continue
  def automat_einrichten(self):
    while True:
      
      self.rabatt = self.eingabe("Wieviel Prozent soll vom Ticketpreis runter gehen? ",float)
      try:
        if self.rabatt>100:
          print("Du bist über 100% das ist nicht möglich.")
          continue
        
      except TypeError:
        continue
      self.rabatt_anzahl = self.eingabe("Ab wieviele Tickets soll der Rabatt eingeführt werden? ",int)
      self.preis_ticket = self.eingabe("Wieviel sollen die Tickets kosten? ",float)
      print(f"Die Einstellungen wurden geändert: Rabatt = {self.rabatt}, Wieviele Tickets Rabatt = {self.rabatt_anzahl}, Ticketpreis = {self.preis_ticket}")
      break
  def hauptprogramm(self):
    self.automat_einrichten()
    while True:
      self.anzahl_tickets()
      self.preis()
      self.rabatt_berechnen()
      beenden = self.beenden()
      if beenden == False:
        break
automat = Automat()
automat.hauptprogramm()
