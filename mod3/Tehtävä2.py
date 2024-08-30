'''
Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
Tehtävässä on käytettävä if/elif/else-toistorakennetta.
    LUX on parvekkeellinen hytti yläkannella.
    A on ikkunallinen hytti autokannen yläpuolella.
    B on ikkunaton hytti autokannen yläpuolella.
    C on ikkunaton hytti autokannen alapuolella.
Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa 'Virheellinen hyttiluokka'
'''

laiva = input("Anna laivan hyttiluokka: ")
if laiva == "LUX":
    print(f"LUX on parvekkeellinen hytti yläkannella.")
elif laiva == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif laiva == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif laiva == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")
