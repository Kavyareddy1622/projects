import random
def rock_paper_scissor():
    choices=('r','p','s')
    while True:
        user_choice=input('enter choice r/p/s: ').lower()
        computer_choice=random.choice(choices)
        print(f'{user_choice}')
        print(f'{computer_choice}')
        if user_choice not in choices:
            print('invalid choice')
            continue
        else:
            if user_choice==computer_choice:
                print('tie')
            elif((user_choice == 'r' and computer_choice == 's') or 
                 (user_choice == 's' and computer_choice == 'p') or 
                 (user_choice == 'p' and computer_choice =='r')):
                print('you win')
            else:
                print('you lose')
        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break
if __name__ == "__main__":
    rock_paper_scissor()
        
    
    