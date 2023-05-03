#https://realpython.com/python-quiz-application/#step-1-ask-questions
from string import ascii_lowercase
import random
# variable Number_of_questions_per_quiz used to randomize the questions in quiz.
Number_of_questions_per_quiz = 5
#Quiz Question in Dictonary format 
# Options are in list format and correct answer will be first option
QUESTIONS = {
    "What is the national animal of New Zealand?" :[
     "Kiwi","Hedgehog","Lion","Tiger"
    ],
    "Which is the closest planet to the sun?" :[
    "Mercury","Venus","Earth","Jupitar"
    ],
    "In which sport can you score a slam dunk? ":[
    "Basketball","Cricket",'Rugby',"Tennis"
    ],
    "Halloween is traditionally in which month?":[
    "October","December","April","May"
    ],
    "Which country won the first World Cup Championship? ":[
    "Uruguay","Brazil","Germany","Argentina"
    ],
    "Which team has won the African Cup of Nations a record 7 times? ":[
    "Egypt","Cameroon","Senegal","Ghana"
    ]
}
# function restrict number of questions per Quiz
""" prepare_questions take two argument 
    1. argument is questions
    2. argument is number of question in current quiz
    this function return K number of random questions from questions list.
"""
def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

""" get_answer function take 2 argument 
    1. argument is question from the quiz and 
    2nd argumnet is given option of question
    This function add alphabetical label in given question option
    and return the user selected label. 

    """

def get_answer(question,alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]

""" 
 ask_question function takes 2 argument
 1st argument is question and 
 2nd  argument is question options
 this function generate the random order of the given options
 and call the get_answer function which return the user entered answer
 and print correct if user answer is correct 
   
"""

def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0
    
""" run_quiz() function first call prepare_question function then
      call ask_question then print 
       the result of quiz """

def run_quiz():
    questions = prepare_questions(
        QUESTIONS, num_questions=Number_of_questions_per_quiz
    )

    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)

    print(f"\nYou got {num_correct} correct out of {num} questions")


if __name__ == "__main__":
    run_quiz()

