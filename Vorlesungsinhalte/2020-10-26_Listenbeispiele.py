# Beispiele zu Listen (Arrays)

# Beispiel 1: Lineare Liste aus Zahlen
liste1 = [1,2,3,4,5,6,7]
for zahl in liste1:
  print(zahl)

# Beispiel 2: Lineare Liste aus Strings
liste2 = ["Hallo","du","schöne","Welt"]
for wort in liste2:
  print(wort)

# Beispiel 3: Gemischte Listen
liste3 = [1,2,3,"Hallo","Liste"]
for element in liste3:
  print(element)

# Beispiel 4: Listen von Listen (Matrix)
liste4 = [[1,2,3],[4,5,6],[7,8,9]]
for zeile in liste4:
  print(zeile)
## Element in Zeile 2 und Stelle 0:
print(liste4[2][0])

# Beispiel 5:
# Liste aus Spielernamen und Handkarten für jeden Spieler
liste5 = [
  [
    "Spieler 1",  # Name von Spieler 1
    "Spieler 2"   # Name von Spieler 2
  ],
  [
    [("Karo","Sieben"), ("Karo","Acht")],  # Liste der Karten von Spieler 1
    [("Herz","Sieben"),("Herz","Acht")]    # Liste der Karten von Spieler 2
  ]
]
print(liste5)
print()

# Schleife, die alle Handkarten von Spieler 1 ausgibt
for karte in liste5[1][0]:
  print(karte)

print()
# Schleife, die alle Spielernamen ausgibt:
for spieler in liste5[0]:
  print(spieler)

print()
# Anzahl der Spieler:
anzahl_spieler = len(liste5[0])

print()
# Schleife, die alle Spieler mit deren Karten ausgibt
# Spieler 1: [("Karo","Sieben"), ("Karo","Acht")]
# Spieler 2: [("Herz","Sieben"), ("Herz","Acht")]

for i in range(anzahl_spieler):
  print(liste5[0][i] + ":", liste5[1][i])

print()
# Beispiel 6: 8x8-Schachbrett
# zweidimensionale Liste
schachbrett = [
  [" "," "," "," "," "," "," "," "],
  [" "," "," "," "," "," "," "," "],
  [" "," "," "," "," "," "," "," "],
  [" "," "," "," "," "," "," "," "],
  [" "," "," "," "," "," "," "," "],
  [" "," "," "," "," "," "," "," "],
  [" "," "," "," "," "," "," "," "],
  [" "," "," "," "," "," "," "," "],
]

# Gibt ein 8x8-Schachbrett auf der Konsole aus
def print_schachbrett(brett):
  laenge = len(brett)
  for i in range(laenge, 0, -1): # Starte bei laenge, höre vor 0 (also bei 1) auf, Schrittweite -1 (d.h. abwärts zählen)
    zeile = brett[i-1]
    print("  +---+---+---+---+---+---+---+---+")
    print(i, end=" | ")
    for feld in zeile:
      print(feld, end=" | ")
    print()
  print("  +---+---+---+---+---+---+---+---+")
  print("    A   B   C   D   E   F   G   H")

print_schachbrett(schachbrett)

print_schachbrett(schachbrett)