##################################################
# Arbeiten mit der Konsole (input() und print()) #
##################################################

# Das Programm soll aus einer Funktion bestehen, die Ihren Namen an der Konsole abfragt und anschließen ausgibt:

def wie_ist_mein_name():
  name = input("Wie heißt du? ")
  print(name)

# wie_ist_mein_name

# Das Programm soll aus einer Funktion bestehen, die Ihren Namen an der Konsole abfragt und anschließen ausgibt. Ist kein Name angegeben, soll eine Fehlermeldung ausgegeben werden:

def wie_ist_mein_name_oder_leer():
  name = input("Wie heißt du? ")
  if(name == ""):
    print("Das ist aber nicht nett!")
  else:
    print("Hallo " + name + "!")

# wie_ist_mein_name_oder_leer()

# Sie wurden beauftragt, für einen US-Supermarkt ein Programm zu entwickeln, dass das Alter des Kunden abfragt und ausgibt, ob die Person in den USA alkoholische Getränke kaufen darf (Hinweis: Altersgrenze 21 Jahre):

def alterspruefung():
  alter = input("How old are you?")
  if(int(alter) < 21):
    print('Customer is NOT old enough to buy alcoholic beverages!')
  else:
    print('Customer is old enough to buy alcoholic beverages!')

# alterspruefung()

##################################################
#                    Scopes                      #
##################################################

# Schreiben Sie eine Funktion `aufruf`, die eine Funktion `aufgerufen` aufruft und ihr dabei den eigenen Namen übergibt:

def aufgerufen(funktionsname):
  print("Ich wurde von " + funktionsname + " aufgerufen!")

def aufruf():
  print("Diese Funktion ruft die Funktion `aufgerufen` auf.")
  aufgerufen("Aufruf")

# aufruf()

# Der US-Supermarkt ist äußerst zufrieden mit Ihrem Programm und möchte auch die Bezahlung darüber abwickeln. Implementieren Sie dafür die Funktion `bezahlen`, die einen Warenwert und die Mehrwertsteuern (beide als Integer) übergeben bekommt und den Gesamtbetrag berechnet. Anschließend ruft diese eine Funktion `kreditkartenzahlung` auf, die den Gesamtwert an der Konsole ausgibt:

def kreditkartenzahlung():
  print("Credit card purchase completed. Total: $" + str(gesamt))

def bezahlen(warenwert, steuern):
  gesamt = warenwert + steuern
  kreditkartenzahlung()

# bezahlen(100, 16)

# Der US-Supermarkt ist äußerst zufrieden mit Ihrem Programm und möchte auch die Bezahlung darüber abwickeln. Implementieren Sie dafür die Funktion `bezahlen_mit_parameter`, die einen Warenwert und die Mehrwertsteuern (beide als Integer) übergeben bekommt und den Gesamtbetrag berechnet. Anschließend ruft diese eine Funktion `kreditkartenzahlung_mit_parameter` auf, die den Gesamtwert an der Konsole ausgibt:

def kreditkartenzahlung_mit_parameter(gesamt):
  print("Credit card purchase completed. Total: $" + str(gesamt))

def bezahlen_mit_parameter(warenwert, steuern):
  gesamt = warenwert + steuern
  kreditkartenzahlung_mit_parameter(gesamt)

bezahlen_mit_parameter(100, 16)
