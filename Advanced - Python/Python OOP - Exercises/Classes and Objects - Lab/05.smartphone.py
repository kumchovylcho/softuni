class Smartphone:

    def __init__(self, memory: int):
        self.memory = int(memory)
        self.apps = []
        self.is_on = False

    def power(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def install(self, app, app_memory: int):
        if self.memory >= app_memory and self.is_on:
            self.memory -= int(app_memory)
            self.apps.append(app)
            return f"Installing {app}"
        elif self.memory >= app_memory and not self.is_on:
            return f"Turn on your phone to install {app}"
        return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
