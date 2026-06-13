#HANGMAN GAME
import random

from sympy import false

from wordslist import words

hangman_art={0:("   ",
                "   ",
                "   "),

            1:(" o ",
                "   ",
                "   "),

            2: (" o ",
                " | ",
                "   ") ,

            3: (" o ",
                "/| ",
                "   "),

            4: (" o ",
                "/|\\",
                "   "),

            5: (" o ",
                "/|\\",
                "/ "),

            6: (" o ",
                "/|\\",
                "/ \\") ,
            }






def display_man(wrong_answer):
    print("**************************************")
    for line in hangman_art[wrong_answer]:
        print(line)
    print("***************************************")
def display_hint(hint):
    print(" ".join(hint))
def correct_answer(answer):
    print(" ".join(answer))




def main():


    answer = random.choice(words)
    hint =["_"] * len(answer)
    wrong_guessed =0
    guessed_letter =set()
    is_running=0



    while is_running==0:


        display_man(wrong_guessed)
        display_hint(hint)

        guess=input("Enter your guess: ").lower()


        if len(guess)!=1 or not guess.isalpha():
            print("Invalid input")
            continue



        if guess in guessed_letter:
            print("You already guessed this letter")
            continue
        guessed_letter.add(guess)



        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i]=guess


        else:
            wrong_guessed+=1



        if "_" not in hint:
            display_man(wrong_guessed)
            correct_answer(answer)
            print("You Win")
            is_running=false



        elif wrong_guessed >= len(answer)-1:
            display_man(wrong_guessed)
            correct_answer(answer)
            print("You Lose")
            is_running=false




if __name__ == "__main__":
    main()





