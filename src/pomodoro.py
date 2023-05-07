import time
import threading
from settings import Settings
from playsound import playsound
from notifier import Notifier

settings = Settings()
notifier = Notifier()


class Pomodoro:
    def __init__(self, ui_instance):
        self.ui = ui_instance
        self.pomodoros = 0
        self.skipped = False
        self.stopped = False
        self.running = False
        self.paused = False
        self.lock = threading.Lock()

        self.ui.start_btn.clicked.connect(self.start_timer_thread)
        self.ui.skip_btn.clicked.connect(self.skip_timer)
        self.ui.reset_btn.clicked.connect(self.reset_timer)
        self.ui.pause_btn.clicked.connect(self.pause_resume_timer)

    def start_timer_thread(self):
        if not self.running:
            timer_thread = threading.Thread(target=self.start_timer)
            timer_thread.start()
            self.running = True

    def start_timer(self):
        self.stopped = False
        self.skipped = False
        timer_id = self.ui.tabs.currentIndex() + 1

        if timer_id == 1:
            full_secs = 60 * int(settings.pomodoro_time)
            while full_secs > 0 and not self.stopped:
                if not self.paused:
                    mins, secs = divmod(full_secs, 60)
                    self.ui.pomo_timer_label.setText(f'{mins:02d}:{secs:02d}')
                    time.sleep(1)
                    full_secs -= 1
                else:
                    continue
            if not self.stopped and not self.skipped:
                self.ui.pomo_timer_label.setText('00:00')
                full_secs = 60 * int(settings.pomodoro_time)
                mins, secs = divmod(full_secs, 60)
                self.ui.pomo_timer_label.setText(f'{mins:02d}:{secs:02d}')
            if not self.stopped or self.skipped:
                self.pomodoros += 1
                self.ui.pomo_counter_label.setText(f'Pomodoros: {self.pomodoros}')
                settings.settings.sync()
                settings.alarm = settings.str_to_bool(settings.settings.value('alarm'))
                if not self.skipped:
                    settings.settings.sync()
                    settings.long_break_interval = settings.str_to_int(settings.settings.value('long_break_interval'))
                    if self.pomodoros % settings.long_break_interval != 0:
                        notifier.notify_pomodoro_done_short()
                    else:
                        notifier.notify_pomodoro_done_long()
                    if settings.alarm:
                        playsound('alarm.wav')
                settings.settings.sync()
                settings.auto_start_timer = settings.str_to_bool(settings.settings.value('auto_start_timer'))
                settings.long_break_interval = settings.str_to_int(settings.settings.value('long_break_interval'))
                if settings.auto_start_timer:
                    if self.pomodoros % settings.long_break_interval == 0:
                        self.ui.tabs.setCurrentIndex(2)
                    else:
                        self.ui.tabs.setCurrentIndex(1)
                    self.start_timer()
                else:
                    self.running = False
        elif timer_id == 2:
            full_secs = 60 * int(settings.short_break_time)
            while full_secs > 0 and not self.stopped:
                if not self.paused:
                    mins, secs = divmod(full_secs, 60)
                    self.ui.short_break_label.setText(f'{mins:02d}:{secs:02d}')
                    time.sleep(1)
                    full_secs -= 1
                else:
                    continue
            if not self.stopped and not self.skipped:
                self.ui.short_break_label.setText('00:00')
                full_secs = 60 * int(settings.short_break_time)
                mins, secs = divmod(full_secs, 60)
                self.ui.short_break_label.setText(f'{mins:02d}:{secs:02d}')
            if not self.stopped or self.skipped:
                settings.settings.sync()
                settings.alarm = settings.str_to_bool(settings.settings.value('alarm'))
                if not self.skipped:
                    notifier.notify_short_break_done()
                    if settings.alarm:
                        playsound('alarm.wav')
                settings.settings.sync()
                settings.auto_start_timer = settings.str_to_bool(settings.settings.value('auto_start_timer'))
                if settings.auto_start_timer:
                    self.ui.tabs.setCurrentIndex(0)
                    self.start_timer()
                else:
                    self.running = False
        elif timer_id == 3:
            full_secs = 60 * int(settings.long_break_time)
            while full_secs > 0 and not self.stopped:
                if not self.paused:
                    mins, secs = divmod(full_secs, 60)
                    self.ui.long_break_label.setText(f'{mins:02d}:{secs:02d}')
                    time.sleep(1)
                    full_secs -= 1
                else:
                    continue
            if not self.stopped and not self.skipped:
                self.ui.long_break_label.setText('00:00')
                full_secs = 60 * int(settings.long_break_time)
                mins, secs = divmod(full_secs, 60)
                self.ui.long_break_label.setText(f'{mins:02d}:{secs:02d}')
            if not self.stopped or self.skipped:
                settings.settings.sync()
                settings.alarm = settings.str_to_bool(settings.settings.value('alarm'))
                if not self.skipped:
                    notifier.notify_long_break_done()
                    if settings.alarm:
                        playsound('alarm.wav')
                settings.settings.sync()
                settings.auto_start_timer = settings.str_to_bool(settings.settings.value('auto_start_timer'))
                if settings.auto_start_timer:
                    self.ui.tabs.setCurrentIndex(0)
                    self.start_timer()
                else:
                    self.running = False
        else:
            print("Invalid Timer ID")

    def reset_timer(self):
        settings.settings.sync()
        settings.pomodoro_time = settings.str_to_int(settings.settings.value('pomodoro_time'))
        settings.short_break_time = settings.str_to_int(settings.settings.value('short_break_time'))
        settings.long_break_time = settings.str_to_int(settings.settings.value('long_break_time'))
        self.stopped = True
        self.skipped = False
        self.paused = False
        self.running = False
        self.ui.pause_btn.setText('Pause')
        self.pomodoros = 0
        full_secs_pomo = 60 * int(settings.pomodoro_time)
        mins_pomo, secs_pomo = divmod(full_secs_pomo, 60)
        self.ui.pomo_timer_label.setText(f'{mins_pomo:02d}:{secs_pomo:02d}')
        full_secs_short = 60 * int(settings.short_break_time)
        mins_short, secs_short = divmod(full_secs_short, 60)
        self.ui.short_break_label.setText(f'{mins_short:02d}:{secs_short:02d}')
        full_secs_long = 60 * int(settings.long_break_time)
        mins_long, secs_long = divmod(full_secs_long, 60)
        self.ui.long_break_label.setText(f'{mins_long:02d}:{secs_long:02d}')
        self.ui.pomo_counter_label.setText('Pomodoros: 0')

    def skip_timer(self):
        current_tab = self.ui.tabs.currentIndex()
        if current_tab == 0:
            self.ui.pomo_timer_label.setText('00:00')
            full_secs = 60 * int(settings.pomodoro_time)
            mins, secs = divmod(full_secs, 60)
            self.ui.pomo_timer_label.setText(f'{mins:02d}:{secs:02d}')
        elif current_tab == 1:
            self.ui.short_break_label.setText('00:00')
            full_secs = 60 * int(settings.short_break_time)
            mins, secs = divmod(full_secs, 60)
            self.ui.short_break_label.setText(f'{mins:02d}:{secs:02d}')
        elif current_tab == 2:
            self.ui.long_break_label.setText('00:00')
            full_secs = 60 * int(settings.long_break_time)
            mins, secs = divmod(full_secs, 60)
            self.ui.long_break_label.setText(f'{mins:02d}:{secs:02d}')

        self.stopped = True
        self.skipped = True
        self.paused = False
        self.ui.pause_btn.setText('Pause')

    def pause_resume_timer(self):
        if not self.paused and self.running:
            self.paused = True
            self.ui.pause_btn.setText('Resume')
        elif self.paused and self.running:
            self.paused = False
            self.ui.pause_btn.setText('Pause')
