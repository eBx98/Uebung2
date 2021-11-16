#Sie bauen ein Haus und wollen wissen wieviel Geld Sie bei einer bestimmten Summe
#und einem bestimmten Zinssatz monatlich zahlen müssen, wenn Sie in 10 Jahren schuldenfrei sein wollen.
import math

Kosten = 123000
Zins = 6
Jahre = 10
Monate = 12

KostenZ = Kosten / 100 * Zins
KostenR = Kosten + KostenZ
Zahlung = KostenR / Monate / Jahre

print(Zahlung)



