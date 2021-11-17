#Erik Brinker
#ETS2021
#17.11.2021


#Sie bauen ein Haus und wollen wissen wieviel Geld Sie bei einer bestimmten Summe
#und einem bestimmten Zinssatz monatlich zahlen müssen, wenn Sie in 10 Jahren schuldenfrei sein wollen.
import math


#Variable
Schulden = 100000                               #Liste Schulden erstellt mit Schulden
Zins = 5                                        #JahresZins
Jahre = 10                                      #Jahre

#Rechnung
Monate = Jahre * 12                             #Monate ausrechnen
Tilgung = Schulden/Monate                       #Tilgung ohne zinsen
mtlZins = Zins/12/100+1                         #monatliche Zinssatz berechnet
zaehler = 0                                     #leere Variable 
while Schulden >= 1:                            #Schleife bis Variable kleiner als 1 ist
    Schulden = Schulden * mtlZins - Tilgung     #Rechnung in Schleife
    zaehler += 1                                #Variable zählt den Vorgang in der Schleife

print ('Die mtl. Tilgung beträgt','{0:.2f}'.format(Tilgung*zaehler/Monate),'€')

