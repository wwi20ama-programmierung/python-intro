# Schreiben Sie eine Funktion, die einen String s als
# Parameter erwartet und die prüft, ob s eine Ziffer ist. 
def ist_ziffer(s):
  ziffern = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  return s in ziffern
#  if s in ziffern:
#    return True
#  return False

# Schreiben Sie eine Funktion ist_zahl(), die einen String s erwartet und True zurückgibt, wenn s nur Ziffern enthält.
def ist_zahl(s):

  # Sonderfall: s ist leer
  if s == "":
    return False

  # Für jeden Buchstaben in s (der Name sei b):
  for b in s:
    if ist_ziffer(b) == False:
      return False
  return True

  
    # und jedes Zeichen
    # darin prüft, ob es eine Ziffer ist.
  
def summe():
  ergebnis = 0
  eingabe = input()

  # Solange der Benutzer keine 0 eingegeben hat:
  # Solange Eingabe != 0
  while ist_zahl(eingabe):
    ergebnis += int(eingabe)
    eingabe = input()
  
  return ergebnis
