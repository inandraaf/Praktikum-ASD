def ucapkanSalam():
    print("Assalamu 'alaikum!")

def sapa(nama):
    ucapkanSalam() # Ini memanggil fungsi ucapkanSalam() di atas.
    print('Halo',nama)
    print('Selamat belajar!')

def kuadratkan(b):
    h = b*b
    return h

ucapkanSalam()
sapa('Mas Wowok')
b = kuadratkan(5)
print(b)
k = 9
print('Bilangannya',k, ', kalau dipangkatkat dua jadinya', kuadratkan(k))