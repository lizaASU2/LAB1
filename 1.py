print('\n''---------- 1 страница ----------''\n')
# вводим список на 1 странице
tit={
    'str1':{'tit':'\t \t Министерство науки и высшего образования РФ \n \t Федеральное государственное бюджетное образовательное учреждение\n\t\t\t высшего образования\n\t"Пермский национальный исследовательский политехнический университет"'.expandtabs(10)},
    'str2':{'tit':'\t Ж У Р Н А Л \n\tучета занятий'.expandtabs(34)},
    'str3':{'tit':'2019/2020 учебный год'.center(80)},
    'str4':{'tit':'Очная форма обучения'.center(80)},
    'str5':{'tit':'Группа № АСУ2-19-1м'.center(80)},
    'str6':{'tit':'\t Направление(специальность) Информатика и вычислительная\n\t\tтехника (Интеллектуальные системы)'.expandtabs(10)}
    }
for j in tit.keys():
    print(tit[j]['tit']) # вывоим строчки
    if j=='str1'or j=='str2'or j=='str4': print('\n')# добавляем пробелы
print('\n''---------- 3 страница ----------''\n')
# вводим список на 3 странице
book={
    -1:{'head':'СПИСОК СТУДЕНТОВ ГРУППЫ     1-й семестр''\n'},
     0: {'title':'| № п.п |   Фамилия,имя и отчество студента''\n''\t''\t''\t''\t''\t'' (полностью)''\n'},
     1: {'surname1': 'Аюпов','name': 'Александр','surname2':'Дамирович'},
     2: {'surname1': 'Барсуков','name': 'Андрей','surname2':'Сергеевич'},
     3: {'surname1': 'Беляев','name': 'Евгений','surname2':'Леонидович'},
     4: {'surname1': 'Боброва', 'name': 'Ирина', 'surname2': 'Александровна'},
     5: {'surname1': 'Гребеньщикова', 'name': 'Елизавета', 'surname2': 'Витальевна'},
     6: {'surname1': 'Клейменова', 'name': 'Вероника', 'surname2': 'Альбертовна'},
     7: {'surname1': 'Князев','name': 'Александр','surname2':'Игоревич'},
     8: {'surname1': 'Орлова','name': 'Екатерина','surname2':'Дмитриевна'},
     9: {'surname1': 'Фоминых','name': 'Полина','surname2':'Юрьевна'},
     10:{'surname1': 'Швецов','name':' Владислав','surname2':'Валерьевич'},
    }
print(book[-1]['head'])#выводим 1 строчку
print(book[0]['title'])#выводим 2 строчку
a = -2 #порядковый номер студента в списке
for i in book.keys():
    a=a+1
    if i>0:
        if a<10:
            print('   ',a,'     ',book[i]['surname1'],book[i]['name'],book[i]['surname2']) #выводим всех студентов до 10
        else:
            print('   ', a, '    ', book[i]['surname1'], book[i]['name'], book[i]['surname2']) #выводим всех студентов >= 10
#-------------------------- вывод в файл ---------------------------------------------------------------------
f=open('journal.txt','w')
f.write('\n''---------- 1 страница ----------''\n\n\n')
for l in tit.keys():
    if l=='str2'or l=='str3'or l=='str5':
        f.write('\n\n\n')
    f.write(tit[l]['tit'])
    f.write('\n')
f.write('\n\n\n''---------- 3 страница ----------''\n\n\n')
f.write(book[-1]['head'])
f.write(book[0]['title'])
f.write('\n')
k = -2
for i in book.keys():
    k=k+1
    if i>0:
        if k<10:
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
f.close()