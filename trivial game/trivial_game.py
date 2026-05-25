
import random

questions={
    "who are you":"way",
    "i am who":"iaw",
    "why i am saying this":"wiast",
    "learn something new":"lsn"
}

def python_trivial_game():
    question_list=list(questions.keys())
    total_questions=4
    score=0
    selectquestions=random.sample(question_list,total_questions)

    for idx,question in enumerate(selectquestions):
        print(f"{idx+1}. {question}")
        user_answer=input("Your answer: ").lower().strip()
        correct_Answer=questions[question]
        if user_answer==correct_Answer.lower():
            print("Correct\n")
            score+=1
        else:
            print(f"Wrong: correct answer is : {correct_Answer}.")
        
    print(f"Game Over your score is: {score}")


python_trivial_game()