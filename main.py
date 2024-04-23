from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    question_bank.append(question)
    print(question)

print(question_bank)