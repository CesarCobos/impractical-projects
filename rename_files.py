import os, re

def cl():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def run():
    #Asking to User for the file path 
    filepath= str(input("\nIngresa el directorio donde se encuentran tus archivos \n"))
    #If the path doesn't exists then shows a message and then the program exits
    if not os.path.exists(filepath):
        
        cl()

        print("\nLa carpeta no se encuentra\n")
        os._exit(1)

    #Showing the number of files
    fileName=os.listdir(filepath)
    
    cl()
    print("Tienes %i archivo(s) en esta carpeta \n" %len(fileName))
    
    #counter for the next for loop
    count= 0

    #If the folder exists then the program asks for a word to replace
    phrase=str(input("\nQué palabra o frase quieres reemplazar? \n"))
    replace=str(input("\nEscribe la nueva palabra o frase: \n"))

    #Replacing by a For loop
    for name in fileName:
        newName = re.sub(phrase, replace, name)
        os.rename(filepath + '/' + name, filepath + '/'+ newName )
        count+= 1
    print("\nSe ha reemplazado el nombre de los archivos")

if __name__ == '__main__':
    run()