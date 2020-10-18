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
	### Anmerkung: Kürzer geht das mit "List Comprehensions" bzw. mit Listenoperationen.

# Mischt den angegebenen Kartenstapel.
def mischen(stapel):
	random.shuffle(stapel)

# Verschiebt die erste Karte vom Quellstapel
# ans Ende des Zielstapels.
def ziehen(quellstapel, zielstapel):
	k = quellstapel[0]
	zielstapel += [k]
	quellstapel.remove(k)

# Gibt 6 Karten vom Quellstapel an den Zielstapel.
def geben(quellstapel, zielstapel):
	for i in range(6):
		ziehen(quellstapel, zielstapel)


# Soll True zurückgeben, wenn die Karte k1
# auf die Karte k2 gelegt werden darf,
# sonst soll False zurückgegeben werden.
def pruefe(k1, k2):
	return k1[0] == k2[0] or k1[1] == k2[1]


# Soll dem Spieler seine Karten zeigen,
# ihn fragen, welche Karte er spielen möchte
# und diesen Zug dann ausführen.
#
# Bei Falscheingabe soll noch einmal gefragt werden.
# Der Spieler sollte die Möglichkeit zum Ziehen haben.
def spielzug(name_spieler, hand_spieler, ablagestapel, kartenstapel):
	# Karten zeigen:
	print(name_spieler + ", Du bist am Zug.")
	print("Deine Karten sind:")
	print(hand_spieler)

	# Nach Zug fragen:
	nummer_karte = int(
	    input("Welche Karte möchtest Du Spielen? (Nummer eingeben)"))

	# Zug ausführen
	karte = hand_spieler[nummer_karte]
	if pruefe(karte, ablagestapel[-1]):
		ablagestapel += [karte]
		hand_spieler.remove(karte)
	else:
		spielzug(name_spieler, hand_spieler, ablagestapel, kartenstapel)

# Führt das Spiel aus.
# Definiert Datenstrukturen für die verschiedenen
# Kartenstapel, Spieler etc.

def start_maumau():
	# Datenstrukturen für das Spiel:

	## Spieler:
	spieler1 = "Rotkäppchen"
	spieler2 = "Böser Wolf"
	### Anmerkung: Später durch eine Liste von
	###            Strings ersetzen

	## Kartenstapel:
	kartenstapel = neue_karten()

	## Ablagestapel
	ablagestapel = []

	## Hände der Spieler
	hand_spieler1 = []
	hand_spieler2 = []

	# Ablauf des Spiels:

	## Startspieler festlegen
	aktueller_spieler = spieler1

	## Karten mischen:
	mischen(kartenstapel)

	## Karten austeilen:
	geben(kartenstapel, hand_spieler1)
	geben(kartenstapel, hand_spieler2)

	## Startkarte ziehen:
	ziehen(kartenstapel, ablagestapel)

	# Bis einer der Spieler keine Karten mehr hat:
	while len(hand_spieler1) != 0 and len(hand_spieler2) != 0:
		### Anmerkung: Später verallgemeinern.

		# Aktueller Spieler macht einen Zug:
		# (legt eine Karte oder zieht eine)
		spielzug(aktueller_spieler, ..., ablagestapel, kartenstapel)

		# TODO:
		# 1. Hand im Aufruf der Funktion spielzug() bestimmen
		#    - hand_spieler1 oder hand_spieler2
		# 2. Spieler wechseln (innerhalb der Schleife)
		# 3. Gewinner ermitteln und ausgeben (nach der Schleife)
