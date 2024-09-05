import random


class fruit():
    def __init__(self):
        self.fruit = {'apple': 'red','banana': 'yellow', 'orange': 'orange', 'grapes': 'purple'}
    def quiz(self):
        while (True):
            fruit,color = random.choice(list(self.fruit.item()))
            print("what is the color of {}".format(fruit))
            user_answer = input()
            if (user_answer.lower()==color):
                print("Correct answer")
            else:
                print("Incorrect")
            option = int(input("Enter 0 if u want to play again otherwise enter 1: "))
            if (option):
                break

print("welcome to the fruit quiz")
sq = fruit()
sq.quiz()
