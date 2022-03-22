import re
import sys
boy = float(input("Boyunuz: "))
sinirlendirilmisboy = str(boy) #sayıların len'i olmaz str'e dönüştürmek gerekir

if len(sinirlendirilmisboy) > 4:
    print("İnsan ol!")
    sys.exit()

kilo = float(input("Kilonuz: "))
sinirlendirilmiskilo = str(kilo) #sayıların len'i olmaz str'e dönüştürmek gerekir

if len(sinirlendirilmiskilo) > 5:
    print("İnsan ol!")
    sys.exit()

bedenkitleneksi = kilo / (boy ** 2)
string = str(bedenkitleneksi)
print("Beden kitle endeksiniz: ", string[0:5])