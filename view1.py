import os
import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class View1(QWidget):
    def __init__(self, on_slot_selected):
        super().__init__()
        self.on_slot_selected = on_slot_selected
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.refresh()

    def refresh(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        self.layout.addWidget(QLabel("Wybierz slot zapisu:"))
        for i in range(1, 4):
            label = self.get_slot_label(i)
            btn = QPushButton(label)
            btn.clicked.connect(lambda _, slot=i: self.on_slot_selected(slot))
            self.layout.addWidget(btn)

    def get_slot_label(self, slot):
        file = f"saves/data{slot}.json"
        if os.path.exists(file):
            with open(file, 'r') as f:
                data = json.load(f)
                if data.get('used', False):
                    task = data.get('task_number', 1)
                    return f"Slot {slot} (Zadanie {task})"
                else:
                    return f"Slot {slot} (nowy)"

