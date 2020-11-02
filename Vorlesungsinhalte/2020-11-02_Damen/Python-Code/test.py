import spielfeld

def testfeld():
  feld = spielfeld.new_spielfeld(4)
  feld[1][2] = "X"
  feld[2][1] = "Y"
  feld[1][0] = "Z"
  feld[2][3] = "U"
  return feld

def test_zeile():
  feld = testfeld()
  assert(spielfeld.zeile(feld,0) == [' ', ' ', ' ', ' '])
  assert(spielfeld.zeile(feld,1) == ['Z', ' ', 'X', ' '])
  assert(spielfeld.zeile(feld,2) == [' ', 'Y', ' ', 'U'])
  assert(spielfeld.zeile(feld,3) == [' ', ' ', ' ', ' '])

def test_spalte():
  feld = testfeld()
  assert(spielfeld.spalte(feld,0) == [' ', 'Z', ' ', ' '])
  assert(spielfeld.spalte(feld,1) == [' ', ' ', 'Y', ' '])
  assert(spielfeld.spalte(feld,2) == [' ', 'X', ' ', ' '])
  assert(spielfeld.spalte(feld,3) == [' ', ' ', 'U', ' '])

def test_diagonale1():
  feld = testfeld()
  assert(spielfeld.diagonale1(feld,1,0) == ['Z', 'Y', ' '])
  assert(spielfeld.diagonale1(feld,2,1) == ['Z', 'Y', ' '])
  assert(spielfeld.diagonale1(feld,3,2) == ['Z', 'Y', ' '])
  assert(spielfeld.diagonale1(feld,1,2) == [' ', 'X', 'U'])

def test_diagonale2():
  feld = testfeld()
  assert(spielfeld.diagonale2(feld,1,0) == [' ', 'Z'])
  assert(spielfeld.diagonale2(feld,2,1) == [' ', 'X', 'Y', ' '])
  assert(spielfeld.diagonale2(feld,3,3) == [' '])
  