from plyer import notification
from random import choice


class Notifier:
    def __init__(self):
        self.notifier = notification
        self.app_name = 'PomoPal'
        self.app_icon = 'notification_icon.ico'
        self.pomodoro_done_short_messages = [
            "Take a rest and grab some water! 💧",
            "Stand up and stretch a bit! 🧘🏽‍♀️",
            "Get some fresh air! 🪟",
            "Relax a bit! 🛏️"
        ]
        self.pomodoro_done_long_messages = [
            "It's time to rest, but don't fall asleep! 😴",
            "Rest a bit, you deserve it! 😀",
            "Maybe grab a healthy snack? 🍎",
            "Listen to some relaxing music! 🎵",
            "Watch some YouTube videos and relax! 📺",
            "Maybe you can play a few rounds of your favourite video game! 🎮 (but not too much 😉)"
        ]
        self.short_break_done_messages = [
            "Get back to work, you've got this! 👍🏽",
            "It's time to work, I know you can do it! 🧠",
            "You've got this, get back to work now! 📚",
            "It's not time to give up now! 😤",
            "Time to continue! ⌚"
        ]
        self.long_break_done_messages = [
            "Enough rest, go back to work! 💻",
            "You can do it, just keep trying! 💪🏽",
            "You've got this, stay focused and keep working! 🔥",
            "That work isn't going to finish itself, so continue! 🤓",
            "I'll give you 5 seconds to start, or your computer will explode! 💥"
        ]

    def notify_pomodoro_done_short(self):
        self.notifier.notify(
            title="It's time for a short break!",
            message=choice(self.pomodoro_done_short_messages),
            app_name=self.app_name,
            app_icon=self.app_icon,
            timeout=5
        )

    def notify_pomodoro_done_long(self):
        self.notifier.notify(
            title="It's time for a long break!",
            message=choice(self.pomodoro_done_long_messages),
            app_name=self.app_name,
            app_icon=self.app_icon,
            timeout=5
        )

    def notify_short_break_done(self):
        self.notifier.notify(
            title="Short break finished!",
            message=choice(self.short_break_done_messages),
            app_name=self.app_name,
            app_icon=self.app_icon,
            timeout=5
        )

    def notify_long_break_done(self):
        self.notifier.notify(
            title="Long break finished!",
            message=choice(self.long_break_done_messages),
            app_name=self.app_name,
            app_icon=self.app_icon,
            timeout=5
        )
