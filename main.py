from repositories.TodoRepository import TodoRepository
from services.TodoService import TodoService
from views.TodoView import TodoView

def main():
    # Buat repository
    todo_repository = TodoRepository()

    # Buat service
    todo_service = TodoService(todo_repository)

    # Buat view
    todo_view = TodoView(todo_service)

    # Jalankan aplikasi
    todo_view.show_todos()

if __name__ == "__main__":
    main()
