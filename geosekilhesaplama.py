print("""
***************************************

Geometrik Şekil Hesaplama

***************************************
""")

a = input("Geometrik şekil seçiniz: ")


if (a == "Dörtgen"):
    print("Kenarları gir: ")
    x = int(input("Birinci kenarın uzunluğu: "))
    y = int(input("İkinci kenarın uzunluğu: "))
    z = int(input("Üçüncü kenarın uzunluğu: "))
    w = int(input("Dördüncü kenarın uzunluğu: "))

    if x==y and x==z and x==w:
        print("Geometrik şeklimiz karedir.")

    elif (x==y and w==z) or (y==w and x==z):
            print("Geometrik şeklimiz dikdörtgendir.")
    else:
        print("Normal dörtgen")


elif (a == "Üçgen"):
    x = int(input("Birinci kenarın uzunluğu: "))
    y = int(input("İkinci kenarın uzunluğu: "))
    z = int(input("Üçüncü kenarın uzunluğu: "))

    if ( abs(x+y) > z and abs(x+z) > y and abs(y+z) > x):

        if ((x==y and x!=z) or (x==z and x!=y)):
             print("İkizkenar üçgen")

        elif (x==y and x==z):
             print("Eşkenar üçgen")

        else:
            print("Normal üçgen")
    else:
        print("Üçgen değil")
else:
    print("Geçersiz şekil")

