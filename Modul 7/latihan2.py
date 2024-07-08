import re

def cari_kata(pola, teks):
    cocok = re.findall(pola, teks)
    return cocok if cocok else []

hasil = cari_kata(r'eee', 'teeeh')
hasil1 = cari_kata(r'ehs', 'teeeh')
hasil2 = cari_kata(r'..h', 'teeeh')
hasil3 = cari_kata(r'\d\d\d', 't123h di 2019 bulan 02')
hasil4 = cari_kata(r'\w\w\w', '@@a*bc#def*tghh!!')
print(hasil)
print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)