import re
s = open('KEI.html','r', encoding='latin1')

teks = s.read()

string = re.findall(r'title="([\w+]+)">', teks)
string = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>', teks)
a = []
for i in string:
    a.append((i[0], float(i[1])))

print(a)

