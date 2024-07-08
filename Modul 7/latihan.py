import re

def cari_kata(pola, teks):
    cocok = re.findall(pola, teks)
    if cocok:
        return cocok
    else:
        return None

s = 'sebuah contoh kata:teh!!'
hasil = cari_kata(r'kata:\w\w\w', s)
if hasil:
    print('Menemukan:', hasil)
else:
    print('Tidak menemukan')