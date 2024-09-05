class flashcards:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'

flash = []
while(True):
    word =input("Enter your word: " )
    meaning =input("Enter the meaning of the word: " )
    flash.append(flashcards(word,meaning))
    option = int(input("Enter 0 if u want to add another flashcard otherwise add 1: " ))
    if(option):
        break

print("Your flashcard")
for i in flash:
    print(i)