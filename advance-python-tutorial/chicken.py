from animal import Animal


class Chickend(Animal):
    def __init__(self, name, age, height):
        super().__init__(name)
        self.age = age
        self.height = height

    def show_info(self):
        print("It's " + self.name)
        print(" age " + str(self.age))
        print(" height " + str(self.height))


if __name__ == '__main__':
    chickend = Chickend("Kentucky", 2, 20)
    chickend.show_info()
    chickend.run()
