from PyQt5.QtCore import QSettings


class Settings:
    def __init__(self):
        self.settings = QSettings('Ansh Thaker', 'PomoPal')
        try:
            self.pomodoro_time = self.str_to_int(self.settings.value('pomodoro_time'))
            self.short_break_time = self.str_to_int(self.settings.value('short_break_time'))
            self.long_break_time = self.str_to_int(self.settings.value('long_break_time'))
            self.auto_start_timer = self.str_to_bool(self.settings.value('auto_start_timer'))
            self.long_break_interval = self.str_to_int(self.settings.value('long_break_interval'))
            self.alarm = self.str_to_bool(self.settings.value('alarm'))
        except TypeError:
            if not self.settings.childKeys():
                self.settings.setValue('pomodoro_time', '25')
                self.settings.setValue('short_break_time', '5')
                self.settings.setValue('long_break_time', '15')
                self.settings.setValue('auto_start_timer', 'true')
                self.settings.setValue('long_break_interval', '4')
                self.settings.setValue('alarm', 'true')
                self.pomodoro_time = self.str_to_int(self.settings.value('pomodoro_time'))
                self.short_break_time = self.str_to_int(self.settings.value('short_break_time'))
                self.long_break_time = self.str_to_int(self.settings.value('long_break_time'))
                self.auto_start_timer = self.str_to_bool(self.settings.value('auto_start_timer'))
                self.long_break_interval = self.str_to_int(self.settings.value('long_break_interval'))
                self.alarm = self.str_to_bool(self.settings.value('alarm'))

    @staticmethod
    def str_to_bool(value):
        if type(value) is str:
            return True if value == 'true' else False
        elif value is None:
            return False
        else:
            return value

    @staticmethod
    def str_to_int(value):
        return int(value)
