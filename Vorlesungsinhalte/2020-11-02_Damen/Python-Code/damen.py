import spielfeld

# Prüft, ob die gegebene Liste nur Leerzeichen enthält:
def leer(liste):
  for element in liste:
    if element != " ":
      return False
  return True

# Prüft, ob eine Dame auf die Position (i,j) im Feld gesetzt werden darf.
def erlaubt(feld,i,j):
  # Wir holen uns die Zeile, Spalte und Diagonalen des Feldes:
  z = spielfeld.zeile(feld,i)
  s = spielfeld.spalte(feld,j)
  d1 = spielfeld.diagonale1(feld,i,j)
  d2 = spielfeld.diagonale2(feld,i,j)

  # Prüfen, ob die Zeilen etc. leer sind:
  return leer(z) and leer(s) and leer(d1) and leer(d2)

# Löst das Damenproblem
# für feld ab der gegebenen Zeile.
# Liefert True zurück, wenn es geschafft ist.
# Liefert False zurück, wenn das Spiel für das gegebene Feld nicht lösbar ist.
def damen(feld, zeilennummer):
  # Sonderfall: zeilennummer == len(feld)
  # In diesem Fall ist das Spiel gelöst.
  if zeilennummer == len(feld):
    return True

  laenge = len(feld)
  # In der gegebenen Zeile eine Dame setzen.
  for spaltennummer in range(laenge):
    if erlaubt(feld,zeilennummer,spaltennummer):
      feld[zeilennummer][spaltennummer] = "D"
      # Das Spiel rekursiv ab der nächsten Zeile lösen.
      ergebnis = damen(feld, zeilennummer+1)
      if ergebnis == True:
        return True
      feld[zeilennummer][spaltennummer] = " "
  return False
