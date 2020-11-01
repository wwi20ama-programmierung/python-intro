# Bewegt eine einzelne Platte:
def bewege(start, ziel):
  print("Bewege Platte von {} nach {}".format(start,ziel))

# Bewegt einen Turm der Höhe 1 von start über mitte nach ziel.
def turm1(start,mitte,ziel):
  bewege(start,ziel)

# Bewegt einen Turm der Höhe 2 von start über mitte nach ziel.
def turm2(start,mitte,ziel):
  turm1(start,ziel,mitte)
  bewege(start,ziel) # Bewegt die unterste Platte
  turm1(mitte,start,ziel)

# Bewegt einen Turm der Höhe 3 von start über mitte nach ziel.
def turm3(start,mitte,ziel):
  turm2(start,ziel,mitte)
  bewege(start,ziel) # Bewegt die unterste Platte
  turm2(mitte,start,ziel)

# Bewegt einen Turm der Höhe 4 von start über mitte nach ziel.
def turm4(start,mitte,ziel):
  turm3(start,ziel,mitte)
  bewege(start,ziel) # Bewegt die unterste Platte
  turm3(mitte,start,ziel)

# Bewegt einen Turm der Höhe 5 von start über mitte nach ziel.
def turm5(start,mitte,ziel):
  turm4(start,ziel,mitte)
  bewege(start,ziel) # Bewegt die unterste Platte
  turm4(mitte,start,ziel)


# Die eigentliche Hanoi-Lösung:
def hanoi(hoehe, start, mitte, ziel):
  if hoehe > 1:
    hanoi(hoehe-1, start, ziel, mitte)
  bewege(start, ziel)
  if hoehe > 1:
    hanoi(hoehe-1, mitte, start, ziel)

# Anmerkungen:
# Die Funktionen turm1 bis turm5 dienen der Veranschaulichung des Prinzips. Sie werden in der endgültigen Lösung weder benutzt noch gebraucht. Sie sollen v.A. das Funktionsprinzip veranschaulichen:

# Eine Funktion, die einen Turm der Höhe 5 bewegt, muss dafür einen Turm der Höhe 4 bewegen. Wenn man das so in einzelne Funktionen verpackt, wie es hier mit turm1 bis turm5 passiert, dann ist leichter verständlich, warum es funktioniert.

# Die Funktion hanoi macht das gleiche, aber sie ruft sich selbst auf und gibt die Höhe als zusätzlichen Parameter mit. Eine rekursive Funktion beschreibt, wie ein Problem gelöst werden kann, indem man es auf kleinere Probleminstanzen reduziert. Dabei gibt man separat an, wie das Problem für die kleinstmögliche Größe (hier 1) gelöst wird und bei größeren Instanzen verlässt man sich darauf, dass es für kleinere bereits funktioniert.
