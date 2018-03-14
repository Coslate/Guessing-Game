#! /usr/bin/env python3.6
'''
#Author  : Coslate
#Purpose : This progriam is Guessing Game.
#date    : 2018/03/14
'''
import random as rnd

#main function
def main():
    '''main function'''
    user_guess_count = 0
    user_guess_val = 0
    distance = 0
    rand_val_targ = rnd.randint(1, 100)

    while(True):
        user_input = input("Please enter your guess : ")
        if(user_input == "End"):
            print("End the program. You have guessed {x} times.\n".format(x = user_guess_count))
            break
        else:
            user_guess_val = int(user_input)
            current_dist = abs(user_guess_val - rand_val_targ)

            if((user_guess_val < 1) or (user_guess_val > 100)):
                print("OUT OF BOUND!\n")
            else:
                if(current_dist == 0):
                    print("CORRECT! You have guessed {x} times.\n".format(x = user_guess_count+1))
                    break
                if(user_guess_count > 0):
                    if(current_dist > distance):
                        print("COLDER!\n")
                    else:
                        print("WARMER!\n")
                else:
                    if(current_dist <= 10):
                        print("WARM!\n")
                    else:
                        print("COLD!\n")

            distance = current_dist
            user_guess_count += 1

#---------------execution---------------#
if __name__ == '__main__':
    main()
