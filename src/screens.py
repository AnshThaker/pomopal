from PyQt5 import QtWidgets, QtGui
from about_ui import Ui_about_window
from settings_ui import Ui_settings_window


class ScreenSwitcher:
    def __init__(self, main_ui_window, main_ui_instance):
        self.about_window = QtWidgets.QMainWindow()
        self.settings_window = QtWidgets.QMainWindow()
        self.about_ui = Ui_about_window()
        self.about_ui.setupUi(self.about_window)
        self.settings_ui = Ui_settings_window()
        self.settings_ui.setupUi(self.settings_window)
        self.main_window = main_ui_window
        self.main_ui = main_ui_instance
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.stacked_widget.addWidget(self.main_window)
        self.stacked_widget.addWidget(self.about_window)
        self.stacked_widget.addWidget(self.settings_window)
        self.stacked_widget.setFixedWidth(600)
        self.stacked_widget.setFixedHeight(300)
        self.stacked_widget.setWindowTitle('PomoPal v0.3')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("tomato.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stacked_widget.setWindowIcon(icon)
        self.main_ui.about_btn.clicked.connect(self.switch_to_about_ui)
        self.main_ui.settings_btn.clicked.connect(self.switch_to_settings_ui)
        self.about_ui.back_btn.clicked.connect(self.switch_to_main_ui_about)
        self.settings_ui.back_btn.clicked.connect(self.switch_to_main_ui_settings)
        self.stacked_widget.show()

    def switch_to_about_ui(self):
        self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() + 1)

    def switch_to_main_ui_about(self):
        self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() - 1)

    def switch_to_settings_ui(self):
        self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() + 2)

    def switch_to_main_ui_settings(self):
        self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() - 2)
