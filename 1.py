import modul1 as m
#  лаба сдана
f = open('journal1.txt', 'w')
f.write('\n''---------- 1 страница ----------''\n\n\n')
tit = m.str1()
for i in tit.keys():
    if i == 'str2' or i == 'str3' or i == 'str5':
        f.write('\n\n\n')
    f.write(tit[i]['tit'])
    f.write('\n')
f.write('\n''---------- 2 страница ----------''\n\n\n')
tit2 = m.str2()
for k in tit2.keys():
    f.write(tit2[k]['tit2'])
    f.write('\n')
f.write('\n\n\n''---------- 3 страница ----------''\n\n\n')
book = m.str3()
f.write(book[-1]['head'])
f.write(book[0]['title'])
f.write('\n')
k = -2
for i in book.keys():
    k = k + 1  # проелы до и после знака операции
    if i > 0:
        if k < 10:
            f.write('    ')
            f.write(str(k))
            f.write('        ')
            f.write(book[i]['surname1'])
            f.write(' ')
            f.write(book[i]['name'])
            f.write(' ')
            f.write(book[i]['surname2'])
            f.write('\n')
        else:
            f.write('    ')
            f.write(str(k))
            f.write('       ')
            f.write(book[i]['surname1'])
            f.write(' ')
            f.write(book[i]['name'])
            f.write(' ')
            f.write(book[i]['surname2'])
f.write('\n''---------- 4 страница ----------''\n\n\n')
f.write("Оглавление" + '\n')
tab = m.str4()
for key in tab.keys():
    f.write(str(key) + '\n')
    for key1 in tab[key]:
        f.write('  ' + str(key1))
        for i in range(len(tab[key][key1])):
            f.write('\t' + tab[key][key1][i])
        f.write('\n')
f.write('\n''---------- 5 страница ----------''\n\n\n')
Attendance_accounting, List = m.str5()
for key in Attendance_accounting.keys():
    f.write(key + " ")
    for i in range(len(Attendance_accounting[key])):
        f.write(str(Attendance_accounting[key][i]) + " ")
    if key != '№ п.п.\ Дата':
        f.write('\n')
for key in List.keys():
    f.write(str(key) + "\t")
    for i in range(len(List[key])):
        if i == 0:
            f.write("\t" + List[key][i] + "\t")
        elif i != len(List[key]) - 2:
            f.write(List[key][i] + "\t")
        else:
            f.write("\t")
            f.write(List[key][i] + "\t\t")
    f.write('\n')
f.write('\n''---------- 6 страница ----------''\n')
table6, head6 = m.str6()
f.write("Учет занятий" + '\n')
f.write(str(head6) + ' \n')
for k in table6[head6].keys():
    for i in range(len(table6[head6][k])):
        f.write(table6[head6][k][i])
    f.write('\n')
f.close()
