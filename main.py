import os.path
import psutil
import zipfile
import json
import xml.etree.ElementTree as ET

#информация о дисках
def get_logical_drives_info():
    drives = psutil.disk_partitions()

    for drive in drives:
        drive_name = drive.device
        volume_label = drive.mountpoint
        file_system_type = drive.fstype
        file_system_size = psutil.disk_usage(drive_name).total

        print(f"Логический диск: {drive_name}")
        print(f"Имя диска: {volume_label}")
        print(f"Тип файловой системы: {file_system_type}")
        print(f"Размер: {file_system_size} байт\n")

def name_check(name):
    forb_sym = ["#", "%", "&", "{", "}", "\\", "<", ">", "*", "?", "/", "!", "'", "\"", "$", ":", "@", "+", "`", "|", "="]
    for sym in forb_sym:
        if sym not in name:
            continue
        else:
            print(f"Имя файла не должно содержать символ '{sym}'")
            return False
    return True


def create_file():
    filename = input("Введите имя нового файла (-1 для выхода в меню):")
    if filename == "-1":
        print("\n")
        menu()
    #проверка названия на запрещенные символы
    if not name_check(filename):
        create_file()
    filename = +".txt"
    #создание файла
    if not os.path.exists(filename):
         file = open(filename, 'w')
         file.close()
         print(f"Файл '{filename}' создан.\n")
    else:
        print("Файл с данным именем уже существует.\n")
        create_file()
    print("\n")

def add_to_file():
    filename = input("Введите имя файла (-1 для выхода в меню):")
    if filename == "-1":
        print("\n")
        menu()
    filename = +".txt"
    if os.path.exists(filename):
        file = open(filename, 'a')
        text = input("Введите текст для добавления к файлу: ")
        file.write(text)
        file.close()
        print(f"Текст добавлен к файлу '{filename}'.\n")
    else:
        print("Файла с данным именем не существует.\n")
        add_to_file()
    print("\n")

def read_from_file():
    filename = input("Введите имя файла (-1 для выхода в меню):")
    if filename == "-1":
        print("\n")
        menu()
    filename = +".txt"
    if os.path.exists(filename):
        file = open(filename, 'r')
        print("Текст файла:\n")
        print(file.read())
        file.close()
    else:
        print("Файла с данным именем не существует.\n")
        read_from_file()
    print("\n")

def delete_file():
    filename = input("Введите имя файла (-1 для выхода в меню):")
    if filename == "-1":
        print("\n")
        menu()
    filename = +".txt"
    if os.path.exists(filename):
        os.remove(filename)
        print("Файл удален.\n")
    else:
        print("Файла с данным именем не существует.\n")
        delete_file()
    print("\n")

def create_json():
    filename = input("Введите имя нового файла (-1 для выхода в меню):")
    if filename == "-1":
        print("\n")
        menu()
    #проверка названия на запрещенные символы
    if not name_check(filename):
        create_json()
    filename = +".json"
    #создание файла
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump({}, f)
        print(f"Файл '{filename}' создан.\n")
    else:
        print("Файл с данным именем уже существует.\n")
        create_json()
    print("\n")


def add_to_json():
    filename = input("Введите имя файла (-1 для выхода в меню):")
    if filename == "-1":
        print("\n")
        menu()
    filename = +".json"
    if os.path.exists(filename):
        with open(filename, 'r+') as file:
            key = input("Введите ключ объекта для добавления к файлу: ")
            val = input("Введите значение объекта для добавления к файлу: ")
            new_object = json.loads("{\""+key+"\" : \""+val+"\"}")
            data = json.load(file)
            data.update(new_object)
            file.seek(0)
            json.dump(data, file)
        print(f"Объект добавлен к файлу '{filename}'.\n")
    else:
        print("Файла с данным именем не существует.\n")
        add_to_json()
    print("\n")


def read_from_json():
    filename = input("Введите имя файла (-1 для выхода в меню):")
    if filename == "-1":
        print("\n")
        menu()
    filename = +".json"
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            print("Содержимое файла:\n")
            print(json.dumps(data, indent=4))
    else:
        print("Файла с данным именем не существует.\n")
        read_from_json()
    print("\n")

