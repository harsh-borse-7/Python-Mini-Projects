
import random
random_num=random.randint(1,100)
guesses_count=1

print('''
*************************************************************
********************** WELCOME TO GAME **********************
************************************************************* 
''')

name=input("Enter Your Name: ")
print(f"Hello {name}, All the best !!!")
with open("log.txt",'w') as f:
    f.write(f"The Random Number is : {random_num}\n\n")

    guess=input("Guess The Number: ")


    try:
        Your_num=int(guess)
    except Exception as e:
        print(e)
    else:
        while(random_num!=Your_num):    
            guesses_count+=1
            f.write(f"You Guessed :{Your_num}\n")
            if(random_num>Your_num):
                guess=input("Guess Larger Number please :")
            
            else:
                guess=input("Guess Smaller Number please :")
            try:
                Your_num=int(guess)
            except Exception as e:
                print(e)

        print(f"Congratulation !!!You guessed in {guesses_count} guesses")   
        f.write(f"Right !!!The number is {random_num} You guessed in {guesses_count} guesses\n")



        with open("Highscore.txt",'r') as f1:
            high=f1.read()
                
        if(high==""):
                with open("Highscore.txt",'w') as f1:
                    f1.write(f"{guesses_count}\n")
        elif(int(high)>=guesses_count):
                with open("Highscore.txt",'w') as f1:
                    f1.write(f"{guesses_count}\n")

    
    