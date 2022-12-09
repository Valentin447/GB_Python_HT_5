'''
3) Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''

with open("file_task_3.txt", encoding="utf-8") as f_obj:
    f_list = f_obj.readlines()
    my_sum = 0
    print("Сотрудники с ЗП ниже 20000:")
    for el in f_list:
        worker = el.split(" ")
        salary = float(worker[1])
        my_sum += salary
        if salary < 20000:
            print(f"{worker[0]}")
    print(f"Средняя ЗП: {round(my_sum / len(f_list), 2)}")