def delete_json():
    filename = input("Введите имя файла (-1 для выхода в меню):")
    if filename == "-1":
        print("\n")
        menu()
    filename = +".json"
    if os.path.exists(filename):
        os.remove(filename)
        print("Файл удален.\n")
    else:
        print("Файла с данным именем не существует.\n")
        delete_json()
    print("\n")

def create_xml():
    filename = input("Введите имя нового файла (-1 для выхода в меню):")
    if filename == "-1":
        print("\n")
        menu()
    # проверка названия на запрещенные символы
    if not name_check(filename):
        create_xml()
    filename = +".xml"
    # создание файла
    if not os.path.exists(filename):
        rootname = input("Введите имя корня: ")
        root = ET.Element(rootname)
        tree = ET.ElementTree(root)
        tree.write(filename)
        print(f"Файл '{filename}' создан.\n")
    else:
        print("Файл с данным именем уже существует.\n")
        create_xml()
    print("\n")

def add_to_xml():
    filename = input("Введите имя файла (-1 для выхода в меню): ")
    if filename == "-1":
        print("\n")
        menu()
    filename = +".xml"
    if os.path.exists(filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        itemname = input("Введите имя элемента: ")
        data = input("Введите значение элемента: ")
        # Создание нового элемента
        new_element = ET.Element(itemname)
        new_element.text = data
        root.append(new_element)
        # Сохраняем изменения в XML файле
        tree.write(filename)

        print(f"Объект добавлен к файлу '{filename}'.\n")
    else:
        print("Файла с данным именем не существует.\n")
        add_to_xml()
    print("\n")

def read_from_xml():
    filename = input("Введите имя файла (-1 для выхода в меню):")
    if filename == "-1":
        print("\n")
        menu()
    filename = +".xml"
    if os.path.exists(filename):
        print("Содержимое файла:\n")
        tree = ET.parse(filename)
        root = tree.getroot()
        display_element(root)
    else:
        print("Файла с данным именем не существует.\n")
        read_from_xml()
    print("\n")


def display_element(element, depth=0):
    # Вывод названия элемента с отступом в зависимости от глубины
    indent = ' ' * depth
    print(indent + "<" + element.tag + ">")

    # Вывод значения элемента, если оно есть
    if element.text and element.text.strip():
        print(indent + '  ' + element.text.strip())

    # Рекурсивный вызов для дочерних элементов
    for child in element:
        display_element(child, depth + 1)


def delete_xml():
    filename = input("Введите имя файла (-1 для выхода в меню):")
    if filename == "-1":
        print("\n")
        menu()
    filename = +".xml"
    if os.path.exists(filename):
        os.remove(filename)
        print("Файл удален.\n")
    else:
        print("Файла с данным именем не существует.\n")
        delete_xml()
    print("\n")


def create_zip():
    filename = input("Введите имя нового архива (-1 для выхода в меню):")
    if filename == "-1":
        print("\n")
        menu()
    # проверка названия на запрещенные символы
    if not name_check(filename):
        create_zip()
    filename = +".zip"
    # создание файла
    if not os.path.exists(filename):
        with zipfile.ZipFile(filename, 'w') as zipf:
            print(f"Архив '{filename}' создан.\n")
    else:
        print("Архив с данным именем уже существует.\n")
        create_zip()
    print("\n")


def add_to_zip():
    filename = input("Введите имя файла, добавляемого в архив c его расширением(-1 для выхода в меню):")
    if filename == "-1":
        print("\n")
        menu()
    # создание файла
    if os.path.exists(filename):
        zipname = input("Введите название архива: ")
        zipname = +".zip"
        with zipfile.ZipFile(zipname, 'a') as zipf:
            zipf.write(filename)
            print(f"Файл '{filename}' добавлен в архив '{zipname}'.")
    else:
        print("Файла с данным именем не существует.\n")
        add_to_zip()
    print("\n")


def unzip_file():
    zipname = input("Введите название архива (-1 для выхода в меню):")
    if zipname == "-1":
        menu()
    zipname = +".zip"
    if os.path.exists(zipname):
        with zipfile.ZipFile(zipname, 'r') as zipf:
            print(f"Содержимое архива: {zipname}")
            for info in zipf.infolist():
                print(f"  - {info.filename}")
                print(f"    Размер файла в архиве: {info.compress_size} бит")
                print(f"    Полный размер файла: {info.file_size} бит")
            zipf.extractall()
            print(f"\nАрхив '{zipname}' успешно разархивирован")
    else:
        print("Архива с данным именем не существует.\n")
        unzip_file()
    print("\n")


def delete_zip():
    zipname = input("Введите имя архива для удаления (-1 для выхода в меню):")
    if zipname == "-1":
        print("\n")
        menu()
    zipname = +".zip"
    if os.path.exists(zipname):
        if input("Удалить файлы, извлеченные из архива? (да/нет): ")=="да":
            with zipfile.ZipFile(zipname, 'r') as zipf:
                for info in zipf.infolist():
                    os.remove(info.filename)
                    print(f"Файл '{info.filename}' успешно удален.")
        os.remove(zipname)
        print(f"Архив '{zipname}' успешно удален.")
    else:
        print("Архива с данным именем не существует.\n")
        delete_zip()
    print("\n")



#корневое меню
def menu():
    print("1 - Информация о логических дисках \n"
              "2 - Работа с файлами \n"
              "3 - Работа с форматом JSON \n"
              "4 - Работа с форматом XML\n"
              "5 - Работа с ZIP-архивами\n")
    choice = int(input("Введите номер желаемого действия: "))
    while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5):
        choice = int(input("Некорректное значение. Введите номер желаемого действия: "))
    menuActivation(choice)

