"""
after 4 hours of starting my inner engine, i proceed with the program i thought on at the 2am
this program it's desingned to work with a timer which time is set by ramdomness and choose a random activity to do
the objective of this program is to work with my reward system, anxiety managment and time of focus.
TimerAFRS, AFRS stands for Anxiety-Focus-reward_system
"""
#libraries
import time     #esta librería sirve para aplicar el delay del temporizador
import random   #esta librería te permite obtener valores "aleatoreos", los sistemas digitales binarios no son capaces de generar lo que se llama en rigor aleatoriedad
import winsound #esta nos permite reproducir sonido :3

#global variable
count = 0 #contador de actividades
temp = 0  #variable temporal :v

#functions
def timer(a):   #define el temporizador
    time.sleep(a) #el programa se inactiva por el tiempo especificado con a
    winsound.PlaySound("C:\Windows\Media\Alarm03.wav",winsound.SND_FILENAME) #reproduce este sonido tan placentero
    print("se ha cumplido el tiempo de {}min\n ////////¡Hora de cambiar de actividad!////////".format(int(a/60))) #imprime el mensaje de forma bonita

def activity(a): #función elegir una actividad aleatorea de una lista de manera "aleatorea" y no repetible
    Mem = a #definición de la variable que hará de memoria para comparar en el ciclo if
    ACT = ["custom activity", "custom activity", "custom activity", "custom activity", "custom activity", "custom activity", "custom activity", "custom activity", "custom activity"] #lista de actividades
    SLCTR = random.randint(1, len(ACT)) #define la variable SLCTR con un número aleatoreo entre 1 y la cantidad de items que tiene la lista, la función len cuenta en cantidad de conjunto natural

    if Mem != SLCTR:    #evalúa si la variable de memoria es diferente a la variable SLTR
        print("la actividad es: {}".format(ACT[SLCTR-1])) #al cumplirse la condición el programa imprime en consola la actividad a realizar, para elegir el item
        #print("Mem different") #codigo comentado para comprobar si hay algún error en el futuro ;v
        Mem = SLCTR # almacena el valor de SLCTR en la variable memoria
        return Mem, SLCTR # retorna los valores de cada uno para luego ser almacenados
    
    elif Mem == SLCTR: #evalúa #evalúa si la variable de memoria es igual a la variable SLTR
        SLCTR = random.randint(1, len(ACT)) #reasigna el valor de SLCTR
        print("la actividad es: {}".format(ACT[SLCTR-1])) #imprime en consola la actividad a realizar, para elegir el item
        #print("Mem wasnt different") #codigo comentado para comprobar si hay algún error en el futuro ;v
        Mem = SLCTR # almacena el valor de SLCTR en la variable memoria
        return Mem, SLCTR # retorna los valores de cada uno para luego ser almacenados
    return None #retorna un valor none que no será almacenado en ningún lugar

#program

while(True): #ciclo infinito while
    #print(State) #codigo comentado para comprobar si hay algún error en el futuro ;v
    State = input("----//escriba 0 para finaliza o 1 para continuar//----\n") # almacena el valor del teclado como un string en la variable state
    #print(temp) #codigo comentado para comprobar si hay algún error en el futuro ;v
    if "1" == State: # evalua el contenido de la variable tipo string state con el carácter
        temp, Slc = activity(temp) #al cumplirse la condición se ejecuta y almacena la función activity
        print("El temporizador inicia ahora") #aviso para el usuario
        timer(random.randint(300,1800)) #ejecuta la función timer
        count += 1 #suma 1 al contador de actividades

    elif "0" == State: # evalua el contenido de la variable tipo string state con el carácter
        break # si se cumple la condición termina el programa
    else:
        print("no se reconoce la opción") #si se da una opción que no se contempló para ser evaluada
        continue #salta la ejecución y ejecuta nuevamente el ciclo
print("ᕙ(⇀‸↼‶)ᕗヾ(-_- )ゞ(っ▀¯▀)つ ¡hoy hiciste {} actividades! ¡yey! (っ▀¯▀)つヾ(-_- )ゞᕙ(⇀‸↼‶)ᕗ".format(count)) #si se cumple la condición para el comand break muestra este mensaje que celebra la cantidad de actividades que hiciste esta vez. Felicidades!