from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(question["question"], question["correct_answer"])
                 for question in question_data]

quiz = QuizBrain(question_bank)
has_more_questions = True
while has_more_questions:
    quiz.next_question()
    has_more_questions = quiz.still_has_questions()
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
# TODO change the code to account for questions not all being true/false now