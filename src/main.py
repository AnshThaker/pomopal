from main_ui import Ui_main_window, QtWidgets, QtCore
from pomodoro import Pomodoro
from screens import ScreenSwitcher
from settings import Settings

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    configure_settings = Settings()
    screen_switcher = ScreenSwitcher(main_window, ui)
    pomodoro = Pomodoro(ui)
    main_window.show()
    sys.exit(app.exec_())
