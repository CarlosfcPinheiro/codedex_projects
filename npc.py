# Import library
import random

class Npc:
    phrases = ["Don't talk with me...", "Hello, welcome to the Vastin", "Leave me alone.", "Go out to the city!", "Take care and have a good adventure!"]
    
    def __init__(self, name:str) -> None:
        self.name = name.title()
    
    def talk(cls) -> None:
        return random.choice(cls.phrases)