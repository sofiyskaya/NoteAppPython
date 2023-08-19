import view
import model
import text

my_nb = model.Notes(text.file_name)

def start():
    while True:
        choice = view.main_menu()

        match choice:
            # open csv file
            case 1:
                my_nb.open()
                view.print_message(text.load_success)

            # save notes to csv file
            case 2:
                my_nb.save()
                view.print_message(text.save_success)

            # load notes
            case 3:
                notes = my_nb.load()
                view.print_notes(notes, text.nb_empty)

            # add note
            case 4:
                note = view.input_note(text.input_new_note)
                name = my_nb.add(note)
                view.print_message(text.new_note_success(name))

            # research note by date
            case 5:
                date_search = view.input_search(text.input_search)
                result = my_nb.search(date_search)
                view.print_notes(result, text.empty_search(date_search))

            # change note
            case 6:
                date_search = view.input_search(text.input_modify)
                result = my_nb.search(date_search)
                if result:
                    if len(result) != 1:
                        view.print_notes(result, '')
                        current_id = view.input_search(text.input_index_modify)
                    else:
                        current_id = result[0].get('id')

                    note = view.input_note(text.modify_note)
                    name = my_nb.modify(note, current_id)
                    view.print_message(text.modify_success(name))
                else:
                    view.print_message(text.empty_search(date_search))

            # delete note
            case 7:
                date_search = view.input_search(text.input_delete)
                result = my_nb.search(date_search)
                if result:
                    if len(result) != 1:
                        view.print_notes(result, '')
                        del_id = view.input_search(text.input_index_delete)
                    else:
                        del_id = result[0].get('id')

                    name = my_nb.delete(del_id)
                    view.print_message(text.delete_success(name))
                else:
                    view.print_message(text.empty_search(date_search))

            case 8:
                break
             