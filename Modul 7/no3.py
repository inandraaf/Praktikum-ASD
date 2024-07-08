import re
s = open('Indonesia.txt','r', encoding='latin1')

teks = s.read()
s.close()
p = r'di \w+'
hasil = re.findall(p, teks)

print(hasil)

