file_name = 'notes.csv'

main_menu = '''\nГлавное меню:
1. Открыть заметки
2. Сохранить заметки в файл
3. Показать заметки
4. Добавить заметку
5. Найти заметку по дате
6. Изменить заметку
7. Удалить заметку
8. Выход\n'''

input_choice = 'Выберите пункт меню: '

load_success = 'Заметки успешно открыты!'

save_success = 'Заметки успешно сохранены в файл!'

nb_empty = 'Файл заметок пуст или не загружен!'

input_new_note = "Введите данные новой заметки: "

new_note = {'id': '0',
            'name': 'Введите название заметки: ',
            'text': 'Введите текст заметки: ',
            'date': '0'}

def new_note_success(name: str):
    return f'Заметка {name} успешно добавлен!'

input_search = 'Введите дату заметки для поиска: '

def empty_search(date):
    return f'Заметки по дате "{date}" не найдены!'

# change note
input_modify = 'Какую заметку будем менять? Введите дату для поиска: '
modify_note = 'Введите новые данные или оставьте поле пустым, чтобы ничего не менять: '
input_index_modify = 'Ведите индекс заметки для изменения: '


def modify_success(name: str):
    return f'Заметка "{name}" успешно изменена!'

# delete note
input_delete = 'Какую заметку будем удалять? Введите дату для поиска: '
input_index_delete = 'Ведите индекс заметки для удаления: '

def delete_confirm(name: str):
    return f'\nВы уверены, что хотите удалить заметку "{name}" (Y/N)?: '

def delete_success(name: str):
    return f'Заметка "{name}" успешно удалена!'