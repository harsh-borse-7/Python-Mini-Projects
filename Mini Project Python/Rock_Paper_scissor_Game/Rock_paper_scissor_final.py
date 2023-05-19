import random
import os    # Run System Command
play_again=2
game_num=0
with open("log_file.txt",'w') as f:

    print('''


        *************************************************************************
        *************    Welcome to Rock, Paper and Scissor Game    *************
        *************************************************************************

        ''')

    name=input("Enter Your Name Buddy: ")
    print(f"Hello {name}, All the best !!! \n")
    f.write(f"Hello {name}, All the best !!!\n")
    while(play_again==2):
        game_num+=1

        print(f"+++++++++++++++++++++++++++++ GAME NUMBER {game_num} +++++++++++++++++++++++++++++")
        f.write(f"+++++++++++++++++++++++++++++ GAME NUMBER {game_num} +++++++++++++++++++++++++++++\n")
        Options={1:"Rock",2:"Paper",3:"Scissor"}

        Comp_score=0
        Player_score=0
        counter_rounds=0


        try:
            ch=input("Number of Rounds you want to play: ")
            Rounds=int(ch)

            
            
            while(counter_rounds<Rounds):
                f.write(f"Computer Score : {Comp_score}\n")
                f.write(f"{name}'s Score : {Player_score}\n")
                f.write(f"^^^^^^^^^^^^^^^^^^^^^ Round {counter_rounds+1} ^^^^^^^^^^^^^^^^^^^^^\n")
                
                random_num=random.randint(1, 3)
                Generate_comp=Options[random_num]

                try:
                    print(f"Choices :  1:Rock   2:Paper   3:Scissor")
                    ch1=(input("Select Choice Number: "))
                    ch1=int(ch1)
                    Player_choice=Options[ch1]
                    print()
                except Exception as e:
                    print(e)
                else:
                    print(f"You Select: {Player_choice}")
                    print(f"Computer Select: {Generate_comp}\n")
                    f.write(f"You Select: {Player_choice}\n")
                    f.write(f"Computer Select: {Generate_comp}\n\n")
                    print()
                if(Player_choice==Generate_comp):
                    print(f"Round {counter_rounds+1} is Tie: \n")
                    f.write(f"Round {counter_rounds+1} is Tie: \n\n")

                elif(Player_choice=="Rock" and Generate_comp=="Paper"):
                    print(f"Round {counter_rounds+1} Goes to Computer Side.\n")
                    f.write(f"Round {counter_rounds+1} Goes to Computer Side.\n\n")
                    Comp_score+=1


                elif(Player_choice=="Scissor" and Generate_comp=="Rock"):
                    print(f"Round {counter_rounds+1} Goes to Computer Side.\n")
                    f.write(f"Round {counter_rounds+1} Goes to Computer Side.\n\n")
                    Comp_score+=1

                elif(Player_choice=="Paper" and Generate_comp=="Scissor"):
                    print(f"Round {counter_rounds+1} Goes to Computer Side.\n")
                    f.write(f"Round {counter_rounds+1} Goes to Computer Side.\n\n")
                    Comp_score+=1

                else:
                    print(f"Round {counter_rounds+1} Goes to Player Side.\n")
                    f.write(f"Round {counter_rounds+1} Goes to Player Side.\n\n")
                    Player_score+=1

                counter_rounds+=1

                if(Comp_score==(Rounds+1)/2 or Player_score==(Rounds+1)/2 ):
                    counter_rounds=Rounds
            
            print()
            print("Final Score... \n")
            print(f"Computer Score : {Comp_score}\n")
            print(f"{name}'s Score : {Player_score}\n\n")
            f.write("***************Final Score*************** \n")
            f.write(f"Computer Score : {Comp_score}\n")
            f.write(f"{name}'s Score : {Player_score}\n\n")

            if(Player_score==Comp_score):

                print("Game Tie\n")
                f.write("Game Tie\n\n\n")
            elif(Player_score>Comp_score):
                print(f"Yo Buddy, {name} You Won the Game!!!\n")
                f.write(f"Yo Buddy, {name} You Won the Game!!!\n\n\n")
            else:
                print(f"Sorry Buddy {name}, You lost the game\n")
                f.write(f"Sorry Buddy {name}, You lost the game\n\n\n")

        except Exception as e:
            print(e)


        else:
            print()
            play_again=int(input(" Wanna View Summery : 1.yes 2.No, Gonna Play again  ----> "))
os.system('log_file.txt')
