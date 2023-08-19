import text

def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        
# print input message
def print_message(message: str):
    print('\n' + '='*len(message))
    print(message)
    print('='*len(message) + '\n')

# print all notes
def print_notes(book: list[dict[str, str]], error: str):
    message_len = 70
    if book:
        print('\n' + '='*message_len)
        for note in book:
            print(f'{note.get("id"):>3}.{note.get("name"):^50} | {note.get("text"):<900} | {note.get("date"):<30}')
        print(message_len*'=' + '\n')
    else:
        print_message(error)

# create new note
def input_note(message: str) -> dict[str, str]:
    new = {}
    print(message)
    for key, txt in text.new_note.items():
        if(key != 'id' and key != 'date'):
            cur_val = input(txt)
            if cur_val:
                new[key] = cur_val
        else:
            new[key] = '0'
    return new

# search note
def input_search(message: str) -> str:
    return input(message)

# confirmation for deletion
def confirm_delete(name: str):
    confirm = input(text.delete_confirm(name)).lower()
    if confirm == 'y':
        return True
    else:
        return False