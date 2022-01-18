# TODO ask the question
# TODO check is the answer is correct
# TODO check if we're at the end of the quiz


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        # TODO retrieve the item from the question_list at the current
        #   question_number
        question = self.question_list[self.question_number]
        # then use input() to show the current question's text and ask for
        #   the user's answer
        user_answer = input(question.text + " True of False?\n")
        if user_answer.title() == question.answer:
            print("Correct")
        else:
            print("Incorrect")
