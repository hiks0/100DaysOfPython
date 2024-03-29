class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_score = 0

    def still_have_questions(self):
        if self.question_number != (len(self.question_list) - 1):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q. {self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_answer, correct_answer ):
        if user_answer.lower() == correct_answer.lower():
            self.current_score += 1
            print("you got it right")
            print(f"current score {self.current_score}/{self.question_number}")
            print("\n")
        else:
            print("you got it wrong")
            print(f"the correct answer was {correct_answer}")
            print(f"current score {self.current_score}/{self.question_number}")
            print("\n")
