from PyQt5.QtWidgets import (QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QHBoxLayout, QWidget, QTextEdit, QApplication, QDateTimeEdit,
                             QDialog, QFormLayout, QMessageBox)
from PyQt5.QtCore import QDateTime
from task_manager import TaskManager
from task import Task
import datetime

class GUIApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.task_manager = TaskManager()
        self.init_ui()
###icon_path = "C:\Users\IM\PycharmProjects\TO-DO-LIST\logo.jpeg"
###window.setWindowIcon(QIcon(icon_path))
    def init_ui(self):
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 500, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.title_label_main = QLabel("Title:")
        self.layout.addWidget(self.title_label_main)

        self.title_entry = QLineEdit()
        self.layout.addWidget(self.title_entry)

        self.description_label = QLabel("Description:")
        self.layout.addWidget(self.description_label)

        self.description_entry = QLineEdit()
        self.layout.addWidget(self.description_entry)

        self.due_date_label = QLabel("Due Date:")
        self.layout.addWidget(self.due_date_label)

        self.due_date_entry = QDateTimeEdit()
        self.due_date_entry.setCalendarPopup(True)
        self.due_date_entry.setDateTime(QDateTime.currentDateTime())
        self.layout.addWidget(self.due_date_entry)

        self.button_layout = QHBoxLayout()

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.button_layout.addWidget(self.add_button)

        self.list_button = QPushButton("List Tasks")
        self.list_button.clicked.connect(self.open_list_tasks_window)
        self.button_layout.addWidget(self.list_button)

        self.remove_button = QPushButton("Remove Task")
        self.remove_button.clicked.connect(self.open_remove_task_window)
        self.button_layout.addWidget(self.remove_button)

        self.layout.addLayout(self.button_layout)

        self.message_box = QTextEdit()
        self.message_box.setReadOnly(True)
        self.layout.addWidget(self.message_box)

    def add_task(self):
        title = self.title_entry.text()
        description = self.description_entry.text()
        due_date = self.due_date_entry.dateTime().toPyDateTime()
        task = Task(title, description, due_date)
        self.task_manager.add_task(task)
        self.message_box.append("Task added: " + str(task))
        self.clear_entries()

    def open_list_tasks_window(self):
        self.list_tasks_window = TaskListWindow(self.task_manager)
        self.list_tasks_window.show()

    def open_remove_task_window(self):
        self.remove_task_window = TaskRemoveWindow(self.task_manager)
        self.remove_task_window.show()

    def clear_entries(self):
        self.title_entry.clear()
        self.description_entry.clear()
        self.due_date_entry.setDateTime(QDateTime.currentDateTime())

class TaskListWindow(QDialog):
    def __init__(self, task_manager):
        super().__init__()
        self.task_manager = task_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("List Tasks")
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()

        self.tasks_display = QTextEdit()
        self.tasks_display.setReadOnly(True)
        layout.addWidget(self.tasks_display)

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.list_tasks)
        layout.addWidget(self.refresh_button)

        self.setLayout(layout)
        self.list_tasks()

    def list_tasks(self):
        tasks = self.task_manager.list_tasks()
        tasks_str = "\n".join([str(task) for task in tasks])
        self.tasks_display.setText(tasks_str)

class TaskRemoveWindow(QDialog):
    def __init__(self, task_manager):
        super().__init__()
        self.task_manager = task_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Remove Task")
        self.setGeometry(100, 100, 400, 200)
        layout = QFormLayout()

        self.title_label = QLabel("Title of task to remove:")
        self.title_entry = QLineEdit()

        self.remove_button = QPushButton("Remove Task")
        self.remove_button.clicked.connect(self.remove_task)

        layout.addRow(self.title_label, self.title_entry)
        layout.addWidget(self.remove_button)

        self.setLayout(layout)

    def remove_task(self):
        title = self.title_entry.text()
        self.task_manager.remove_task(title)
        QMessageBox.information(self, "Info", f"Task removed: {title}")
        self.title_entry.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = GUIApp()
    window.show()
    app.exec_()
