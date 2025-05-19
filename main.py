import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedLayout, QMessageBox
from view1 import View1
from view2 import View2
from viewIntermediate import ViewIntermediate
from statsView import StatsView

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Licznik zadań – zapisy")
        self.setGeometry(100, 100, 300, 200)

        self.stack = QStackedLayout()

        self.view1 = View1(self.open_intermediate_view)
        self.view_intermediate = None
        self.stats_view = None
        self.view2 = None

        self.stack.addWidget(self.view1)

        layout = QVBoxLayout()
        layout.addLayout(self.stack)
        self.setLayout(layout)

    def open_intermediate_view(self, slot_number):
        if self.view_intermediate is None:
            self.view_intermediate = ViewIntermediate(
                slot_number,
                on_start_learning=self.load_slot,
                on_show_stats=self.open_stats_view,
                on_back=self.return_to_menu_from_intermediate
            )
            self.stack.addWidget(self.view_intermediate)
        else:
            self.view_intermediate.update_slot(slot_number)
        self.stack.setCurrentWidget(self.view_intermediate)

    def open_stats_view(self, slot_number):
        if self.stats_view is None:
            self.stats_view = StatsView(slot_number, on_back=self.back_to_intermediate_from_stats)
            self.stack.addWidget(self.stats_view)
        else:
            self.stats_view.update_slot(slot_number)
        self.stack.setCurrentWidget(self.stats_view)

    def load_slot(self, slot_number):
        if self.view2 is None:
            self.view2 = View2(slot_number, self.return_to_menu)
            self.stack.addWidget(self.view2)
        else:
            self.view2.change_slot(slot_number)
        self.stack.setCurrentWidget(self.view2)

    def back_to_intermediate_from_stats(self):
        self.stack.setCurrentWidget(self.view_intermediate)

    def return_to_menu_from_intermediate(self):
        self.view1.refresh()
        self.stack.setCurrentWidget(self.view1)

    def return_to_menu(self):
        self.view1.refresh()
        self.stack.setCurrentWidget(self.view1)


def load_stylesheet(path):
    with open(path, "r") as f:
        return f.read()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet("style.qss"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
