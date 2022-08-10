from tkinter import *
from quiz_brain import QuizBrain
import html
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="White")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Hello",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #label
        self.score_label = Label(text="Score:0", bg=THEME_COLOR,fg= "White")
        self.score_label.grid(row=0, column=1)

        #Button
        true_pic = PhotoImage(file="images/true.png")
        self.true_mark = Button(image=true_pic,command= self.correct_answer)
        self.true_mark.grid(row=2,column=0)
        false_pic = PhotoImage(file = "images/false.png")
        self.false_mark = Button(image=false_pic,command=self.wrong_answer_)
        self.false_mark.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg ="White")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text,text= "You've reached the end of the quiz")
            self.true_mark.config(state="disabled")
            self.false_mark.config(state="disabled")
    
    def correct_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_answer_(self):
        is_right =  self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="Green")
            self.score_label.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.config(bg="Red")
            self.score_label.config(text=f"Score:{self.quiz.score}")
        self.window.after(1000,self.get_next_question)