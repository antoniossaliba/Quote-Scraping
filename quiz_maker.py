import random as rnd


class QuizMaker:

    def __init__(self, quotes, authors):
        self.quotes = quotes
        self.authors = authors

    def generate_quote(self):
        return [self.quotes[rnd.randint(0, len(self.quotes) - 1)],
                self.authors[rnd.randint(0, len(self.authors) - 1)]]

    def play_quiz(self):
        got_answer = False
        rnd_int = rnd.randint(0, len(self.quotes) - 1)
        random_quote = self.quotes[rnd_int]
        random_author = self.authors[rnd_int]
        print(f"Random generated quote is: {random_quote}\n")
        while not got_answer:
            user_answer = input("Who wrote this quote? ")
            if user_answer.strip().lower() != random_author.strip().lower():
                print(f"Nah. Not {user_answer}. Try again!\n")
            else:
                print(f"YEAH. {user_answer} wrote this. Did you know?\n")
                got_answer = True
        return
