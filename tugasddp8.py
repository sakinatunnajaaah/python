def profil(nama, alamat, gender, umur, hoby):
    print("Nama:", nama)
    print("Alamat:", alamat)
    print("Jenis Kelamin:", gender)
    print("Umur:", umur)
    print("Hobi:", hoby)
profil("sakinatun najah", "Jl. Gg Hj musa , Jakarta Selatan", "perempuan", 19, "Membaca, menulis, dan berolahraga")
print()

def cek_kelulusan(nilai):
    if nilai <= 60:
        print('gagal')
    elif 61 <=nilai <=70:
        print('Baik')
    elif 71 <=nilai <=80:
        print('Sangat Baik')
    elif 81 >=nilai <=100:
        print('Istimewa')
cek_kelulusan(90)
print()


def ganjil(n):
    i = 1
    while i <= n:
        if i % 2 != 0:
            print(i)
        i+= 1
ganjil(100)

