#Задание 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#Об окончании ввода данных свидетельствует пустая строка.

file = open('file1.txt', 'w')
line = input('Введите текст \n')
while line:
    file.writelines(line)
    line = input('Введите текст (для завершения программы нажмите enter без текста) \n')
    if not line:
        break

file.close()
file = open('file1.txt', 'r')
content = file.readlines()
print(content)
file.close()

#Задание 2.Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
#количества слов в каждой строке.

file = open('file2.txt', 'r')
reading = file.read()
print(f'Содержимое файла: \n {content}')
file = open('file2.txt', 'r')
reading = file.readlines()
print(f'Количество строк в файле - {len(reading)}')
file = open('file2.txt', 'r')
reading = file.readlines()
for i  in range(len(reading)):
    lastDigit = (i + 1) % 10
    penultimateAndLastDigit = (i + 1) % 100
    if(lastDigit != 3 | penultimateAndLastDigit != 13):
        print(f'Колличество символов {i + 1} - ой строки {len(reading[i])}')
    else:
        print(f'Колличество символов {i + 1} - ей строки {len(reading[i])}')
file = open('file2.txt', 'r')
reading = file.read()
reading = reading.split()
print(f'Общее количество слов - {len(reading)}')
file.close()

#Задание 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
#величины дохода сотрудников. 

with open('file3.txt', 'r') as file:
    sal = []
    poor = []
    list = file.read().split('\n')
    for i in list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
sum = round(sum(map(int, sal)) / len(sal), 2)
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum}')

#Задание 4. Создать (не программно) текстовый файл со следующим содержимым:
#One - 1
#Two - 2
#Three - 3
#Four - 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
#числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


translate = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
file = []
with open('file4.txt', 'r') as fileObj:
    for i in fileObj:
        i = i.split(' ', 1)
        file.append(translate[i[0]] + '  ' + i[1])
    print(file)

with open('file4_new.txt', 'w') as fileObj2:
    fileObj2.writelines(file)

#Задание 5.Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
#подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
    try:
        with open('file5.txt', 'w+') as fileObj:
            line = input('Введите цифры через пробел \n')
            fileObj.writelines(line)
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')

    with open('file5.txt', 'r') as fileObj:
        list = fileObj.read().split(' ')
        sum = 0
        for i in list:
            sum += int(i)
        print(sum)
summary()

#Задание 6.Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
#практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
#были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
#Вывести словарь на экран. Примеры строк файла: Информатика:
#100(л)   50(пр)   20(лаб).
#Физика:   30(л)   —   10(лаб)
#Физкультура:   —   30(пр)   —
#Пример словаря: {“Информатика”: 170, “Физика”: 40,
#“Физкультура”: 30}

subj = {}
with open('file6.txt', 'r') as initF:
    for line in initF:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')
 
#Создать вручную и заполнить несколькими строками текстовый файл,в котором каждая строка должна содержать данные о фирме:
#наз вание, форма собственности, выручка, издержки. Пример строки файла: firm_1   ООО   10000   5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки,
#в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь 
#с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, 
#{“average_profit”: 2000}]. Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, 
#{"average_profit": 2000}]

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')