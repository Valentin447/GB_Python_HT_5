'''
5) Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
'''

my_numbers = []

with open("file_task_5", "a", encoding="utf-8") as f_obj:
    while True:
        s = input("Введите число: ")
        if s == "":
            break
        try:
            num = int(s)
        except ValueError:
            print("Неверный ввод!")
        print(f"{num} ", file=f_obj, end="")

with open("file_task_5", "r", encoding="utf-8") as f2_obj:
    num_list = f2_obj.read().split(" ")
    my_sum = 0
    for el in num_list:
        if el != "":
            my_sum += int(el)
    print(f"Сумма чисел: {my_sum}")
