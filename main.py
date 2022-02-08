from question_model import Question
from data import question_cooker, set_category, set_difficulty
from quiz_brain import QuizBrain
from logo import logo


print(logo)

input("Please press any button to list your category questions:\n")
question_dict = question_cooker(cat=set_category(), difficulty=set_difficulty())

question_bank = []
for n in range(0, len(question_dict)):
    text = question_dict[n]["question"]
    answer = question_dict[n]["correct_answer"]
    question_object = Question(text, answer)
    question_bank.append(question_object)

our_quiz = QuizBrain(question_bank)


while our_quiz.still_has_questions():
    our_quiz.next_question()

print(f"You've completed the quiz. "
      f"Your final score was {our_quiz.score}/{our_quiz.question_number} or "
      f"{round((our_quiz.score/our_quiz.question_number)*100)}%.")
