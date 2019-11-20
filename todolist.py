from todo import Todo

class TodoList:
    def __init__(self):
        #properties
        #- todos
        self.todos = []
    
    def display(self): 
        for todo in self.todos:
            print(todo)
            
    #assume a new todo isn't already completed
    def add(self, title):
        #instantiate a new todo object
        new_todo = Todo(title, False)
        self.todos.append(new_todo)

    def add_already_completed(self, title):
        new_todo = Todo(title, True)
        self.todos.append(new_todo)

    def complete(self, index):
        todo = self.todos[index]
        # todo.completed = True
        todo.update_completed(True)
#behaviors
# -add
# -print
#- complete