from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(question["text"], question["answer"])
                 for question in question_data]

quiz = QuizBrain(question_bank)
has_more_questions = True
while has_more_questions:
    quiz.next_question()
    has_more_questions = quiz.still_has_questions()
