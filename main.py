from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for dict in question_data:
    text = dict["question"]
    answer = dict["correct_answer"]
    question_bank.append(Question(text, answer))

    q_brain = QuizBrain(question_bank)

while q_brain.still_has_questions():
    q_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {q_brain.score}/{len(q_brain.questions_list)}")