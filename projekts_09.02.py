from math import *
ned=float(input("Cik stundas šonedēļ ir tavs mērķis sportot? - "))
diena=["pirmdien","otrdien","trešdien","ceturtdien","piektdien","sestdien","svētdien"]
kopa=0
for i in diena:
    laiks=float(input("Cik stundas sportoji "+i+"? - "))    
    kopa+=laiks
kopa=round(kopa,2)
ned=round(ned,2)
if ned==kopa:
    print("Šonedēļas mērķis ir izpildīts!")
elif ned>kopa:
    print("Šonedēļas mērķis nav izpildīts, pietrūkst ",ned-kopa,"stundas")
elif kopa>ned:
    print("Šonedēļas mērķis ir izpildīts! Nosportots ",kopa-ned,"stundas vairāk nekā plānots")
