import os
import re

def run(): 
    path = './'
    pattern = "PFI*.*"
    regex = r"[.-]"
    columnas = "Nombre de Proyecto" + "/" + "Numero de Proyecto" + "/" + "Plano" + "/" + "Tipo de Plano" + "/" + "Ubicacion" 
    print(str(columnas.split("/")).strip("'[]").replace("'",''))

    ignore_list = ["Obsoleto","OBSOLETO","obsoleto","OBSOLETOS","Obsoletos","obsoletos"]

    for root,dirs, files in os.walk(path, topdown=True):
        [dirs.remove(d) for d in list(dirs) if d in ignore_list]
        for f in files:
            if f.startswith("PFI") and f.endswith(".pdf"):
                name_proyect = str(''.join(f.split('.')[0:1])) + '%' + str(re.split(regex,f)[0:1]).replace(' ','').strip("'[] ") + '%' + str(re.split(regex,f)[1:2]).replace(' ','').strip("'[] ") + '%' + str(re.split(regex,f)[2:3]).strip("'[]") + '%' + str(root).replace(' ','').replace("./",'')
                output = str(name_proyect.split('%')).strip("'[] ").replace("'",'')
                for r in (("á","a"),("é","e"),("í","i"),("ó","o"),("ú","u")):
                    output = output.replace(*r)

                print(output.replace("pdf",''))

if __name__ == '__main__':
    run()