from services.TodoService import TodoService
from utils.InputUtil import InputUtil

class TodoView:
    def __init__(self, todo_service: TodoService):
        self.todo_service = todo_service

    def show_todos(self):
        while True:
            self.todo_service.show_todos()

            print("\nMenu:")
            print("1. Tambah")
            print("2. Ubah")
            print("3. Cari")
            print("4. Urutkan")
            print("5. Hapus")
            print("x. Keluar")

            choice = InputUtil.input("Pilih")
            stop = False

            if choice == "1":
                self.add_todo()
            elif choice == "2":
                self.update_todo()
            elif choice == "3":
                self.search_todo()
            elif choice == "4":
                self.sort_todo()
            elif choice == "5":
                self.remove_todo()
            elif choice.lower() == "x":
                stop = True
            else:
                print("[!] Pilihan tidak dimengerti.")

            if stop:
                break

            print()

    def add_todo(self):
        print("[Menambah Todo]")
        title = InputUtil.input("Judul (x Jika Batal)")
        if title.lower() != "x":
            self.todo_service.add_todo(title)

    def remove_todo(self):
        print("[Menghapus Todo]")
        str_id = InputUtil.input("[ID Todo] yang dihapus (x Jika Batal)")
        if str_id.lower() != "x":
            try:
                todo_id = int(str_id)
                self.todo_service.remove_todo(todo_id)
            except ValueError:
                print("[!] ID harus berupa angka.")

    def update_todo(self):
        print("[Mengubah Todo]")
        # TODO: implement update functionality
        pass

    def search_todo(self):
        print("[Mencari Todo]")
        # TODO: implement search functionality
        pass

    def sort_todo(self):
        print("[Mengurutkan Todo]")
        # TODO: implement sort functionality
        pass