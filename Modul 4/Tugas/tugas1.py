class Mahasiswa(object):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

c0 = Mahasiswa('Anton',120,'Sragen', 500000)
c1 = Mahasiswa('Devi',90,'Sragen', 500000)
c2 = Mahasiswa('Roni',144,'Wonogiri', 200000)
c3 = Mahasiswa('Yakob',145,'Ngawi', 250000)
c4 = Mahasiswa('Abdi',156,'Klaten', 240000)
c5 = Mahasiswa('Veronica',155,'Sragen', 350000)
c6 = Mahasiswa('Syaiful',133,'Bekasi', 445000)
c7 = Mahasiswa('Damar',153,'Sukoharjo', 545000)
c8 = Mahasiswa('Yanto',128,'Bogor', 745000)
c9 = Mahasiswa('Bambang',122,'Wonogiri', 570000)
c10 = Mahasiswa('Bobby',132,'Klaten', 865000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]


#No 1
def cari(koleksi,target):
    output = []
    index = 0
    for i in koleksi:
        if i.kotaTinggal == target:
            output.append(index)
            index += 1
        else:
            index += 1
    return output

#No 2
def cariTerkecil(koleksi) :
    uangSaku_terkecil = koleksi[0].uangSaku
    for Mahasiswa in koleksi :
        if Mahasiswa.uangSaku < uangSaku_terkecil :
            uangSaku_terkecil = Mahasiswa.uangSaku

    return uangSaku_terkecil

#No 3
def cariuangTerkecil(kumpulan):
    terkecil = kumpulan[0].uangSaku
    hasil = kumpulan[0]
    for mhs in kumpulan:
        if mhs.uangSaku < terkecil:
            terkecil = mhs.uangSaku
            hasil = mhs
    print(hasil.nama, hasil.uangSaku)


#No 4
def cariDaftarUangSakuKurang(kumpulan):
    b = []  
    for i in kumpulan:
        if i.uangSaku < 250000:
            terkecil = i.uangSaku
            b.append(kumpulan.index(i))
    return b

#No 5
class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
a = Node(1,Node(3,Node(5,Node(7,Node(11)))))
def sistem(kumpulan,target):
    data = kumpulan
    x = 1
    while data is not None:
        if data.data == target:
            return ["Data "+str(target)+" terdapat di Node ke"+str(x),True]
        x += 1
        return ['tidak ada',False]

#No 6
A = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) -1
    data = []

    while low <= high:
        mid = (high + low) //2
        if kumpulan[mid] == target:
            data.append(kumpulan.index(target))
            return True
        elif target < kumpulan[mid]:
            high = mid -1
        else :
            low = mid +1
    return False

#No 7
def binSeIndex(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1
    data = []

    while low <= high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            # Menambahkan index saat ini ke dalam data
            data.append(mid)
            # Pencarian ke kiri
            left = mid - 1
            while left >= 0 and kumpulan[left] == target:
                data.append(left)
                left -= 1
            # Pencarian ke kanan
            right = mid + 1
            while right < len(kumpulan) and kumpulan[right] == target:
                data.append(right)
                right += 1
            return data
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

#No 8
from random import randint as r
Answer = r(1,100)
al = list(range(0,100))
i= 1
print(Answer)
front = 0
back = 99
while True:
     x = int(input("Masukkan tebakan dari("+ str(al[front]) + ","+ 
 str(al[back]+1) + ") ke-%i:> " %i))
     mid = (front + back) // 2
     if x == Answer:
         print("BENAR SEKALI")
         break
     elif x < Answer:
         front = x + 1
         print("TO THE RIGHT")
     elif x > Answer:
         back = x - 2
         print("TO THE LEFT")
     i+=1