#подменю
def menuActivation(choice):
    print("\n")
    if choice == 1:
        get_logical_drives_info()
        menu()
    elif choice == 2:
        submenu_files()
    elif choice == 3:
        submenu_json()
    elif choice == 4:
        submenu_xml()
    elif choice == 5:
        submenu_zip()

def submenu_files():
    print("1 - Создание файла \n"
              "2 - Добавление текста в файл \n"
              "3 - Чтение файла \n"
              "4 - Удаление файла\n"
              "-1 - Выход в главное меню\n")
    choice = int(input("Введите номер желаемого действия: "))
    while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice!=-1):
        choice = int(input("Некорректное значение. Введите номер желаемого действия: "))
    if choice==1:
        create_file()
    elif choice==2:
        add_to_file()
    elif choice==3:
        read_from_file()
    elif choice == 4:
        delete_file()
    else:
        print("\n")
    submenu_files()


def submenu_json():
    print("1 - Создание файла json \n"
              "2 - Добавление объекта в файл json \n"
              "3 - Чтение файла json\n"
              "4 - Удаление файла json\n"
              "-1 - Выход в главное меню\n")
    choice = int(input("Введите номер желаемого действия: "))
    while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice!=-1):
        choice = int(input("Некорректное значение. Введите номер желаемого действия: "))
    if choice==1:
        create_json()
    elif choice==2:
        add_to_json()
    elif choice==3:
        read_from_json()
    elif choice == 4:
        delete_json()
    else:
        print("\n")
    submenu_json()


def submenu_xml():
    print("1 - Создание файла xml\n"
              "2 - Добавление данных в файл xml\n"
              "3 - Чтение файла xml\n"
              "4 - Удаление файла xml\n"
              "-1 - Выход в главное меню\n")
    choice = int(input("Введите номер желаемого действия: "))
    while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice!=-1):
        choice = int(input("Некорректное значение. Введите номер желаемого действия: "))
    if choice == 1:
        create_xml()
    elif choice == 2:
        add_to_xml()
    elif choice == 3:
        read_from_xml()
    elif choice == 4:
        delete_xml()
    else:
        print("\n")
    submenu_xml()


def submenu_zip():
    print("1 - Создание файла zip\n"
              "2 - Добавление файлов в архив zip\n"
              "3 - Распаковка архива zip\n"
              "4 - Удаление архива zip\n"
              "-1 - Выход в главное меню\n")
    choice = int(input("Введите номер желаемого действия: "))
    while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice!=-1):
        choice = int(input("Некорректное значение. Введите номер желаемого действия: "))
    if choice == 1:
        create_zip()
    elif choice == 2:
        add_to_zip()
    elif choice == 3:
        unzip_file()
    elif choice == 4:
        delete_zip()
    else:
        print("\n")
        menu()
    submenu_zip()

menu()
