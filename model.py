from datetime import datetime
import os

class Notes:

    def __init__(self, path: str):
        self._notes: list[dict[str, str]] = []
        self._path = path
        self._last_id = 0

    # open notes file
    def open(self):
        with open(self._path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for note in data:
            note = note.strip().split(':')
            new = {'id':note[0], 'name':note[1], 'text': note[2], 'date': note[3]}
            self._notes.append(new)

    # save notes
    def save(self):
        data = []
        for note in self._notes:
            data.append(':'.join([value for value in note.values()]))
            data = '\n'.join(data)

        with open(self._path, 'w', encoding = 'UTF-8') as file:
            file.write(data)

    # load notes
    def load(self):
        return self._notes
    
    # add notes
    def add(self, new: dict[str, str]) -> str:
        self._last_id += 1
        new['id'] = str(self._last_id)
        new['date'] = str(datetime.now().replace(microsecond=0))
        self._notes.append(new)
        return new.get('name')
    
    # search in notes
    def search(self, date: str) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        for note in self._notes:
            if date in note.get('date'):
                result.append(note)
        return result
    
    # change chosen note
    def modify(self, new: dict, index: int):
        for note in self._notes:
            if index == note.get('id'):
                note['name'] = new.get('name', note.get('name'))
                note['text'] = new.get('text', note.get('text'))
                note['date'] = str(datetime.now().replace(microsecond=0))
                return note.get('name')
            
    # delete chosen note
    def delete(self, index: int) -> str:
        for i in range(len(self._notes)):
            if index == self._notes[i].get('id'):
                name = self._notes[i].get('name')
                del self._notes[i]
                return name