from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

# We will create a dictionary that will hold the questions and answers in a dictionary

question_bank = []
question = 0

"""
Here, I've simplified the for loop. Initial was:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
"""

for question in question_data:
    question_bank.append(Question(question["text"], 
              question["answer"]))
    

quiz = QuizzBrain(question_bank)

while quiz.still_ask_question():
    quiz.next_question()
    print("\n")

print("You've compleated the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")