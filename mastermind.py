from quantumrandom import randint
# from random import randint

class Mastermind_Game:
    def __init__(self):
        self.colours = ["orange", "green", "purple", "red", "blue", "cyan"]
        self.code = []

    def __create_code(self):
        for i in range(4):
            self.code.append(self.colours[int(randint(0, 5))])

    def game(self):
        self.__create_code()


if __name__ == "__main__":
    Mastermind_Game()
