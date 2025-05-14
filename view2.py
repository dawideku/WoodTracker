import json
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class View2(QWidget):
    def __init__(self, slot_number, on_finish_callback):
        super().__init__()
        self.slot_number = slot_number
        self.on_finish = on_finish_callback
        self.data_file = f"saves/data{slot_number}.json"

        self.task_number = self.load_task_number()

        self.layout = QVBoxLayout()
        self.task_label = QLabel(f"Zadanie {self.task_number}")

        self.next_button = QPushButton("Następne zadanie")
        self.next_button.clicked.connect(self.next_task)

        self.finish_button = QPushButton("Zakończ")
        self.finish_button.clicked.connect(self.finish)

        self.layout.addWidget(self.task_label)
        self.layout.addWidget(self.next_button)
        self.layout.addWidget(self.finish_button)
        self.setLayout(self.layout)

    def next_task(self):
        self.task_number += 1
        self.task_label.setText(f"Zadanie {self.task_number}")

    def finish(self):
        self.save_task_number()
        self.on_finish()

    def save_task_number(self):
        data = {
            'used': True,
            'task_number': self.task_number
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f)

    def load_task_number(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                if data.get("used", False):
                    return data.get('task_number', 1)
        return 1
