from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot, Signal

from ui.base_qt_ui.ui_mainwindow import Ui_MainWindow
from ui.coordwidget import CoordWidget



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.counter_id: int = 0

        self.ui.add_button.clicked.connect(self.add_coordwidget)
        self.ui.clear_button.clicked.connect(self.clear_area)
    @Slot()
    def add_coordwidget(self):
        self.counter_id += 1
        coord_widget = CoordWidget(self.counter_id)
        self.ui.coordwidget_layout.addWidget(coord_widget)
        coord_widget.delete.connect(self.delete_coordwidget)

    @Slot()
    def clear_area(self):
        for _ in range(self.ui.coordwidget_layout.count()):
            item = self.ui.coordwidget_layout.takeAt(0)
            item.widget().deleteLater()

    @Slot(int)
    def delete_coordwidget(self, wid: int):
        print(f"Deleting widget with id: {wid}")
        widget = self.sender()
        print(f"Widget {widget}")
        self.ui.coordwidget_layout.removeWidget(widget)
        widget.deleteLater()
