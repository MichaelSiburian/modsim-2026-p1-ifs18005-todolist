from typing import List
from entities.Todo import Todo

class TodoRepository():
    def __init__(self):
        self.data: List[Todo] = []  # type: ignore

    def get_all_todos(self) -> List[Todo]: # type: ignore
        return self.data

    def add_todo(self, new_todo: Todo):
        self.data.append(new_todo)

    def remove_todo(self, id: int) -> bool:
        # cari todo berdasarkan id
        target_todo = next((todo for todo in self.data if todo.id == id), None)
        if target_todo is None:
            return False
        self.data.remove(target_todo)
        return True