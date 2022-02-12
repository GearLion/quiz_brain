from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
LABEL_FONT = ("Arial", 10)


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window
        self.window = Tk()
        self.window.minsize(width=370, height=460)
        self.window.title("QuizBrain")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score
        self.score_label = Label()
        self.score = 0
        self.score_label.grid(column=0, row=0)
        self.score_label.config(text=f"Score: {self.score}",
                                font=LABEL_FONT, bg=THEME_COLOR, fg="white", justify=RIGHT)

        # Canvas
        self.settings_canvas = Canvas(width=300, height=250, bg=THEME_COLOR)

        self.question_canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.question_canvas.create_text(150, 125, width=280, text="This is text",
                                                              fill=THEME_COLOR, font=FONT)
        self.question_canvas.grid(column=0, row=1, columnspan=3, padx=10, pady=20)

        # Buttons
        self.true_button = Button()
        self.true_button.grid(column=0, row=2)
        checkmark = PhotoImage(file="images/true.png")
        self.true_button.config(image=checkmark, highlightthickness=0, command=self.check_answer_true)

        self.false_button = Button()
        self.false_button.grid(column=2, row=2)
        crossmark = PhotoImage(file="images/false.png")
        self.false_button.config(image=crossmark, highlightthickness=0, command=self.check_answer_false)

        self.settings_button = Button(command=self.go_settings)
        self.settings_button.grid(column=2, row=0)
        self.settings_button.config(bg=THEME_COLOR, fg="white", text="Settings", font=LABEL_FONT, highlightthickness=0)

        self.return_button = Button(self.settings_canvas, text="Return", command=self.go_home)
        self.return_button.grid(column=1, row=0)

        # Function at Start
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.question_canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def check_answer_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def go_settings(self):
        self.question_canvas.grid_forget()
        self.settings_canvas.grid(column=0, row=1, columnspan=3, padx=10, pady=20)
        self.true_button.grid_forget()
        self.false_button.grid_forget()
        self.score_label.grid_forget()
        self.settings_button.grid_forget()

    def go_home(self):
        self.settings_canvas.grid_forget()
        self.question_canvas.grid(column=0, row=1, columnspan=3, padx=10, pady=20)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=2, row=2)
        self.score_label.grid(column=0, row=0)
        self.settings_button.grid(column=2, row=0)
