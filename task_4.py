'''
4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл.
'''

my_dic = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

with open("file_task_4.txt", encoding="utf-8") as f_obj1:
    with open("file_task_4_1.txt", "w", encoding="utf-8") as f_obj2:
        for s in f_obj1:
            new_s = s
            for item in my_dic.items():
                if s.find(item[0]) != -1:
                    new_s = s.replace(item[0], item[1])
            print(new_s, file=f_obj2, end="")
