a = float(input("İlk sayıyı giriniz: "))
b = float(input("İkinci sayıyı giriniz: "))
c = float(input("Üçüncü sayıyı giriniz: "))

if a>b and a>c:
    print("Seçtiğiniz ilk sayı bu üç sayı arasındaki en büyük sayıdır.")
elif b>a and b>c:
    print("Seçtiğiniz ikinci sayı bu üç sayı arasındaki en büyük sayıdır.")
elif c>a and c>b:
    print("Seçtiğiniz üçüncü sayı bu üç sayı arasındaki en büyük sayıdır.")
else:
    print("Geçersiz bir istekte bulundunuz!")