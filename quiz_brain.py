from html import unescape


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question = unescape(current_question.text)
        user_answer = input(f"Q.{self.question_number}: {question} (True/False)?\n")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"You got it wrong. The correct answer was {correct_answer}")
        print(f"You've answered {self.score}/{self.question_number} correctly.")
        print("\n")
