#Erik Brinker
#ETS2021
#17.11.2021


#Ermitteln Sie für einen festgelegten Zahlenbereich 
# Primzahlen und schreiben Sie diese in eine Liste. Geben Sie die Liste anschließend aus.




prim = []                               #Liste für die Primzahlen erstellt

for num in range(2,101):                #Bereich der Zahlen angeben aus denen die Primzahlen ermittelt werden sollen
    prime = True                        #Für alle Nummern in dem Bereich ist die Variable prime --->immer<--- als true markiert(kann nur durch false geändert werden)
    for i in range(2,num):              #Neuer Bereich der Zahlen, die unter der Zahl liegen, die ich als Primzahl ermitteln will
        if (num%i==0):                  #Ist meine Primzahl durch eine Zahl in dem oberen Bereich (i) teilbar,
            prime = False               #ist es keien Primzahl, prime wird dadurch auf false gesetzt

    if prime:                           #für alle Zahlen, bei denen prime true ist, 
       prim.append(num)                 #werden diese hier in die Liste der PRimzahlen gepackt

for pr in prim:                         #Liste ausgeben
    print(pr)