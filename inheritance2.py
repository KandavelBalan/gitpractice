from intertance import dad

class son(dad):
    def factory(self):
        return "red"
    def house(self):
        return "blue"
d = son()
print(d.factory())