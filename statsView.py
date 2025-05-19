from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
import json
import os


class StatsView(QWidget):
    def __init__(self, slot_number, on_back):
        super().__init__()
        self.slot_number = slot_number
        self.on_back = on_back

        self.layout = QVBoxLayout()

        self.title_label = QLabel(f"Statystyki dla slotu {slot_number}")
        self.layout.addWidget(self.title_label)

        self.stats_label = QLabel()
        self.layout.addWidget(self.stats_label)

        self.back_button = QPushButton("Powrót")
        self.back_button.clicked.connect(self.on_back_clicked)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

        self.load_stats()

    def load_stats(self):
        file = f"saves/data{self.slot_number}.json"
        if os.path.exists(file):
            with open(file, 'r') as f:
                data = json.load(f)
                if data.get("used", False):
                    text = (f"Zadanie: {data.get('task_number', '?')}\n"
                            f"Zrobione: {data.get('done', 0)}\n"
                            f"Zrobione z pomocą: {data.get('done_with_help', 0)}\n"
                            f"Łączny czas: {data.get('total_time', 0)} s\n"
                            f"Najkrótsze zadanie: {data.get('min_time', '?')} s (zadanie {data.get('min_task', '?')})\n"
                            f"Najdłuższe zadanie: {data.get('max_time', '?')} s (zadanie {data.get('max_task', '?')})"
                            )
                    self.stats_label.setText(text)
                else:
                    self.stats_label.setText("Brak danych statystycznych (slot nie używany).")
        else:
            self.stats_label.setText("Brak pliku zapisu.")

    def on_back_clicked(self):
        self.on_back()

    def update_slot(self, slot_number):
        self.slot_number = slot_number
        self.load_stats()