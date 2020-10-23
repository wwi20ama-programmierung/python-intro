import maumau


def test_mischen():
    ausgangsstapel = [("Pik", "Dame"), ("Kreuz", "König")]
    teststapel = ausgangsstapel.copy()

    maumau.mischen(teststapel)

    # Differenzstapel berechnen:
    # Enthält alle Karten, die nur in einem von ausgangsstapel und teststapel enthalten sind.
    differenzstapel = [k for k in teststapel if k not in ausgangsstapel]
    differenzstapel += [k for k in ausgangsstapel if k not in teststapel]

    # Wenn der Differenzstapel nicht leer ist, dann
    # ist beim Mischen ein Fehler passiert.
    if len(differenzstapel) != 0:
        print("Fehler beim Mischen")


def test_ziehen():
    quellstapel = [("Kreuz", "König"), ("Karo", "Neun")]
    zielstapel = []
    maumau.ziehen(quellstapel, zielstapel)

    if quellstapel != [("Karo", "Neun")]:
        print("Fehler, Quellstapel falsch.")
    if zielstapel != [("Kreuz", "König")]:
        print("Fehler, Zielstapel falsch.")

    quellstapel = []
    zielstapel = []
    maumau.ziehen(quellstapel, zielstapel)

    if quellstapel != [] or zielstapel != []:
        print(
            "Fehler: Wenn am Anfang beide Stapel leer sind, müssen sie es auch nach dem Ziehen sein."
        )


def test_geben():
    kartenstapel = ["k1", "k2", "k3", "k4", "k5", "k6", "k7"]
    handkarten = []
    speicherstapel = kartenstapel.copy()
    maumau.geben(kartenstapel, handkarten)

    # Prüfen, ob nach dem Geben die Liste der Handkarten
    # genau die ersten 6 Karten vom Kartenstapel enthält
    # und ob diese 6 Karten vom Stapel entfernt wurden.
    if handkarten != speicherstapel[0:6]:
        print("Fehler: Handkarten nach dem Geben stimmen nicht.")
    if speicherstapel[6:] != kartenstapel:
        print("Fehler: Kartenstapel nach dem Geben stimmt nicht.")

    kartenstapel = ["k1", "k2", "k3", "k4", "k5"]
    handkarten = []
    maumau.geben(kartenstapel, handkarten)
    if kartenstapel != ["k1", "k2", "k3", "k4", "k5"] or handkarten != []:
        print(
            "Fehler: Bei zu wenigen Karten im Kartenstapel dürfte eigentlich nichts passieren."
        )


def test_pruefe():
    if not maumau.pruefe(("Kreuz", "König"), ("Kreuz", "Zehn")):
        print("Kreuz König und Kreuz Zehn sollten eigentlich zusammenpassen.")


def test_neu_mischen():
    ablagestapel = ["k1", "k2", "k3"]
    kartenstapel = []
    maumau.neu_mischen(kartenstapel, ablagestapel)

    if ablagestapel != []:
        print("Fehler: Ablagestapel sollte nach neuem Mischen leer sein.")
    if len(kartenstapel) != 3:
        print(
            "Fehler: Der Kartenstapel sollte nach dem Mischen 3 Elemente haben."
        )

    # To Do:
    # 2. Test dafür schreiben
    #    - Zwei Kartenstapel ("kartenstapel", "ablagestapel") erzeugen.
#     - Wenn "kartenstapel" nicht leer ist, soll nichts passieren


#      - Sonst sollen die Karten vom Ablagestapel auf dem Kartenstapel liegen.
#      - Gibt es weitere/andere Anforderungen?
