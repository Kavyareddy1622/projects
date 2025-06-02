import random

def number_guess():
    rand = random.randint(1, 100)
    while True:
        try:
            choice = int(input("enter number between 1 and 100"))
            if choice > rand:
                print("too high")
            elif choice < rand:
                print("too low")
            else:
                print("number found")
                break
        except ValueError:
            print("invalid input")

if __name__ == "__main__":
    number_guess()
                
                
         
       
             
         
         
        


   
    
    
    
