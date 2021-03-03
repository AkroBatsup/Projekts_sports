from math import *
ned=float(input("Cik stundas sonedel ir tavs merkis sportot? - "))
diena=["pirmdien","otrdien","tresdien","ceturtdien","piektdien","sestdien","svetdien"]
kopa=0
for i in diena:
    laiks=float(input("Cik stundas sportoji "+i+"? - "))    
    kopa+=laiks
kopa=round(kopa,2)
ned=round(ned,2)
if ned==kopa:
    print("Sonedelas merkis ir izpildits!")
elif ned>kopa:
    print("Sonedelas merkis nav izpildits, pietrukst ",ned-kopa,"stundas")
elif kopa>ned:
    print("Sonedelas merkis ir izpildits! Nosportots ",kopa-ned,"stundas vairak neka planots")