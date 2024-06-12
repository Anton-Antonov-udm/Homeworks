import os
import time

directory = '.'
# directory = 'C:\\pythonProject\\Homeworks'

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)  # полный путь до файла
        file_time = os.path.getmtime(file_path)  # время последнего изменения в секундах
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))  # привычный формат времени
        file_size = os.path.getsize(file_path)  # размер файла
        parent_dir = os.path.dirname(file_path)  # директория в которой находится файл
        print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
