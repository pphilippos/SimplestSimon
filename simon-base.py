#!/bin/env python
import random
import time
import sys

sequence = []

def compare_sequence(string):
    result = string.upper() == "".join(sequence)
    return result

def clear_sequence():
    sequence.clear()

def extend_sequence():
    sequence.append(chr(65+random.randint(0,3)))

if __name__ == '__main__':

    print ("Welcome to Simon says!")
    while (1):
        cmd = input ("Press [enter] to play, or type exit to exit: ")
        if cmd=="exit":
            exit()
        for score in range(100):
            extend_sequence()
            for letter in sequence:
                sys.stdout.write ("\r"*50 + letter+" "*10)
                time.sleep(1)
                sys.stdout.write ("\r"*50)
                time.sleep(0.2)
            user_string = input("What did Simon say?\n")
            sys.stdout.write ("\r"*50+'\033[{}C\033[1A'+"\r"*50)
            if (compare_sequence(user_string)):
                print ("Correct! score=%d"%(score+1,))
            else:
                print ("Game over! score=%d"%(score))
                break
    

