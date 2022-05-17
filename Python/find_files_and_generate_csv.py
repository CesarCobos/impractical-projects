import os
import re
import csv

def run(): 
    path = './'
    pattern = "PFI*.*"
    regex = r"[.-]"
    
    #Creating file columns
    columnas = "Nombre de Proyecto" + "/" + "Numero de Proyecto" + "/" + "Plano" + "/" + "Tipo de Plano" + "/" + "Ubicacion" 
    print(str(columnas.split("/")).strip("'[]").replace("'",''))
    #an ignore list of dirs
    ignore_list = ["Obsoleto","OBSOLETO","obsoleto","OBSOLETOS","Obsoletos","obsoletos"]
    
    #starting code
    for root,dirs, files in os.walk(path, topdown=True):
        #removing "obsolet" dirs
        [dirs.remove(d) for d in list(dirs) if d in ignore_list]
        for f in files:
            #if the files starts with some string and ends with some extension then list it
            if f.startswith("PFI") and f.endswith(".pdf"):
                name_proyect = str(''.join(f.split('.')[0:1])) + '%' + str(re.split(regex,f)[0:1]).replace(' ','').strip("'[] ") + '%' + str(re.split(regex,f)[1:2]).replace(' ','').strip("'[] ") + '%' + str(re.split(regex,f)[2:3]).strip("'[]") + '%' + str(root).replace(' ','').replace("./",'')
                output = str(name_proyect.split('%')).strip("'[] ").replace("'",'')
                #replace utf'8 chars
                for r in (("á","a"),("é","e"),("í","i"),("ó","o"),("ú","u")):
                    output = output.replace(*r)
             
                print(output.replace("pdf",''))

if __name__ == '__main__':
    run()