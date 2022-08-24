class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        message = ""
        if self.bullets > 0:
            self.bullets -= 1
            message = "shooting..."
        elif self.bullets == 0:
            message = "no bullets left"
        return message

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"
