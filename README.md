# Task Manager App

Welcome to the Task Manager App! This application is designed to help you manage your tasks effectively. You can easily add, complete, and remove tasks, with completed tasks being stored along with the date and time of completion. Also now includes Windows 10/11 notifications for tasks that have a reminder date!

![image](https://github.com/user-attachments/assets/6b15b8ee-0a43-4afd-9112-107a402a8bec)

![image](https://github.com/user-attachments/assets/ba8163f6-3d9f-46fe-b434-49a973cef26b)


## Features

- Add Tasks: Quickly add new tasks to your to-do list.
- Complete Tasks: Mark tasks as completed and move them to the completed list with a timestamp.
- Remove Tasks: Easily remove tasks from both the uncompleted and completed lists.
- Persistent Storage: Your tasks are saved locally and reloaded when the app is reopened.

## Getting Started

### Prerequisites

- Windows Operating System
- Python 3.6 or higher (if you are running the Python script directly)
- No Python Knowledge Required if using the provided executable

## Installation and Setup

### Option 1: Using the Pre-built Executable (Recommended for Non-Technical Users)

#### 1.) Download the Executable:

- Go to the [Releases](https://github.com/noellerjd/Task-Manager-App/releases) section of this repository and download the latest version of the executable file `TaskManagerApp.exe`.

#### 2.) Place the Executable

- Move the downloaded `TaskManagerApp.exe` file to a location where you want to keep it!
- It's recommended to keep this application within a folder as this will create a json file to store the information between sessions.

#### 3.) Create a Desktop Shortcut (Recommended)

- Right-click on the `TaskManagerApp.exe` file, select Send to > Desktop named `TaskManagerApp - Shortcut`

#### 4.) Launch the application!

- Double-click the app or shortcut to launch into the Task Manager App!

### Option 2: Building the Executable for Yourself (For Developers or Advanced Users)

#### 1.) Clone the repository using Comman prompt, PowerShell etc:

- `git clone https://github.com/noellerjd/Task-Manager-App.git`

#### 2.) Install Python and PyInstaller:

- if you don't already have python installed, download and install it from [python.org](https://www.python.org/downloads/)
- Install `PyInstaller` using `pip`: `pip install pyinstaller`

#### 3.) Create the Executable:

- Run the following command to create the executable: `pyinstaller --onefile --windowed TaskManagerApp.py`.
- If using the .spec use this command instead: `pyinstaller TaskManagerApp.spec` or `pyinstaller --clean TaskManagerApp.spec` to ensure a clean packaging if changes were made to the .spec file
- This command will generate a dist/ folder containing the standalone executable (TaskManagerApp.exe) and a build/ folder with temporary build files. The .spec file will also be generated in your project directory.

#### 4.) Feel free to move the Executable or create a shortcut!

#### 5.) Double click the Executable to launch the Task Manager App

## Using the Task Manager App

#### Adding a Task:

Type your task into the input field and click the "Add Task" button. The task will appear in the uncompleted tasks list.

#### Completing a Task:

Select a task from the uncompleted tasks list and click the "Complete Task" button. The task will move to the completed tasks list with the date and time of completion.

#### Removing a Task:

You can remove a task from either the uncompleted or completed tasks list by selecting the task and clicking the "Remove Task" button.

## Uninstallation

To uninstall the Task Manager App:

- Simply delete the TaskManagerApp folder from your computer.

### Contact

If you encounter any issues or have questions, feel free to open an issue in the repository!
