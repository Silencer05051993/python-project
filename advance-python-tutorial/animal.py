class Animal(object):
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print("It's " + self.name)

    def run(self):
        print("runing...")
