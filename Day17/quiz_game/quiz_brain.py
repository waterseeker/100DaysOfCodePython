class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} \
(True/False:)\n")
        if user_answer.title() == current_question.answer:
            print("Correct")
        else:
            print("Incorrect")
