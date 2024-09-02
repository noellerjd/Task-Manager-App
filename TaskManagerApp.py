import sys
import os
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QLabel, QDateTimeEdit, QInputDialog, QListWidgetItem, QMessageBox, QSystemTrayIcon, QMenu, QHBoxLayout
from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtGui import QColor, QIcon
import datetime

# Function to handle the resource path, making it work both in development and in a PyInstaller bundle
def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

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

        # Task input layout
        self.task_input_layout = QHBoxLayout()
        
        # Input for new tasks
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter task description...")
        
        # Reminder date button and date input
        self.reminder_date_button = QPushButton("Set Reminder")
        self.reminder_date_edit = QDateTimeEdit(QDateTime.currentDateTime().addDays(1))
        self.reminder_date_edit.setCalendarPopup(True)
        self.reminder_date_edit.setDisplayFormat("MM-dd-yy h:mm ap")
        self.reminder_date_edit.setVisible(False)  # Hide the date edit initially

        # Add task button
        self.add_button = QPushButton("Add Task")
        
        # Add input fields and buttons to the task input layout
        self.task_input_layout.addWidget(self.input_field)
        self.task_input_layout.addWidget(self.reminder_date_button)
        self.task_input_layout.addWidget(self.reminder_date_edit)
        self.task_input_layout.addWidget(self.add_button)
        
        # Uncompleted tasks layout
        self.uncompleted_label = QLabel("Uncompleted Tasks")
        self.uncompleted_list = QListWidget()
        self.uncompleted_list.setDragDropMode(QListWidget.InternalMove)  # Enable drag-and-drop
        self.complete_button = QPushButton("Complete Task")
        self.remove_uncompleted_button = QPushButton("Remove Uncompleted Task")
        
        # Completed tasks layout
        self.completed_label = QLabel("Completed Tasks")
        self.completed_list = QListWidget()
        self.completed_list.setDragDropMode(QListWidget.InternalMove)  # Enable drag-and-drop
        self.remove_completed_button = QPushButton("Remove Completed Task")
        
        # Add widgets to the main layout
        self.layout.addLayout(self.task_input_layout)
        self.layout.addWidget(self.uncompleted_label)
        self.layout.addWidget(self.uncompleted_list)
        self.layout.addWidget(self.complete_button)
        self.layout.addWidget(self.remove_uncompleted_button)
        self.layout.addWidget(self.completed_label)
        self.layout.addWidget(self.completed_list)
        self.layout.addWidget(self.remove_completed_button)
        
        # Button functionality
        self.reminder_date_button.clicked.connect(self.toggle_reminder_date)
        self.add_button.clicked.connect(self.add_task)
        self.input_field.returnPressed.connect(self.add_task)
        self.complete_button.clicked.connect(self.complete_task)
        self.remove_uncompleted_button.clicked.connect(self.remove_uncompleted_task)
        self.remove_completed_button.clicked.connect(self.remove_completed_task)
        
        # Track when the items have been rearranged
        self.uncompleted_list.model().rowsMoved.connect(self.save_uncompleted_order)
        self.completed_list.model().rowsMoved.connect(self.save_completed_order)
        
        self.setLayout(self.layout)
        
        # Timer to check reminders every minute
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_dates)
        self.timer.start(60000)  # Check every 60 seconds
        
        self.load_tasks_into_ui()
        self.check_dates()  # Check reminders when the app starts
    
    def get_save_path(self, filename):
        """Get the path to save the file in the same directory as the executable."""
        if getattr(sys, 'frozen', False):  # Check if the app is running as a PyInstaller bundle
            base_path = sys._MEIPASS  # Use the temp directory created by PyInstaller
            base_path = os.path.dirname(sys.executable)  # Correct to use the directory of the executable
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, filename)
    
    # Function to load tasks.json
    def load_tasks(self):
        tasks_path = self.get_save_path("tasks.json")
        try:
            with open(tasks_path, "r") as file:
                self.tasks = json.load(file)
                print("Tasks loaded successfully:", self.tasks)  # Debugging line
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading tasks: {e}")  # Debugging line
            self.tasks = {"uncompleted": [], "completed": []}

    # Function to save tasks to json
    def save_tasks(self):
        tasks_path = self.get_save_path("tasks.json")
        try:
            with open(tasks_path, "w") as file:
                json.dump(self.tasks, file)
                print("Tasks saved successfully.")  # Debugging line
        except Exception as e:
            print(f"Error saving tasks: {e}")  # Debugging line

    # Function to load tasks into UI
    def load_tasks_into_ui(self):
        for task in self.tasks["uncompleted"]:
            if isinstance(task, str):  # Handle old tasks that are plain strings
                task = {"text": task, "reminder_date": None}
            item = QListWidgetItem(task["text"])
            item.setData(Qt.UserRole, task)
            self.uncompleted_list.addItem(item)
    
        for task in self.tasks["completed"]:
            if isinstance(task, str):  # Handle old tasks that are plain strings
                task = {"text": task, "reminder_date": None}
            item = QListWidgetItem(task["text"])
            item.setData(Qt.UserRole, task)
            self.completed_list.addItem(item)
    
        self.update_task_colors()
    
    # Function to add a task to the uncompleted section
    def add_task(self):
        task_text = self.input_field.text()
        reminder_date = self.reminder_date_edit.dateTime()

        # Check that the reminder date is not None and that it is equal to or after the current time
        if reminder_date.isValid() and reminder_date >= QDateTime.currentDateTime():
            reminder_date_str = reminder_date.toString("MM-dd-yy h:mm ap")
        else:
            reminder_date_str = None  # Set to None only if the reminder date is invalid or in the past

        if task_text:
            task = {
                "text": task_text,
                "reminder_date": reminder_date_str
            }
            self.tasks["uncompleted"].append(task)
            item = QListWidgetItem(task_text)
            item.setData(Qt.UserRole, task)
            self.uncompleted_list.addItem(item)
            self.input_field.clear()
            self.reminder_date_edit.setDateTime(QDateTime.currentDateTime().addDays(1))  # Reset reminder to tomorrow
            self.reminder_date_edit.setVisible(False)
            self.save_tasks()
            self.update_task_colors()


    
    # Function to toggle the visibility of the reminder date input
    def toggle_reminder_date(self):
        self.reminder_date_edit.setVisible(not self.reminder_date_edit.isVisible())
    
    # Function to move a task to the completed section, adds date and time of completion. 
    def complete_task(self):
        selected_task = self.uncompleted_list.currentRow()  # Get the index of the selected task
        if selected_task >= 0:  # Make sure a task is selected
            task_item = self.uncompleted_list.takeItem(selected_task)  # Remove the task from the uncompleted list
            
            # Add date and time of completion
            completion_time = QDateTime.currentDateTime().toString("MM-dd-yy h:mm ap") # Formats date and time ex 1/1/24 1:01 pm
            task_data = task_item.data(Qt.UserRole)
            completed_task_text = f"{task_data['text']} (Completed on: {completion_time})" # Adds date and time onto the task
            
            # Update and move the task to completed list
            task_data["text"] = completed_task_text
            self.tasks["uncompleted"].pop(selected_task)
            self.tasks["completed"].append(task_data)
            item = QListWidgetItem(completed_task_text)
            item.setData(Qt.UserRole, task_data)
            self.completed_list.addItem(item)
            self.save_tasks()
            self.update_task_colors()
    
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

    # Function to save the order of uncompleted tasks after rearranging
    def save_uncompleted_order(self):
        self.tasks["uncompleted"] = [self.uncompleted_list.item(i).data(Qt.UserRole) for i in range(self.uncompleted_list.count())]
        self.save_tasks()
    
    # Function to save the order of completed tasks after rearranging
    def save_completed_order(self):
        self.tasks["completed"] = [self.completed_list.item(i).data(Qt.UserRole) for i in range(self.completed_list.count())]
        self.save_tasks()

    # Function to update task colors based on reminders
    def update_task_colors(self):
        for i in range(self.uncompleted_list.count()):
            item = self.uncompleted_list.item(i)
            task_data = item.data(Qt.UserRole)
            if task_data["reminder_date"]:
                reminder_date = datetime.datetime.strptime(task_data["reminder_date"], "%m-%d-%y %I:%M %p")
                days_left = (reminder_date - datetime.datetime.now()).days
                if days_left < 0:
                    item.setBackground(QColor("red"))
                elif days_left == 0:
                    item.setBackground(QColor("orange"))
                else:
                    item.setBackground(QColor("white"))
    
    # Function to check dates for reminders
    def check_dates(self):
        now = datetime.datetime.now()
        
        for i in range(self.uncompleted_list.count()):
            item = self.uncompleted_list.item(i)
            task_data = item.data(Qt.UserRole)
            
            if task_data["reminder_date"]:
                # Parse the reminder date
                reminder_date = datetime.datetime.strptime(task_data["reminder_date"], "%m-%d-%y %I:%M %p")
                print(f"Current time: {now}")
                print(f"Reminder time: {reminder_date}")
                
                if now >= reminder_date and now.date() >= reminder_date.date():
                    print("Notification triggered!")  # For debugging, to ensure this line is reached
                    self.show_notification(task_data["text"], "Reminder!")
                    task_data["reminder_date"] = None  # Optional: Reset reminder to avoid repeated notifications
                    self.save_tasks()

        self.update_task_colors()



    # Function to show a desktop notification
    def show_notification(self, title, message):
        # try:
            # print("Attempting to show notification...")
        icon_path = resource_path('task_mananotification.png')
            # print(f"Icon path: {icon_path}") 
        tray_icon = QSystemTrayIcon(QIcon(icon_path), self)
        tray_icon.setVisible(True)
        tray_icon.showMessage(message, title, QSystemTrayIcon.Information)
            # print("Notification should be visible")
        # except Exception as e:
            # print(f"Failed to show notification: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
