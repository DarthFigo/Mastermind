from random import randint

class MastermindGame:
    def __init__(self):
        self.colours = ["orange", "green", "purple", "red", "blue", "cyan"]
        self.code = []

        self.game()

    def __create_code(self):
        for i in range(4):
            self.code.append(self.colours[int(randint(0, 3))])

    def game(self):
        self.__create_code()

        count = 11
        for i in range(10):
            count -= 1
            print("Tries left: %s\n" % (count))

            guess_c1 = input("Guess for color 1: ")
            guess_c2 = input("Guess for color 2: ")
            guess_c3 = input("Guess for color 3: ")
            guess_c4 = input("Guess for color 4: ")
            print("")

            guesses = [guess_c1, guess_c2, guess_c3, guess_c4]

            rpcounter = 0
            wpcounter = 0

            for i in range(4):
                if guesses[i] == self.code[i]:
                    rpcounter += 1
                elif guesses[i] in self.code:
                    wpcounter += 1

            if rpcounter >= 4:
                print("ya won")
                exit(0)
            else:
                print("Red pegs: %s, white pegs: %s\n\n" % (rpcounter, wpcounter))

        print("ya failed, noob")
        exit(0)


if __name__ == "__main__":
    MastermindGame()
