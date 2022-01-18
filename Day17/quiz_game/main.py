from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(question["text"], question["answer"])
                 for question in question_data]

quiz_brain = QuizBrain(question_bank)
quiz_brain.next_question()
