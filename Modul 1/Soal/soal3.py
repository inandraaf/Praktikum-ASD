def jumlahHurufVokal(teks):
    teks = teks.lower()
    total_huruf = len(teks)
    huruf_vokal = sum(1 for huruf in teks if huruf in 'aiueo')
    print('\n---Oleh L200220045---')
    return total_huruf, huruf_vokal
    



def jumlahHurufKonsonan(teks):
    teks = teks.lower()
    total_huruf = len(teks)
    huruf_konsonan = sum(1 for huruf in teks if huruf.isalpha() and huruf not in 'aiueo')
    print('\n---Oleh L200220045---')
    return total_huruf, huruf_konsonan
    


