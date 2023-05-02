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
# restrict number of questions per Quiz
num_questions = min(Number_of_questions_per_quiz, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions) #pick the random question from QUESTION list

num_correct_answer = 0    

for num, (question,alternatives) in enumerate(questions,start=1):
    print(f'Question{num}:')
    print(f'{question}')
    correct_answer = alternatives[0]
    #labeled_alternatives variable is used to shuffle the options
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
    )
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    #answer_label = input("\nChoice? ")
    while ( answer_label := input("\nChoice? ")).lower() not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")
    answer = labeled_alternatives.get(answer_label.lower())
    
    if answer == correct_answer: 
        num_correct_answer += 1
        print("⭐ Correct! ⭐")
    else:
         print(f"The answer is {correct_answer!r}, not {answer!r}")
print(f"\nYou got {num_correct_answer} correct out of {num} questions")