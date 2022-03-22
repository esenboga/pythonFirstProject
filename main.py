while True:
        a = int(input("Bir sayı giriniz: "))
        if a % 2 != 0:
            print("Asal sayıdır.")
        elif a==2:
            print("Asal sayıdır.")
        elif a % a == 0 & a % 1 == 0 :
            print("Asal değildir.")
