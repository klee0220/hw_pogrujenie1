'''
Напишите функцию группового переименования файлов.
Она должна:

1 принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.

2 принимать параметр количество цифр в порядковом номере.

3 принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.

4 принимать параметр расширение конечного файла.

5 принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение.

Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами.

'''
import os


def batch_rename(new_name, digits, source_ext, dest_ext, range_name, path='.'):
    counter = 1
    for filename in os.listdir(path):
        if filename.endswith(source_ext):

            old_name = os.path.splitext(filename)[0] # get the name without extension
            old_name_substring = old_name[range_name[0]:range_name[1]] if range_name else ""
            new_filename = f"{old_name_substring}{new_name}{str(counter).zfill(digits)}{dest_ext}"
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
            counter += 1


batch_rename('new_file', 3, '.txt', '.md', [1, 3], './for7')
batch_rename('new_file', 3, '.html', '.txt', [1, 3], './for7')
