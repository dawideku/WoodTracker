from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
import json
import os


class ViewIntermediate(QWidget):
    def __init__(self, slot_number, on_start_learning, on_show_stats, on_back):
        super().__init__()
        self.slot_number = slot_number
        self.on_start_learning = on_start_learning
        self.on_show_stats = on_show_stats
        self.on_back = on_back

        self.layout = QVBoxLayout()

        self.info_label = QLabel(f"Wybrano slot {slot_number}")
        self.layout.addWidget(self.info_label)

        self.start_button = QPushButton("Rozpocznij naukę")
        self.start_button.clicked.connect(self.on_start_learning_clicked)
        self.layout.addWidget(self.start_button)

        self.stats_button = QPushButton("Pokaż statystyki")
        self.stats_button.clicked.connect(self.on_show_stats_clicked)
        self.layout.addWidget(self.stats_button)

        self.back_button = QPushButton("Powrót")
        self.back_button.clicked.connect(self.on_back_clicked)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def update_slot(self, slot_number):
        self.slot_number = slot_number
        self.info_label.setText(f"Wybrano slot {slot_number}")

    def on_start_learning_clicked(self):
        self.on_start_learning(self.slot_number)

    def on_show_stats_clicked(self):
        self.on_show_stats(self.slot_number)

    def on_back_clicked(self):
        self.on_back()
