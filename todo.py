class Todo:
    #instructions for how to construct a new todo object
    # use the __init__() to create instances (THINGS) of the todo class.
    # Also known as the "constructor"
    # "dunder init" - double underscore init (__init__)
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    # behaviors
    #examples of "encapsulation". this means you hide the details of how your code works. 
    # you manage that yourself. You present an interface to anybody using your code, 
    # but you don't require them to know those details.
    def update_title(self, new_title):
        self.title != new_title
        self.updated_on = '2019-11-18' #whatever the current date really i
    def update_completed(self, new_completed):
        self.completed = new_completed
        if self.completed:
            self.completed_on = "Current Date" #calculate function later

    def display(self):
        # You must use the keyword "self" as the 
        # first argument so that an 
        # object can call the fucntion. 
        # It links the function to the object
        print(self.title)

    def __str__(self):
        return f"{self.title} ({self.completed})"