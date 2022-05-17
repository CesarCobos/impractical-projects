import os
import re
import csv

def run(): 
    path = './'
    pattern = "PFI*.*"
    regex = r"[.-]"
    
    #Creating file columns
    columnas = "Nombre de Proyecto" + "/" + "Numero de Proyecto" + "/" + "Plano" + "/" + "Rev" + "/" + "Tipo de Plano" + "/" + "Descripcion" + "/" + "Ubicacion" 
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
                name_proyect = str(''.join(f.split('.')[0:1])) + '%' + str(re.split(regex,f)[0:1]).replace(' ','').strip("'[] ") + '%' + str(re.split(regex,f)[1:2]).replace(' ','').strip("'[] ")[:-2] + '%' + str(re.split(regex,f)[1:2]).strip("'[] ").replace(' ','')[-2:] + '%' + str(re.split(regex,f)[1:2]).strip("'[] ").replace(' ','')[:-5]+ '&' + '%' + str(re.split(regex,f)[2:3]).strip("'[]") + '%' + str(root).replace(' ','').replace("./",'')
                output = str(name_proyect.split('%')).strip("'[] ").replace("'",'')
                #replace utf'8 chars
                for r in (("á","a"),("é","e"),("í","i"),("ó","o"),("ú","u")):
                    output = output.replace(*r)
                for t in (("AG&","Arreglo General"),
                            ("VLV&","Valvula"),
                            ("BTW&","Bota aguas"),
                            ("SPT&","Soporte"),
                            ("DSP&","Despiece"),
                            ("ESC&","Escotilla"),
                            ("FIN&","Cuello de Succion"),
                            ("S2R&","Transicion"),
                            ("STW&","Escalera Marina"),
                            ("YEE&","Yee"),
                            ("PLT&","Plataforma"),
                            ("RED&","Reduccion"),
                            ("PDG&","Paso de Gato"),
                            ("OMG&","Soporte tipo Omega"),
                            ("TRAP&","Trampa de Dren"),
                            ("NS&","Silenciador"),
                            ("DE&","Diagrama Electrico"),
                            ("PID&","Diagrama de Instrumentacion"),
                            ("SPC12&","Matachispas 12in"),
                            ("XPJ&","Junta de Expansion"),
                            ("BDR&","Brida"),
                            ("ASM&","Ensamble"),
                            ("BOX&","Cubierta"),
                            ("ELB&","Codo"),
                            ("MC&","Componente Mecanico"),
                            ("STR&","Armaduras"),
                            ("HOD&","Campana"),
                            ("CXN&","Conexion"),
                            ("CHW&","Cortina Hawaiana"),
                            ("MD&","Modulos Campana"),
                            ("WTT&","Bota aguas"),
                            ("VEM&","Ventilador"),
                            ("FIB&","Fan Inlet Box"),
                            ("TMP&","Plantilla"),
                            ("CHR&","Charola"),
                            ("HPR&","Tolva"),
                            ("DTS","Archivo de Detalle")):
                    output = output.replace(*t)
                print(output.replace("pdf",''))

if __name__ == '__main__':
    run()