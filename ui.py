import time
from tkinter import *
from data import question_data
import html

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
class QuizInterface:
    def true_answer(self):
       self.give_feedback(self.quiz.check_answer(user_answer="True"))


    def false_answer(self):
        self.give_feedback(self.quiz.check_answer(user_answer="False"))

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzzzzzz")
        self.window.config(bg=THEME_COLOR, width=400, height=600, pady=20, padx=20)
        self.score_label=Label(text="score: 0", fg="white",bg=THEME_COLOR,font=("Arial",18,"italic"))
        self.score_label.grid(column=2,row=0)
        self.falseImage=PhotoImage(file="images/false.png")
        self.false_button=Button(image=self.falseImage)
        self.false_button.config(highlightthickness=0,pady=20, padx=20, command=self.false_answer)
        self.false_button.grid(column=1,row=2)
        self.trueImage = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.trueImage)
        self.true_button.config(highlightthickness=0, pady=20, padx=20, command=self.true_answer)
        self.true_button.grid(column=2, row=2)
        self.canvas=Canvas(width=350, height=550,bg="white")
        self.canvas.grid(column=1,row=1, columnspan=2, pady=50)
        self.question_text=self.canvas.create_text(175, 300, width=300, text="some text", font=("Arial", 18,"bold"))
        self.get_next_que()
        self.window.mainloop()
    def get_next_que(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your final score is {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.window.after(1000, self.window.destroy)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500,self.get_next_que)




