# Erzeugt ein neues quadratisches Spielfeld und liefert es zurück
def new_spielfeld(h):
  return [[" "] * h for i in range(h)]

# Gibt ein quadratisches Schachbrett auf der Konsole aus
def print_spielfeld(feld):
  hoehe = len(feld)
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for i in range(hoehe, 0, -1): # Starte bei hoehe, höre vor 0 (also bei 1) auf, Schrittweite -1 (d.h. abwärts zählen)
    zeile = feld[i-1]
    print("  +" + "---+" * hoehe)
    print(i, end=" | ")
    for zelle in zeile:
      print(str(zelle), end=" | ")
    print()
  print("  +" + "---+" * hoehe)
  print("    ", end="")
  for i in range(hoehe):
    print("{}   ".format(alphabet[i]), end="")
  print()

# Liefert die i-te Zeile des Feldes als Liste:
def zeile(feld,i):
  return feld[i]

# Liefert die i-te Spalte des Feldes als Liste:
def spalte(feld,i):
  return [feld[k][i] for k in range(len(feld))]

# Erläuterung:
# - Spalte i wird festgelegt, es muss dann aus jeder Zeile
#   das i-te Element genommen werden.
# - D.h. feld[k][i] für alle k-Werte von 0 bis zur Länge
# - vgl. Whiteboard-Notizen

# Liefert die Diagonale von links unten nach rechts oben als Liste, auf der i und j liegen:
def diagonale1(feld,i,j):
  # i und j so weit wie möglich nach links unten verschieben:
  abstand = min(i,j) # Abstand nach links unten.
  i -= abstand
  j -= abstand

  # Feld von links unten nach rechts oben entlangwandern:
  laenge = len(feld)
  return [feld[i+k][j+k] for k in range(laenge) if i+k < laenge and j+k < laenge]

# Liefert die Diagonale von rechts unten nach links oben als Liste, auf der i und j liegen:
def diagonale2(feld,i,j):
  # i und j so weit wie möglich nach rechts unten verschieben:
  laenge = len(feld)
  abstand = min(i,laenge-j-1) # Abstand nach rechts unten.
  i -= abstand
  j += abstand

  # Feld von rechts unten nach links oben entlangwandern:
  return [feld[i+k][j-k] for k in range(laenge) if i+k < laenge and j-k >= 0]