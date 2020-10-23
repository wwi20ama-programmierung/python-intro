import random

def neue_karten():
  return [
      ("Kreuz", "Sieben"),
      ("Kreuz", "Acht"),
      ("Kreuz", "Neun"),
      ("Kreuz", "Zehn"),
      ("Kreuz", "Bube"),
      ("Kreuz", "Dame"),
      ("Kreuz", "König"),
      ("Kreuz", "Ass"),
      ("Pik", "Sieben"),
      ("Pik", "Acht"),
      ("Pik", "Neun"),
      ("Pik", "Zehn"),
      ("Pik", "Bube"),
      ("Pik", "Dame"),
      ("Pik", "König"),
      ("Pik", "Ass"),
      ("Herz", "Sieben"),
      ("Herz", "Acht"),
      ("Herz", "Neun"),
      ("Herz", "Zehn"),
      ("Herz", "Bube"),
      ("Herz", "Dame"),
      ("Herz", "König"),
      ("Herz", "Ass"),
      ("Karo", "Sieben"),
      ("Karo", "Acht"),
      ("Karo", "Neun"),
      ("Karo", "Zehn"),
      ("Karo", "Bube"),
      ("Karo", "Dame"),
      ("Karo", "König"),
      ("Karo", "Ass"),
  ]

def mischen(stapel):
  random.shuffle(stapel)


def ziehen(quellstapel, zielstapel):
  if quellstapel == []:
    return
  k = quellstapel[0]
  zielstapel += [k]
  quellstapel.remove(k)

def geben(quellstapel, zielstapel):
  if len(quellstapel) < 6:
    return
  for i in range(6):
    ziehen(quellstapel, zielstapel)

# Soll True zurückgeben, wenn die Karte k1
# auf die Karte k2 gelegt werden darf,
# sonst soll sie False zurückgeben.
def pruefe(k1, k2):
  return k1[0] == k2[0] or k1[1] == k2[1]

# Soll den Ablagestapel neu mischen und zum Kartenstapel machen.
def neu_mischen(kartenstapel, ablagestapel):
  if len(kartenstapel) == 0:
    kartenstapel += ablagestapel
    mischen(kartenstapel)
    ablagestapel.clear()

# Soll dem Spieler seine Karten zeigen,
# ihn fragen, welche Karte er spielen möchte
# und diesen Zug dann ausführen.
#
# Bei Falscheingabe soll noch einmal gefragt werden.
# Der Spieler sollte die Möglichkeit zum Ziehen haben.
def spielzug(name_spieler, hand_spieler, ablagestapel, kartenstapel):
  # Karten zeigen:
  print()
  print(name_spieler + ", Du bist am Zug.")
  karte = ablagestapel[-1]
  print("Auf dem Ablagestapel liegt ein(e) " + karte[0] + " " + karte[1])
  print("Deine Karten sind:")
  print(hand_spieler)
  # Nach Zug fragen:
  eingabe = input("Welche Karte möchtest Du spielen? (Nummer oder 'z' zum Ziehen) ")
  if eingabe == "z":
    if len(kartenstapel) == 0:
      neu_mischen(kartenstapel, ablagestapel)
    ziehen(kartenstapel, hand_spieler)
  else:
    nummer_karte = int(eingabe) - 1  
    # Zug ausführen
    karte = hand_spieler[nummer_karte]
    if pruefe(karte, ablagestapel[-1]):
      ablagestapel += [karte]
      hand_spieler.remove(karte)
    else:
      spielzug(name_spieler, hand_spieler, ablagestapel, kartenstapel)

def start_maumau():
  # Datenstrukturen für das Spiel:
  ## Spieler:
  spieler1 = "Rotkäppchen"
  spieler2 = "Böser Wolf"
  aktueller_spieler = spieler1
  ### Anmerkung: Später durch eine Liste von
  ###            Strings ersetzen
  ## Kartenstapel:
  kartenstapel = neue_karten()
  ## Ablagestapel
  ablagestapel = []
  ## Hände der Spieler
  hand_spieler1 = []
  hand_spieler2 = []
  aktuelle_hand = hand_spieler1
  mischen(kartenstapel)
  ## Karten austeilen und Startkarte ziehen:
  geben(kartenstapel, hand_spieler1)
  geben(kartenstapel, hand_spieler2)
  ziehen(kartenstapel, ablagestapel)
  # Bis einer der Spieler keine Karten mehr hat:
  while len(hand_spieler1) != 0 and len(hand_spieler2) != 0:
    ### Anmerkung: Später verallgemeinern.
    # Aktueller Spieler macht einen Zug:
    # (legt eine Karte oder zieht eine)
    spielzug(aktueller_spieler, aktuelle_hand,ablagestapel, kartenstapel)
    # 2. Spieler wechseln
    if aktueller_spieler == spieler1:
      aktueller_spieler = spieler2
    else:
      aktueller_spieler = spieler1
    # aktuelle Hand aktualisieren
    if aktueller_spieler == spieler1:
      aktuelle_hand = hand_spieler1
    else:
      aktuelle_hand = hand_spieler2
    # Alternative:
    # aktuelle_hand = hand_spieler1 if aktueller_spieler == spieler1 else hand_spieler2
  
  # 3. Gewinner ermitteln und ausgeben (nach der Schleife)
  if len(hand_spieler1) == 0:
    print(spieler1 + " hat das Spiel gewonnen.")
  else:
    print(spieler2 + " hat das Spiel gewonnen.")

