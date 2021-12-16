#Created for entertainment and learning purposes, it is not intended to offend any type of person 

#Regaeton lyrics generator
#This code reads some lists with verbs and commons words used, by a structure and a random selection generates the lyrics, then creates and show a TXT file with it
#If the "lyrics" file exists then it replace the content, if not a new file is created
#Created with Python 3.10, should work with an older version


import random

subject =['mami','chica','bebé','princess','loca', 'lady']
action=['quiero','vamos a','voy a', 'vengo a']
verb=['darte', 'castigarte','azotarte','encenderte','amarte', 'ligar', 'jugar']
intensidad=['duro', 'rapido', 'lento', 'suave', 'fuerte']
time=['hasta que salga el sol', 'toda la noche', 'hasta el amanecer', 'hasta mañana', 'todo el día'] 
something=['sin miedo', 'sin anestesia', 'contra el piso', 'contra la pared', 'sin compromiso', 'face to face', 'sin compromiso']

def run():  

    #Opening txt file
    f = open("lyrics.txt", "w")
    
    #Here starts to generate lyrics and writting the TXT file

    #intro: Using a for cycle to create a kind of intro
    f.write("\n[ Intro ] \n")
    for i in range(4):
        intro=(random.choice(subject).title() + " " + random.choice(action) + " " + random.choice(verb) + " " + random.choice(intensidad) + " " + random.choice(time))
        f.write(intro+"\n")

    #bridge: Just a pre-corus
    bridge=("\n[ Bridge ]\n" + random.choice(verb).title() + " " + random.choice(verb) + " " + random.choice(verb) + ", " + random.choice(time) + ", " + random.choice(intensidad) + "\n")
    f.write(bridge + "\n")

    #Corus: similar to "Intro", it is created with a for cycle
    f.write("\n[ Coro ] \n")
    for i in range(4):
        coro1=(random.choice(subject).title()  +" " + random.choice(action) + " " + random.choice(verb) + " " + random.choice(intensidad) + " " + random.choice(time) + " + " + random.choice(something))
        f.write(coro1 + "\n")

    #Another bridge
    bridge2=("\n[ Bridge ]\n" + random.choice(verb).title() + " " + random.choice(verb) + " " + random.choice(verb) + ", " + random.choice(time) + ", " + random.choice(intensidad) + "\n")
    f.write(bridge2)
  
    #Now, lyrics are done, and we can close the TXT file
    f.close()

    #Now it is showing the file in the prompt
    f = open("lyrics.txt", "r")
    print(f.read())
    f.close()


if __name__ == '__main__':
    run()