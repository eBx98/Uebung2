#Erik Brinker
#ETS2021
#17.11.2021


#Ermitteln Sie für einen festgelegten Zahlenbereich 
# Primzahlen und schreiben Sie diese in eine Liste. Geben Sie die Liste anschließend aus.




primzahlen = []                               #Liste für die Primzahlen erstellt

for Zahl in range(2,101):                #Bereich der Zahlen angeben aus denen die Primzahlen ermittelt werden sollen
    prim = True                        #Für alle Nummern in dem Bereich ist die Variable prime --->immer<--- als true markiert(kann nur durch false geändert werden)
    for i in range(2,Zahl):              #Neuer Bereich der Zahlen, die unter der Zahl liegen, die ich als Primzahl ermitteln will
        if (Zahl%i==0):                  #Ist meine Primzahl durch eine Zahl in dem oberen Bereich (i) teilbar,
            prim = False               #ist es keien Primzahl, prime wird dadurch auf false gesetzt

    if prim:                           #für alle Zahlen, bei denen prime true ist, 
       primzahlen.append(Zahl)                 #werden diese hier in die Liste der PRimzahlen gepackt

for pr in primzahlen:                         #Liste ausgeben
    print(pr)