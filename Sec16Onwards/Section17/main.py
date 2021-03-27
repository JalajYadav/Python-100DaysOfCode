from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_ques()

print("You have completed the quiz. ")
print(f"Your Final score is {quiz.score}/{quiz.question_number}")