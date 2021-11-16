#Ermitteln Sie für einen festgelegten Zahlenbereich 
# Primzahlen und schreiben Sie diese in eine Liste. Geben Sie die Liste anschließend aus.

import math

for i in range(1,120):
    if (i / i == 1) and (i / 2 != 0):
        print(i)