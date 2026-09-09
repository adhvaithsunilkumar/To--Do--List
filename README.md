# To-Do List / Task Manager

**Adhvaith Sunilkumar**

A simple and user-friendly **To-Do List / Task Manager** developed using **Python, Object-Oriented Programming (OOP), and Tkinter GUI**.

The application helps users manage their daily tasks by allowing them to add, view, complete, and delete tasks through a graphical interface.

## Features

- **Add a Task** – Add new tasks to the list.
- **View Tasks** – Display all added tasks.
- **Mark as Completed** – Change a task's status from Pending to Completed.
- **Delete a Task** – Remove a selected task from the list.
- **Simple GUI** – Easy-to-use graphical interface using Tkinter.
- **Input Validation** – Prevents adding empty tasks and alerts the user when no task is selected.

## Technologies Used

- **Python 3**
- **Tkinter**
- **Object-Oriented Programming (OOP)**

## Project Structure

```text
To-Do-List/
│
├── todo.py
└── README.md
```

## OOP Structure

The project is divided into three main classes:

### `Task`

Responsible for storing individual task information.

- Task name
- Completion status
- Marking a task as completed

### `TaskManager`

Responsible for managing the collection of tasks.

- Add tasks
- Complete tasks
- Delete tasks

### `TaskApp`

Responsible for the graphical user interface.

- Creates the application window
- Displays the task list
- Handles buttons and user interaction

## How to Run

### 1. Install Python

Make sure **Python 3** is installed on your computer.

You can check by running:

```bash
python --version
```

### 2. Download or Clone the Repository

```bash
git clone <your-repository-link>
```

Then move into the project folder:

```bash
cd To-Do-List
```

### 3. Run the Program

```bash
python todo.py
```

The To-Do List GUI will open automatically.

## How to Use

1. Enter a task in the text box.
2. Click **Add Task**.
3. Select a task from the list.
4. Click **Mark as Completed** to complete it.
5. Click **Delete Task** to remove it.

## 📸 Application Preview

_Add a screenshot of your application here._

```text
+---------------------------------------+
|              TO-DO LIST               |
|                                       |
|  [ Enter your task                 ]  |
|                                       |
|           [ Add Task ]                |
|                                       |
|  ○ Complete Python Assignment        |
|  ○ Study Java                         |
|  ✓ Submit Project - Completed        |
|                                       |
|      [ Mark as Completed ]            |
|                                       |
|          [ Delete Task ]              |
+---------------------------------------+
```

## Project Objective

The main objective of this project is to demonstrate the practical use of **Object-Oriented Programming in Python** while developing a simple graphical application.

It provides hands-on experience with:

- Classes and objects
- Methods
- Encapsulation
- Lists
- Event-driven programming
- Tkinter GUI development
- Basic input validation

## Future Improvements

Possible improvements include:

- Save tasks permanently using a file or database
- Add due dates
- Add task reminders
- Add task search and filtering
- Add an option to edit tasks
- Add dark mode
- Add task statistics

## Author

**Adhvaith Sunilkumar**

---

⭐ If you found this project useful, consider giving it a star!
