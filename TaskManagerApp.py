import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QLabel
from PyQt5.QtCore import QDateTime

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        # Title
        self.setWindowTitle("Task Manager App")
        # Sizing upon launch
        self.setGeometry(100, 100, 600, 400)
        
        # Sets json format and calls to load old json information
        self.tasks = {"uncompleted": [], "completed": []}
        self.load_tasks()
        
        # Main layout
        self.layout = QVBoxLayout()
        
        # Input for new tasks
        self.input_field = QLineEdit()
        self.add_button = QPushButton("Add Task")
        
        # Uncompleted tasks layout
        self.uncompleted_label = QLabel("Uncompleted Tasks")
        self.uncompleted_list = QListWidget()
        self.complete_button = QPushButton("Complete Task")
        self.remove_uncompleted_button = QPushButton("Remove Uncompleted Task")
        
        # Completed tasks layout
        self.completed_label = QLabel("Completed Tasks")
        self.completed_list = QListWidget()
        self.remove_completed_button = QPushButton("Remove Completed Task")
        
        # Add widgets to the layout
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.uncompleted_label)
        self.layout.addWidget(self.uncompleted_list)
        self.layout.addWidget(self.complete_button)
        self.layout.addWidget(self.remove_uncompleted_button)
        self.layout.addWidget(self.completed_label)
        self.layout.addWidget(self.completed_list)
        self.layout.addWidget(self.remove_completed_button)
        
        # Button functionality
        self.add_button.clicked.connect(self.add_task)
        self.complete_button.clicked.connect(self.complete_task)
        self.remove_uncompleted_button.clicked.connect(self.remove_uncompleted_task)
        self.remove_completed_button.clicked.connect(self.remove_completed_task)
        
        self.setLayout(self.layout)
        
        self.load_tasks_into_ui()
    
    # Function to load tasks.json
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = {"uncompleted": [], "completed": []}
    
    # Function to save tasks to json
    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
    
    # Function to load tasks into ui
    def load_tasks_into_ui(self):
        self.uncompleted_list.addItems(self.tasks["uncompleted"])
        self.completed_list.addItems(self.tasks["completed"])
    
    # Function to add a task to the uncompleted section
    def add_task(self):
        task = self.input_field.text()
        if task:
            self.tasks["uncompleted"].append(task)
            self.uncompleted_list.addItem(task)
            self.input_field.clear()
            self.save_tasks()
    
    # Function to move a task to the completed section, adds date and time of completion. 
    def complete_task(self):
        selected_task = self.uncompleted_list.currentRow()  # Get the index of the selected task
        if selected_task >= 0:  # Make sure a task is selected
            task_item = self.uncompleted_list.takeItem(selected_task)  # Remove the task from the uncompleted list
            
            # Add date and time of completion
            completion_time = QDateTime.currentDateTime().toString("MM-dd-yy h:mm ap") # Formats date and time ex 1/1/24 1:01 pm
            completed_task = f"{task_item.text()} (Completed on: {completion_time})" # Adds date and time onto the task
            
            # Add the task to the completed list
            self.tasks["uncompleted"].pop(selected_task)
            self.tasks["completed"].append(completed_task)
            self.completed_list.addItem(completed_task)
            self.save_tasks()
    
    # Function to remove an uncompleted task from json
    def remove_uncompleted_task(self):
        selected_task = self.uncompleted_list.currentRow()
        if selected_task >= 0:
            self.uncompleted_list.takeItem(selected_task)
            self.tasks["uncompleted"].pop(selected_task)
            self.save_tasks()
    
    # Function to remove a completed task from json
    def remove_completed_task(self):
        selected_task = self.completed_list.currentRow()
        if selected_task >= 0:
            self.completed_list.takeItem(selected_task)
            self.tasks["completed"].pop(selected_task)
            self.save_tasks()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())