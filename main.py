import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedLayout, QMessageBox
from view1 import View1
from view2 import View2

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Licznik zadań – zapisy")
        self.setGeometry(100, 100, 300, 200)

        self.stack = QStackedLayout()
        self.view1 = View1(self.load_slot)
        self.stack.addWidget(self.view1)

        layout = QVBoxLayout()
        layout.addLayout(self.stack)
        self.setLayout(layout)

    def load_slot(self, slot_number):
        self.view2 = View2(slot_number, self.return_to_menu)
        if self.stack.count() > 1:
            self.stack.removeWidget(self.stack.widget(1))
        self.stack.addWidget(self.view2)
        self.stack.setCurrentIndex(1)

    def return_to_menu(self):
        QMessageBox.information(self, "Zapisano", "Zapis został zapisany.")
        self.view1.refresh()
        self.stack.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
