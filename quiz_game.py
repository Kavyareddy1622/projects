import random

from httpx import options

QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'
def ask_question(index,question,options):
    print(f'{question}')
    for option in options:
        print(option)
    return input('your answer:').upper().strip()
def run_quiz(quiz):
    score=0
    random.shuffle(quiz)
    for index,item in enumerate(quiz,1):
        answer=ask_question(index,item[QUESTION],item[OPTIONS])
        if answer==item[ANSWER]:
            print('correct answer')
            score+=1
        else:
            print(f'wrong aswer correct answer is {item[ANSWER]}')
    print(f'Quiz over score is {score}')
def main():
    quiz=[
        {
            QUESTION:'Who painted the Mona Lisa?',
            OPTIONS:['A.Picasso','B.Leonardo da Vinci','C.Van Gogh','D.Michelangelo'],
            ANSWER:'B'
        },
        {
            QUESTION:'What is the chemical symbol for gold?',
            OPTIONS:['A.Ag','B.Au','C.Fe','D.Cu'],
            ANSWER:'A'
            
        }
    ]
    run_quiz(quiz)
if __name__=="__main__":       
    main() 
    
    
    