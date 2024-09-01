# To-Do List App

## A simple to-do list application built with Python and PyQt5. This app allows users to manage their tasks with features to add, complete, and remove tasks. Completed tasks are stored with a timestamp.

# Features

Add Tasks: Easily add new tasks to your to-do list.

Complete Tasks: Mark tasks as completed and move them to the completed list with a timestamp.

Remove Tasks: Remove tasks from both the uncompleted and completed lists.

Persistent Storage: Tasks are saved locally and reloaded when the app is reopened.

# Requirements

Windows Operating System

No prior Python knowledge is needed if you're using the executable file. If you're running the script directly, you'll need:

- Python 3.6+ installed on your system

- Required Python packages: PyQt5

# Getting Started

## Option 1: Using the Executable File (Recommended for Non-Technical Users)

Download the Executable:

Download the executable file ToDoApp.exe from the releases section (link to your release, if applicable).
Run the Application:

Double-click the ToDoApp.exe file to launch the application.
Using the App:

You can now start adding, completing, and removing tasks using the simple user interface.
Option 2: Running the Python Script (For Developers or Advanced Users)
Install Python:

Download and install Python from python.org.
Clone the Repository:

Open a terminal or command prompt and run:
bash
Copy code
git clone https://github.com/yourusername/todo-app-py.git
Navigate to the project directory:
bash
Copy code
cd todo-app-py
Set Up a Virtual Environment (Optional but Recommended):

Create a virtual environment to keep dependencies isolated:
bash
Copy code
python -m venv venv
Activate the virtual environment:
On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install Dependencies:

Install the required Python packages:
bash
Copy code
pip install -r requirements.txt
Run the Application:

Start the application by running:
bash
Copy code
python todo_app.py
Option 3: Creating Your Own Executable with PyInstaller
Install PyInstaller:

If you prefer to create your own executable, install PyInstaller:
bash
Copy code
pip install pyinstaller
Create the Executable:

Generate an executable using PyInstaller:
bash
Copy code
pyinstaller --onefile --windowed todo_app.py
Find the Executable:

The executable will be located in the dist directory. You can now run the app by double-clicking the todo_app.exe file in the dist folder.
Troubleshooting
If the app doesn't launch: Make sure that all the necessary files are in the same directory as the executable.
Encountered an error? Run the app from the command prompt to see error messages that might help with debugging.
Contributing
Feel free to submit issues or pull requests to help improve the app. Contributions are welcome!

![image](https://github.com/user-attachments/assets/0ce9e274-b79b-4443-baf4-14529567f107)

This app will store information within local memory as a json file for easy access to old information.
