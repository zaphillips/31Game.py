class Card():
    def __init__(self, suite: str, name: str):
        self.suite = suite
        self.name = name
        self.value = 0
        self.__setValue()

    def __setValue(self):
        if self.name in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            self.value = int(self.name)
        elif self.name in ['J', 'Q', 'K']:
            self.value = 10
        elif self.name == 'A':
            self.value = 11

    def show(self):
        print(self.suite + " " + self.name)

    def returnValue(self)-> int:
        return self.value