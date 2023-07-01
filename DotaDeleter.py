import os

def delete_files(directory, extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Видалено файл: {file_path}")

                except OSError as e:
                    print(f"Помилка під час видалення файлу {file_path}: {e}")

# Задаємо шлях до каталогу, в якому потрібно видалити файли
directory_path = r"C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta"

# Задаємо розширення файлів, які потрібно видалити
file_extension = ".exe", ".txt", ".dll", ".vpk", ".bin", ".cfg", ".log", ".vdf", ".vtf", ".vtx", ".vvd", ".pcf", ".dat", ".sav", ".dem", ".nav", ".png", ".jpg", ".bmp", ".wav", ".mp3", ".mp4", ".avi", ".webm", ".ogg", ".ttf", ".fon", ".otf", ".eot", ".woff", ".woff2", ".ttc", ".zip", ".rar", ".7z", ".bz2", ".xz", ".gz", ".pak", ".vpk", ".vp6", ".vp8", ".vp9", ".vtf", ".vmt", ".vtf", ".vtx", ".vvd", ".pcf", ".dat", ".sav", ".dem", ".nav", ".png", ".jpg", ".bmp", ".wav", ".mp3", ".mp4", ".avi", ".webm", ".ogg", ".ttf", ".fon", ".otf", ".eot", ".woff", ".woff2", ".ttc", ".zip", ".rar", ".7z", ".bz2", ".xz", ".gz", ".pak", ".vpk", ".vp6", ".vp8", ".vp9", ".vtf", ".vmt", ".vtf", ".vtx", ".vvd", ".pcf", ".dat", ".sav", ".dem", ".nav", ".png", ".jpg", ".bmp", ".wav", ".mp3", ".mp4", ".avi", ".webm", ".ogg", ".ttf", ".fon", ".otf", ".eot", ".woff", ".woff2", ".ttc", ".zip", ".rar", ".7z", ".bz2", ".xz", ".gz", ".pak", ".vpk", ".vp6", ".vp8", ".vp9", ".vtf", ".vmt", ".vtf", ".vtx", ".vvd", ".pcf", ".dat", ".sav", ".dem", ".nav", ".png", ".jpg", ".bmp", ".wav", ".mp3", ".mp4", ".avi", ".webm", ".ogg", ".ttf", ".fon", ".otf", ".eot", ".woff", ".woff2", ".ttc", ".zip", ".rar", ".7z"

# Викликаємо функцію для видалення файлів
delete_files(directory_path, file_extension)
