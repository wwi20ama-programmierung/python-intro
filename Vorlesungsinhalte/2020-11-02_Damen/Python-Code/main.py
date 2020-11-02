import test
import spielfeld
import damen

# Tests ausführen!
test.test_zeile()
test.test_spalte()
test.test_diagonale1()
test.test_diagonale2()


feld = spielfeld.new_spielfeld(4)

spielfeld.print_spielfeld(feld)

damen.damen(feld,0)

spielfeld.print_spielfeld(feld)

# Konzepte - Wiederholung
# - List Comprehensions
# - Schleifen
# - Rekursive Lösung für Damenproblem
# - Tests
