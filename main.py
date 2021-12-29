from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from logo import logo

print(logo)

question_bank = []
for n in range(0, len(question_data)):
    text = question_data[n]["question"]
    answer = question_data[n]["correct_answer"]
    question_object = Question(text, answer)
    question_bank.append(question_object)

our_quiz = QuizBrain(question_bank)

while our_quiz.still_has_questions():
    our_quiz.next_question()

print(f"""""You've completed the quiz.
Your final score was {our_quiz.score}/{our_quiz.question_number} or {round((our_quiz.score/our_quiz.question_number)*100)}%.""")
