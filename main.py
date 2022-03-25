print("""
***********************************
Dört İşlem Hesap Makinesi

İşlemler:

Toplama İşlemi: 1

Çıkarma İşlemi: 2

Çarpma İşlemi: 3

Bölme İşlemi: 4


***********************************
""")
islem = input("Yapmak istediğiniz işlemi giriniz: ") #girdiyi string olarak istedik
birincisayi = float(input("İşlem yapmak istediğiniz ilk sayı giriniz: "))
ikincisayi = float(input("İşlem yapmak istediğiniz ikinci sayı giriniz: "))


if islem == "1": #girdiyi string olarak istediğimiz için burada da string olarak tanımladık
    print("Toplama işleminin sonucu: ", birincisayi + ikincisayi)
elif islem == "2": #girdiyi string olarak istediğimiz için burada da string olarak tanımladık
    print("Çıkarma işleminin sonucu: ", birincisayi - ikincisayi)
elif islem == "3": #girdiyi string olarak istediğimiz için burada da string olarak tanımladık
    print("Çarpma işeminin sonucu: ", birincisayi * ikincisayi)
elif islem == "4": #girdiyi string olarak istediğimiz için burada da string olarak tanımladık
    print("Bölme işeminin sonucu: ", birincisayi / ikincisayi)
    print("İşlemin kalanı: ", birincisayi % ikincisayi)
else:
    print("İşlem seçmediniz!")
