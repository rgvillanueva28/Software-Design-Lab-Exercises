
from doctor import Doctor

class main:

    def main(self  ):
        """Handles the interaction between user and the class doctor."""
        print("Good morning, I hope you are well today.")
        print("What can I do for you?")
        while True:
            sentence = input("\n>> ")
            if sentence.upper() == "QUIT":
                print("Have a nice day!")
                break
            print(Doctor().reply(sentence))

#The entry point for program execution
if __name__ == "__main__":
    main().main()