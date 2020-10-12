from zahlen import ist_ziffer, ist_zahl, summe

print(ist_ziffer(""))  # Soll False ausgeben
print(ist_ziffer("1"))  # Soll True ausgeben
print(ist_ziffer("2"))  # Soll True ausgeben
print(ist_ziffer("7"))  # Soll True ausgeben
print(ist_ziffer("12"))  # Soll False ausgeben
print(ist_ziffer("abc123"))  # Soll False ausgeben

print("Zahlen:")
print(ist_zahl(""))  # Soll False ausgeben
print(ist_zahl("1"))  # Soll True ausgeben
print(ist_zahl("123"))  # Soll True ausgeben
print(ist_zahl("abc123"))  # Soll False ausgeben

print(summe())
