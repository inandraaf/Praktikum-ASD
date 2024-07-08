class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai',len(self.teks),'karakter.')
    def perbarui(self,stringBaru):
        self.teks = stringBaru
    def apakahTerkandung(self, kata):   #NO.1A
        self.kata = kata
        if self.kata in self.teks:
            return True
        else:
            return False

    def hitungKonsonan(self):   #NO.1B
        a = self.teks
        vok = " AIUEOaiueo"	
        jml = 0	
        for b in a:
            if b.lower() not in vok :
                jml+=1
        return jml
    
    def hitungVokal(self):  #NO.1C
        a = self.teks
        vok = " AIUEOaiueo"	
        jml = 0	
        for b in a:
            if b.lower() in vok :
                jml+=1
        return jml
    
print('\n Oleh L200220045 ')
print(' Inandra Asha Fardhana ')
