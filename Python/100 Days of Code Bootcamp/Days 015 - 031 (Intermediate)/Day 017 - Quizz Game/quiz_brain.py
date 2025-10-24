"""
This will create a class that will initiate the Quizz Game

First, we will create a init that will have the question_number, which will be 0 to get the first question.
The init will also hold the question_list from the question_bank list in the main.py

Second, the next_question() method will get the question and the question number.
It will pull the corresponding question, ask the user for a prompt
and it will increase the question_number by 1 to get the next question.

Third, create a method to check the answer

Last, the still_ask_questions will check if there are any questions left in the question_list.
"""

class QuizzBrain():
    
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.question_list = questions_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.q_text} (True/False): ")
        self.check_answer(user_answer, current_question.q_answer)
        

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right.")
        else:
            print(f"That's wrong! The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.")

    def still_ask_question(self):
        return self.question_number < len(self.question_list)
