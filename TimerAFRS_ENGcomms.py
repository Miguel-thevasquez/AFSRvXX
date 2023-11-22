"""
after 4 hours of starting my inner engine, i proceed with the program i thought on at the 2am
this program it's desingned to work with a timer which time is set by ramdomness and choose a random activity to do
the objective of this program is to work with my reward system, anxiety managment and time of focus.
TimerAFRS, AFRS stands for Anxiety-Focus-reward_system
"""
#libraries
import time     #this library sets the timer
import random   #this lib allows you to get "random" numbers , digital systems are not got with randomness
import winsound #this one is for play sound :3

#global variable
count = 0 #activities counter
temp = 0  #temporal variable :v

#functions
def timer(a):   #defines the timer
    time.sleep(a) #sets programm to sleep by the time specified on a parameter
    winsound.PlaySound("C:\Windows\Media\Alarm03.wav",winsound.SND_FILENAME) #plays a pleasant sound i found at windows gallery
    print("time has ended and you had {}min\n ////////¡time to next activity!////////".format(int(a/60))) #prints the message

def activity(a): #this function choose a random activity from the list and non repeatable
    Mem = a #this variable stores a value to be used at the if cicle
    ACT = ["custom activity", "custom activity", "custom activity", "custom activity", "custom activity", "custom activity", "custom activity", "custom activity", "custom activity"] #custom activities list
    SLCTR = random.randint(1, len(ACT)) #defines SLCTR variable which stores a random number from 1 to the number of item that the list contains, len function counts in natural order

    if Mem != SLCTR:    #evaluates whether the memory variable is different than SLTR variable
        print("the activity is: {}".format(ACT[SLCTR-1])) #when the condition is fulfilled, the program prints on the console the activity to be performed, to choose the item
        #print("Mem different") #commented code to check for errors in the future ;v
        Mem = SLCTR # stores SLCTR value into Memory variable
        return Mem, SLCTR # returns values of each variable
    
    elif Mem == SLCTR: ##evaluates whether the memory variable is equal than SLTR variable
        SLCTR = random.randint(1, len(ACT)) #reassigns the value of SLCTR
        print("the activity is: {}".format(ACT[SLCTR-1])) #prints on console the activitie to realize
        #print("Mem wasnt different") #commented code to check for errors in the future ;v
        Mem = SLCTR # stores SLCTR value into Memory variable
        return Mem, SLCTR # returns values of each variable to be stored later
    return None #returns a none value to close the function

#program

while(True): #ciclo infinito while
    #print(State) #commented code to check for errors in the future ;v
    State = input("----//set 0 to end or 1 to continue//----\n") # stores the keyboard value as a string in the state variable
    #print(temp) #commented code to check for errors in the future ;v
    if "1" == State: # evaluates the content of the variable state which is stored as a string
        temp, Slc = activity(temp) # when condition is fulfilled function is executed and stores its returns
        print("Time starts now!") #user notice
        timer(random.randint(300,1800)) #executes timer function
        count += 1 #add 1 to the activity counter

    elif "0" == State: # evaluates the content of the variable state which is stored as a string
        break # if condition is fulfilled then the program ends
    else:
        print("option not contemplated") #if an option is given that was not contemplated to be evaluated
        continue #skips this iteration and starts the next one
print("ᕙ(⇀‸↼‶)ᕗヾ(-_- )ゞ(っ▀¯▀)つ ¡you achieved {} activities! ¡yey! (っ▀¯▀)つヾ(-_- )ゞᕙ(⇀‸↼‶)ᕗ".format(count)) #if the condition for the command break is fulfilled, it shows this message celebrating the number of activities you did this time. Congratulations!