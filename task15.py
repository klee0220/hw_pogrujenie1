"""
 Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
 Соберите информацию о содержимом в виде объектов namedtuple.
 Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
 В процессе сбора сохраните данные в текстовый файл, используя логирование.
"""
import argparse
import logging
import os
from collections import namedtuple

logger = logging.getLogger(__name__)
file_info_format = '{msg}'
logging.basicConfig(filename='dirlib.txt', filemode='w', encoding='UTF-8',
                    level=logging.NOTSET, style='{', format=file_info_format)


def get_dir_info(_dir):
    try:

        if _dir is None:
            raise ValueError
        if not isinstance(_dir, str):
            raise TypeError
        if not os.path.exists(_dir):
            raise FileNotFoundError

        Path_object = namedtuple('Path_object', ['name', 'type', 'parent_path'], defaults=[None, None])
        list_obj = []

        for dir_path, dirs_name, files_name in os.walk(_dir):

            if dirs_name and not os.path.dirname(dir_path):
                for dir_name in dirs_name:
                    dir_obj = Path_object(name=dir_name,
                                          type='directory',
                                          parent_path=dir_path)
                    list_obj.append(dir_obj)

            elif dirs_name and os.path.dirname(dir_path):
                for dir_name in dirs_name:
                    dir_obj = Path_object(name=dir_name,
                                          type='directory',
                                          parent_path=os.path.basename(dir_path))
                    list_obj.append(dir_obj)

                    for file_name in files_name:
                        dir_obj = Path_object(name=os.path.splitext(file_name)[0],
                                              type=os.path.splitext(file_name)[1],
                                              parent_path=os.path.basename(dir_path))
                    list_obj.append(dir_obj)
        for dir_obj in list_obj:
            logger.info(msg=f'Object: {dir_obj.name:<10}' +
                            f'Type: {dir_obj.type:<15}' +
                            f'Parent path name: {dir_obj.parent_path}.')
        return list_obj

    except ValueError:
        print('Path should be entered.')
    except TypeError:
        print('Path should be a string.')
    except FileNotFoundError:
        print(f'Path {_dir} does not exist.')
    except NotADirectoryError:
        print(f'{_dir} is not a directory.')
    except PermissionError:
        print('You do not have enough permission level')
    except Exception:
        print('Unknown error')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get directory contains')
    parser.add_argument('dir', metavar='dir', type=str, nargs=1, help='enter a path')
    args = parser.parse_args()
    get_dir_info(*args.dir)
