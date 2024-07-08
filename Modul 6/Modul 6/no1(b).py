class MhsTIF(object):
    def __init__(self,nama,umur,kota,saku,nim):
        self.nama = nama
        self.umur = umur
        self.kota = kota
        self.saku = saku
        self.nim = nim
    
c0 = MhsTIF('Ika',10,'Sukoharjo', 240000, 101)
c1 = MhsTIF('Budi',19,'Sragen', 230000, 102)
c2 = MhsTIF('Ahmad',12,'Surakarta', 250000, 103)
c3 = MhsTIF('Chandra',17,'Surakarta', 235000, 104)
c4 = MhsTIF('Eka',13,'Boyolali', 240000, 105)
c5 = MhsTIF('Fandi',11,'Salatiga', 250000, 106)
c6 = MhsTIF('Deni',16,'Klaten', 245000, 107)
c7 = MhsTIF('Galuh',18,'Wonogiri', 245000, 108)
c8 = MhsTIF('Janto',20,'Klaten', 245000, 109)
c9 = MhsTIF('Hasan',14,'Karanganyar', 270000, 110)
c10 = MhsTIF('Khalid',15,'Purwodadi', 265000, 111)


Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)
    
def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, titikBelah + 1, akhir)
        quickSortBantu(A, awal, titikBelah - 1)

def partisi(A, awal, akhir):
    nilaiPivot = A[awal]
    
    penandaKiri = awal + 1
    penandaKanan = akhir
    
    selesai = False
    while not selesai:
        
        while penandaKiri <= penandaKanan and A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1
            
        while penandaKanan >= penandaKiri and A[penandaKanan] >= nilaiPivot:
            penandaKanan = penandaKanan - 1
            
        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp
            
    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp
    
    return penandaKanan

def con(a, b):
    new = []
    for x in range(len(a)):
        for y in range(len(a)):
            if a[x] == b[y].nama:
                new.append(b[y])
    return new

ls = []
for x in Daftar:
    ls.append(x.nama)

print('Pengurutan berdasarkan nama sebagai berikut : ')
quickSort(ls)
for x in con(ls, Daftar):
    print("~~", x.nama, x.umur, x.kota, x.saku, x.nim)