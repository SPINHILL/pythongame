class Invader:
    def __init__(self, name, invader_type, health, speed):
        self.name = name
        self.invader_type = invader_type
        self.health = health
        self.speed = speed

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Type: {self.invader_type}")
        print(f"Health: {self.health}")
        print(f"Speed: {self.speed}")