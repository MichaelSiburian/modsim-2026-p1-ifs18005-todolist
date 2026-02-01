from entities.Todo import Todo
from repositories.TodoRepository import TodoRepository

class TodoManager:
    def __init__(self, todo_storage: TodoRepository):
        self.todo_storage = todo_storage
    
    def display_all_tasks(self):
        task_list = self.todo_storage.fetch_all_tasks()
        print("Daftar Todo:")
        
        if len(task_list) == 0:
            print("- Data todo belum tersedia!")
            return
        
        for index, task in enumerate(task_list, 1):
            print(f"{index}. {task}")
    
    def create_new_task(self, task_description: str):
        task_item = Todo(title=task_description)
        self.todo_storage.store_task(task_item)
    
    def delete_task(self, task_id: int):
        deletion_status = self.todo_storage.delete_task(task_id)
        if deletion_status == False:
            print(f"[!] Tidak dapat menghapus todo ID {task_id}.")
    
    def modify_task(self, task_id: int, updated_description: str):
        task_list = self.todo_storage.fetch_all_tasks()
        task_found = False
        
        for task in task_list:
            if task.id == task_id:
                task.title = updated_description
                task_found = True
                print("Perubahan berhasil disimpan.")
                break
        
        if not task_found:
            print("ID todo tidak ditemukan.")
    
    def find_tasks(self, search_term: str):
        task_list = self.todo_storage.fetch_all_tasks()
        search_results = []
        
        for task in task_list:
            if search_term.lower() in task.title.lower():
                search_results.append(task)
        
        return search_results
    
    def organize_tasks(self):
        task_list = self.todo_storage.fetch_all_tasks()
        
        if len(task_list) == 0:
            return []
        
        organized_list = sorted(
            task_list, 
            key=lambda task: task.title.lower()
        )
        
        return organized_list