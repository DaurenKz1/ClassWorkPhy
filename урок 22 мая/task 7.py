volume = input("Введите объем вашей флешки в гб: ")
size = input("Введите разменр файла в мб: ")

try:
    flash_drive_size = float(volume)
    file_size_mb= float(size)
    file_size_gb = file_size_mb * 1024
    copies = flash_drive_size/file_size_gb
except ValueError:
    print("Ошибка! Вы ввли нек число!")
except ZeroDivisionError:
    print("Ошибка! Размер файла не может юыть 0!")
else:
    print(copies)