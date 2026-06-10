import html
from data import question_data


class Questions:
    def __init__(self,q_bank,score=0,question_number=0):
        self.question_bank = q_bank
        self.score = score
        self.current_number = question_number
        self.quiz_not_finished = True

    def show_current(self):
        questions = self.question_bank[self.current_number]["question"]
        return questions

    def next_question(self):
        self.current_number += 1
        if self.current_number >= len(self.question_bank):
            return None

        else:
            return self.question_bank[self.current_number]["question"]


question_bank = []

for item in question_data:
    question = html.unescape(item["question"])
    answer = item["correct_answer"]
    ques_answer = {
        "question":question,
        "answer": answer
    }

    question_bank.append(ques_answer)

