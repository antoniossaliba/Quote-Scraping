from quiz_maker import QuizMaker
from scraper import Scraper
from pprint import pprint

scraper = Scraper(list(), list())
scraper.fetch_authors_quotes()

quiz = QuizMaker(scraper.quotes, scraper.authors)

quiz.play_quiz()