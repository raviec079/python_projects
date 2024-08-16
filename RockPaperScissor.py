""" design a python program which takes input user from user for rock or paper or scissor. Also write a function which randomly generates
    rock or paper or scissor. the number of times input to be taken is 3. if user beats the randomly generated result then a message of win
    should be displayed else lost.
"""
"""
DESIGN: we will use integers. 1 can beat 2, 2 can beat 3, 3 can beat 1. so generate random integers from 1 to 3 and return it and compare
        it with the integer entered by user and display the message.
"""
import random

def computer():
    n= random.randint(1,3)
    return n

def main():
    print("Welcome to the legendary ROCK PAPER SCISSOR GAME")
    print("! Enter 9 to exit the game !")
    user_wins=0
    computer_wins=0
    i=0
    while True:
        if user_wins>=2:
            print("Congrats, you won against the computer")
            break
        elif computer_wins>=2:
            print("Sorry you loose, Better luck next time.")
            break

        user_n = int(input("Enter '1' to select rock\t '2' to select scissor\t '3' to select paper\n"))
        computer_n=computer()
        # print("computer's value is ",computer_n)
        if user_n == computer_n:
            print("Draw, play again")
            continue
        elif user_n==1 and computer_n==2 or user_n==2 and computer_n==3 or user_n==3 and computer_n==1:
            user_wins+=1
        else:
            computer_wins+=1
        print(f"YOUR SCORE {user_wins}, COMPUTER SCORE {computer_wins}")
        if user_n==9:
            break

if __name__=='__main__':
    main()