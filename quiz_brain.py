class QuizBrain:

    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_num < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_ans = input(f"Q.{self.question_num}: {current_question.text} (True/False): ")
        self.answer_check(user_ans, current_question.answer)

    def answer_check(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_ans}\nYour current score is: {self.score}/{self.question_num}\n")

    def final_msg(self):
        print(f"You've completed the quiz\nYour final score is: {self.score}/{len(self.question_list)}")
