class User:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.name = name
        self.age = age