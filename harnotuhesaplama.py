print("""
***************************************

Harf Cinsinden Ders Notu Hesaplama

Vize1 toplam notun %30'una etki edecek.

Vize2 toplam notun %30'una etki edecek.

Final toplam notun %40'ına etki edecek.

***************************************
""")

while True:
    try:
        vize1 = float(input("Birinci vize notunuzu giriniz: "))
        if vize1 < 0 or vize1 > 100:
            raise ValueError #this will send it to the print message and back to the input option
        break
    except ValueError:
        print("\nGeçersiz bir not girdiniz. Lütfen notunuzu 0-100 arasında giriniz.\n")

while True:
    try:
        vize2 = float(input("İkinci vize notunuzu giriniz: "))
        if vize2 < 0 or vize2 > 100:
            raise ValueError #this will send it to the print message and back to the input option
        break
    except ValueError:
        print("\nGeçersiz bir not girdiniz. Lütfen notunuzu 0-100 arasında giriniz.\n")

while True:
    try:
        final = float(input("Final notunuzu giriniz: "))
        if final < 0 or final > 100:
            raise ValueError #this will send it to the print message and back to the input option
        break
    except ValueError:
        print("\nGeçersiz bir not girdiniz. Lütfen notunuzu 0-100 arasında giriniz.\n")

birincivize = (vize1 * 30) / 100
ikincivize = (vize2 * 30) / 100
finalnotu = (final * 40) / 100

toplamnot = birincivize + ikincivize + finalnotu

print("\nBirinci vize notunuzun %30'u: {}\nikinci vize notunuzun %30'u: {}\nfinal notunuzun %40'ı: {}\nToplam aldığınız not: {}\n".format(birincivize, ikincivize, finalnotu, toplamnot))

if toplamnot >= 90:
    print("Harf notunuz AA")
elif 90 > toplamnot >= 85:
    print("Harf notunuz BA")
elif 85 > toplamnot >= 80:
    print("Harf notunuz BB")
elif 80 > toplamnot >= 75:
    print("Harf notunuz CB")
elif 75 > toplamnot >= 70:
    print("Harf notunuz CC")
elif 70 > toplamnot >= 65:
    print("Harf notunuz DC")
elif 65 > toplamnot >= 60:
    print("Harf notunuz DD")
elif 60 > toplamnot >= 55:
    print("Harf notunuz FD")
elif toplamnot < 55:
    print("Harf notunuz FF")
else:
    print("Geçersiz talep!")