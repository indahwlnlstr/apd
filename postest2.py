#operasi aritmatika
print("Hello,""Selamat Datang")

def print_menu():
    print(30 * "-", "MENU", 30*"-")
    print("1. Menghitung Luas Balok")
    print("2. Menghitung Konversi Suhu")
    print("3. Menghitung Volume Kerucut")

print_menu()
pilihan = int(input("Masukkan Pilihan: "))
if pilihan == 1:
    p = int(input("masukkan panjang = "))
    l = int(input('masukkan luas = '))
    t = int(input('masukkan tinggi = '))

    luas = (2*p*l)+(2*p*t)+(2*l*t)

    print("luas balok adalah = ", luas)

elif pilihan == 2:
    Celcius = float(input("masukkan suhu = "))
    Reamur = 4/5*Celcius
    Farenheit = 9/5*Celcius+32
    Kelvin = 273+Celcius

    print("Celcius = ", Celcius)
    print("Reamur = ", Reamur)
    print("Farenheit = ", Farenheit)
    print("Kelvin = ", Kelvin)

elif pilihan == 3:
    r = int(input("Masukkan jari-jari = "))
    t = int(input("Masukkan Tinggi = "))

    phi = 3.14
    volume = 1/3*(phi*r*r*t)

    print("Volume Kerucut adalah = ", volume)

print(30* "-", "TERIMAKASIH", 30* "-")

