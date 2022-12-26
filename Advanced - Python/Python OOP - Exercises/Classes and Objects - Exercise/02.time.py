class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = int(seconds)

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
        if self.minutes > Time.max_minutes:
            self.minutes = 0
            self.hours += 1
        if self.hours > Time.max_hours:
            self.hours = 0
        return self.get_time()


time = Time(10, 59, 59)
print(time.next_second())


# class Time:
#     max_hours = 23
#     max_minutes = 59
#     max_seconds = 59
#
#     def __init__(self, hours: int, minutes: int, seconds: int):
#         self.hours = int(hours)
#         self.minutes = int(minutes)
#         self.seconds = int(seconds)
#
#     def set_time(self, hours: int, minutes: int, seconds: int):
#         self.hours, self.minutes, self.seconds = int(hours), int(minutes), int(seconds)
#
#     def get_time(self):
#         return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
#
#     def next_second(self):
#         self.seconds += 1
#         if self.seconds > Time.max_seconds:
#             self.seconds = 0
#             self.minutes += 1
#             if self.minutes > Time.max_minutes:
#                 self.minutes = 0
#                 self.hours += 1
#                 if self.hours > Time.max_hours:
#                     self.hours = 0
#         return self.get_time()

