'''
2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

with open("file_task_2.txt", encoding='utf-8') as f_obj:
    list_s = f_obj.readlines()
    print(f"Количество строк: {len(list_s)}")
    for i, el in enumerate(list_s):
        print(f"В строке №-{i + 1} - {len(el.split(' '))} слова")
