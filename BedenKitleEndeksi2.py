print("""
*********************************************

Beden Kitle Endeksi Hesaplama

*********************************************
""")

boy = float(input("Boyunuzu giriniz: "))
kilo = float(input("Kilonuzu giriniz: "))
bki = kilo / (boy ** 2)
print("Beden kitle endeksiniz: ", bki)

if bki < 18.25:
    print("Zayıf")
elif 18.5 < bki < 25:
    print("Normal")
elif 25 < bki < 30:
    print("Fazla Kilolu")
elif bki > 30:
    print("Obez")
else:
    print("Geçersiz boy ve kilo değerleri!")