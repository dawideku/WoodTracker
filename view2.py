import json
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer

class View2(QWidget):
    def __init__(self, slot_number, on_finish_callback):
        super().__init__()
        self.slot_number = slot_number
        self.on_finish = on_finish_callback
        self.data_file = f"saves/data{slot_number}.json"

        self.load_data()

        self.layout = QVBoxLayout()
        self.task_label = QLabel(f"Zadanie {self.task_number}")
        self.time_label = QLabel("Czas: 0 s")

        self.done_button = QPushButton("Zrobione")
        self.done_button.clicked.connect(self.mark_done)

        self.help_button = QPushButton("Zrobione z pomocą")
        self.help_button.clicked.connect(self.mark_done_with_help)

        self.finish_button = QPushButton("Zakończ")
        self.finish_button.clicked.connect(self.finish)

        self.layout.addWidget(self.task_label)
        self.layout.addWidget(self.time_label)
        self.layout.addWidget(self.done_button)
        self.layout.addWidget(self.help_button)
        self.layout.addWidget(self.finish_button)
        self.setLayout(self.layout)

        # Timer
        self.task_seconds = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # co sekundę

    def update_timer(self):
        self.task_seconds += 1
        self.time_label.setText(f"Czas: {self.task_seconds} s")

    def mark_done(self):
        self.done += 1
        self.advance_task()

    def mark_done_with_help(self):
        self.done_with_help += 1
        self.advance_task()

    def advance_task(self):
        self.check_task_time()
        self.total_time += self.task_seconds
        self.task_number += 1
        self.task_seconds = 0
        self.task_label.setText(f"Zadanie {self.task_number}")
        self.time_label.setText(f"Czas: 0 s")

    def check_task_time(self):
        if self.task_seconds < self.min_time:
            self.min_time = self.task_seconds
            self.min_task = self.task_number
        elif self.task_seconds > self.max_time:
            self.max_time = self.task_seconds
            self.max_task = self.task_number

    def finish(self):
        self.total_time += self.task_seconds
        self.save_data()
        self.timer.stop()
        self.on_finish()

    def save_data(self):
        data = {
            'used': True,
            'task_number': self.task_number,
            'done': self.done,
            'done_with_help': self.done_with_help,
            'total_time': self.total_time,
            'min_time': self.min_time,
            'max_time': self.max_time,
            'min_task': self.min_task,
            'max_task': self.max_task,
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                if data.get("used", False):
                    self.task_number = data.get('task_number', 1)
                    self.done = data.get('done', 0)
                    self.done_with_help = data.get('done_with_help', 0)
                    self.total_time = data.get('total_time', 0)
                    self.min_time = data.get('min_time', 10000)
                    self.max_time = data.get('max_time', 0)
                    self.min_task = data.get('min_task', 0)
                    self.max_task = data.get('max_task', 0)
                    return
        # nowy zapis
        self.task_number = 1
        self.done = 0
        self.done_with_help = 0
        self.total_time = 0
        self.min_time = 10000
        self.max_time = 0
        self.min_task = 0
        self.max_task = 0
