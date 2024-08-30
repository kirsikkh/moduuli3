'''
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon
(g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
    Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
    Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
'''

sukupuoli = input("Anna biologinen sukupuoli: ")
hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))
if sukupuoli == "nainen" and 117 <= hemoglobiini <= 175:
    print("Hemoglobiiniarvo on normaali.")
if sukupuoli == "nainen" and hemoglobiini < 117:
    print("Hemoglobiiniarvo on alhainen.")
if sukupuoli == "nainen" and hemoglobiini > 175:
    print("Hemoglobiiniarvo on korkea.")
if sukupuoli == "mies" and 134 <= hemoglobiini <= 195:
    print("Hemoglobiiniarvo on normaali.")
if sukupuoli == "mies" and hemoglobiini < 134:
    print("Hemoglobiiniarvo on alhainen.")
if sukupuoli == "mies" and hemoglobiini > 195:
    print("Hemoglobiiniarvo on korkea.")
