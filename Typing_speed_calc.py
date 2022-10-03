# you have to import time module
# you import random module
from time import *
import random

# Defining a function error1 to find errors in given user input or what he have typed...

def error1(para,user):
    error=0
    for i in range(len(para)):
        try:
            if para[i]!=user[i]:
                error = error+ 1
        except :
            error=error+1
    return error

#defining speed of function by time module to find speed of the typing..
def speed(time_1,time_2,user):
    diftime=time_2-time_1
    diftime_r=round(diftime,2)
    speed=len(test1)/diftime_r
    return round(speed)


# kept while loop and it runs until you type 'no' and for yes it goes on giving random paragraphs for you to type..
while True:
    k=input('  READY to TEST: yes/no:  ')
    if k=='yes':
        test = ['In Avengers: Age of Ultron, Jarvis tried to destroy ultron but failed fully', 'My name is Robert',
                'I live in United states of America']
        test1 = random.choice(test)
        print('*************TYPING_SPEED******************')

        print(test1)
        print()
        print()
        time_1 = time()
        user = input('Enter : ')
        time_2 = time()
        print('Speed: ', speed(time_1, time_2, user), 'w/seconds')
        print('ERRORS ARE: ', error1(test1, user))
    elif k=='no':
        print('  Thank you  ')
        break
    else:
        print('YOU did not give yes/no you have wrong input!!!')
