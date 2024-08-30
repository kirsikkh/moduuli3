"""
Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
Kuha on alamittainen, jos sen pituus on alle 37 cm.
"""

pituus = float(input("Kalastaja, anna kuhan pituus senttimetreinä: "))
if pituus<37:
    ali = 37 - pituus
    print(f"Laske kuha takaisin järveen, se on {ali} centtimetriä liian lyhyt.")

