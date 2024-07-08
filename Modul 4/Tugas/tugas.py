class Mahasiswa(object):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

c0 = Mahasiswa('cinta',120,'Sragen', 500000)
c1 = Mahasiswa('devanda',90,'Sragen', 500000)
c2 = Mahasiswa('izam',144,'Wonogiri', 200000)
c3 = Mahasiswa('zaki',145,'Ngawi', 250000)
c4 = Mahasiswa('al fitran',156,'Klaten', 240000)
c5 = Mahasiswa('victor',155,'Sragen', 350000)
c6 = Mahasiswa('iqbal',133,'Bekasi', 445000)
c7 = Mahasiswa('galih',153,'Sukoharjo', 545000)
c8 = Mahasiswa('firman',128,'Bogor', 745000)
c9 = Mahasiswa('Yakuza',122,'Wonogiri', 570000)
c10 = Mahasiswa('Bagas',132,'Solo', 865000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

target = 'Sragen'
def cari(target, Daftar):
    o = []
    d = 0
    for i in range (len(Daftar)):
        if Daftar[i].kotaTinggal == target:
            o.append(d)
            d += 1
        else:
            d += 1
    return o

def cariUangSakuTerkecil(kumpulan):
    terkecil = kumpulan[0].uangSaku
    for i in kumpulan:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku
    return terkecil

def cariyangTerkecil(kumpulan):
    n = []
    terkecil = kumpulan[0].uangSaku
    for i in kumpulan:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku
            n.append(kumpulan.index(i))
    return n

def cariKurangDari(kumpulan):
    b = []
    for i in kumpulan:
        if i.uangSaku < 250000:
            terkecil = i.uangSaku
            b.append(kumpulan.index(i))
    return b

class node (object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def cari (self, cari):
        curNode = self
        while curNode is not None :
            if curNode.next != None :
                if curNode.data != cari :
                    curNode = curNode.next
                else :
                    print ("Item", cari, "ada dalam Linked List")
                    break
            elif curNode.next == None :
                    print ("Item", cari, "tidak ada Linked List")
                    break
a = node (12)
a.next = node (34)
a = a.next
a.next = node (10)
a = a.next
a.next = node (45)

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

a = [2,3,5,6,8,9,10,11,12,13,14]
index_a = 12
index_b = 17

def binSearch(kumpulan, target):
    low = 0
    high = len(kumpulan) -1
    data = []

    while low != high:
        mid = (high + low) //2
        if kumpulan[mid] == target:
            break
        elif target < kumpulan[mid]:
            high = mid -1
        else :
            low = mid +1
    for i in range (low, high):
        if target == kumpulan[i]:
            data.append(i)
    return data

print("\n---Oleh L200220045---")
