# “Приложение заметки”

# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных.
# При чтении списка заметок реализовать фильтрацию по дате

import os
from datetime import datetime
class Note:
    def __init__(self, id, dtime, header, txt):
        self.id = id
        self.dtime = dtime
        self.header = header
        self.txt = txt

    def header_preview(self, length):
        return self.header[:length] + '...' if len(self.header) > length else self.header

    def txt_preview(self, length):
        preview = self.txt[:length] + '...' if len(self.txt) > length else self.txt
        return preview.replace("/n", " ")

def sort_notes(type, reverse=False):
    if type == 'by_id':
        return sorted(notes, key=lambda note: note.id, reverse=reverse)
    elif type == 'by_date':
        return sorted(notes, key=lambda note: datetime.strptime(note.dtime, "%d.%m.%y %H:%M:%S"), reverse=reverse)

def print_notes(notes):
    os.system('cls')
    print('0. Назад...')
    for i, note in enumerate(notes):
        print(f'{i + 1}. #{note.id} {note.dtime} {note.header_preview(40)} {note.txt_preview(80)}')

def main_menu():
    # Основное меню:
    # 1. Вывести заметки
    #   1.1 Весь список
    #   1.2 Поиск
    #       1.2.1 По названию
    #       1.2.2 По дате
    # 2. Новая заметка
    # 0. Выход

    # Меню заметки:
    # 1. Редактировать
    # 2. Удалить
    # 0. Назад

    MENU_TXT = \
        '1. Вывести заметки \n' + \
        '   1.1 Новые вначале \n' + \
        '   1.2 Старые вначале \n' + \
        '2 Поиск \n' + \
        '   2.1 По названию \n' + \
        '   2.2 По дате \n' + \
        '3. Новая заметка \n' + \
        '0. Выход'

    while True:
        os.system('cls')
        print(MENU_TXT)
        input_num = input('Выберите пункт меню: ')
        if input_num == '1.1':
            sorted_notes=sort_notes('by_date', reverse=True) 
            print_notes(sorted_notes)
            i = int(input('Выберите заметку: '))
            if 0 < i <= len(sorted_notes):
                note_menu(sorted_notes[i - 1])
        elif input_num == '1.2':
            sorted_notes=sort_notes('by_date') 
            print_notes(sorted_notes)
            i = int(input('Выберите заметку: '))
            if 0 < i <= len(sorted_notes):
                note_menu(sorted_notes[i - 1])
        elif input_num == '2.1':
            print_note('find_header')
        elif input_num == '2.2':
            print_note('find_dtime')
        elif input_num == '3':
            add_new()
        elif input_num == '0':
            break    
        # input('Нажмите Enter для продолжения...')

def note_menu(note):
    MENU_TXT = \
        '1. Редактировать \n' + \
        '2. Удалить \n' + \
        '0. Назад'

    while True:
        os.system('cls')
        print(f'ID: #{note.id}\n' + \
            f'Дата: {note.dtime}\n' + \
            f'Заголовок: {note.header}\n' + \
            f'Текст: {note.txt}')
        print(MENU_TXT)
        input_num = input('Выберите пункт меню: ')
        if input_num == '1':
            pass
        elif input_num == '2':
            notes.remove(note)
        break

notes = [Note('001', \
            '12.12.23 10:23:12', \
            'Очень длинное название ...........................................................................', \
            'Очень длинное содержание ............................../n...........................................'),
        Note('002', \
            '12.11.23 09:11:36', \
            'Другое очень длинное название ...........................................................................', \
            'Другое очень длинное содержание ............................../n...........................................'),
        Note('003', \
            '12.12.23 08:11:36', \
            'Третье очень длинное название ...........................................................................', \
            'Третье очень длинное содержание ............................../n...........................................'),
        Note('004', \
            '01.12.23 10:10:36', \
            'Другое очень длинное название ...........................................................................', \
            'Другое очень длинное содержание ............................../n...........................................')]
main_menu()