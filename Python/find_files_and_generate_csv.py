import os
import re
import csv

def run(): 
    path = './'

    #Creating file columns
    columnas = "Nombre de archivo" + "/" + "Numero de Proyecto" + "/" + "Plano" + "/" + "Rev" + "/" + "Tipo de Plano" + "/" + "Descripcion" + "/" + "Ubicacion" 
    print(str(columnas.split("/")).strip("'[]").replace("'",''))
    #an ignore list of dirs
    ignore_list = ["Obsoleto","OBSOLETO","obsoleto","OBSOLETOS","Obsoletos","obsoletos"]
    #replace dicts
    blueprint_replace = {
        "AG&":"Arreglo General",
        "VLV&":"Valvula",
        "BTW&":"Bota aguas",
        "SPT&":"Soporte",
        "DSP&":"Despiece",
        "ESC&":"Escotilla",
        "FIN&":"Cuello de Succion",
        "S2R&":"Transicion",
        "S&": "Transicion",
        "STW&":"Escalera Marina",
        "YEE&":"Yee",
        "PLT&":"Plataforma",
        "RED&":"Reduccion",
        "PDG&":"Paso de Gato",
        "OMG&":"Soporte tipo Omega",
        "TRAP&":"Trampa de Dren",
        "NS&":"Silenciador",
        "DE&":"Diagrama Electrico",
        "PID&":"Diagrama de Instrumentacion",
        "SPC12&":"Matachispas 12in",
        "XPJ&":"Junta de Expansion",
        "ASM&":"Ensamble",
        "BOX&":"Cubierta",
        "ELB&":"Codo",
        "MC&":"Componente Mecanico",
        "STR&":"Armaduras",
        "HOD&":"Campana",
        "CXN&":"Conexion",
        "CHW&":"Cortina Hawaiana",
        "MD&":"Modulos Campana",
        "WTT&":"Bota aguas",
        "VEM&":"Ventilador",
        "FIB&":"Fan Inlet Box",
        "TMP&":"Plantilla",
        "CHR&":"Charola",
        "HPR&":"Tolva",
        "DTS&":"Archivo de Detalle",
        "BRD&":"Brida",
        "BDR":"Brida",
        "CE&":"Campana de extraccion",
        "CHN&":"Canal tipo U",
        "LMC&":"Lista de Materiales y componentes",
        "ANX$":"Anexo",
        "PMP$":"Progama de actividades"
    }
    utf_replace ={
        "á":"a","é":"e","í":"i","ó":"o","ú":"u"
    }

    #PFI21C001-S2R001R10-descripcion
    regex = re.compile(r'(PFI\d\d\w\d{1,3}).*- ?([\w]{1,5}[\d]{1,3}).*?([\w]{1,}).*?(.*)\.')
    regex_rev = re.compile(r'.*(R[\d]{1,3})')
    regex_blueprint =re.compile(r'PFI\d\d\w\d{2,3} ?- ?([A-Z]{1,3}|\w\d\w)')

    #starting code
    for root,dirs, files in os.walk(path, topdown=True):
        #removing "obsolet" dirs
        [dirs.remove(d) for d in list(dirs) if d in ignore_list]
        for f in files:
            #if the files starts with some string and ends with some extension then list it
            for i in utf_replace.items():
                f = f.replace(*i)

            if f.startswith("PFI") and f.endswith(".pdf"):
                res = re.match(regex,f)
                rev = re.match(regex_rev,f)
                blueprint = re.match(regex_blueprint,f)
                blueprint_replaced = str((f"{blueprint.group(1)}&"))
                name_replace = str(f"{res.group(4)}").replace('-', '')
                path = path.replace('./','')
                for r in blueprint_replace.items():
                    blueprint_replaced = blueprint_replaced.replace(*r)

                if res:
                    name_part_two= (f"{res.group(1)},{res.group(2)},{rev.group(1)},{blueprint_replaced},{name_replace.lstrip(' ').rstrip(' ')}")
                    name_part_one = (f"{res.group(1)}-{res.group(2)}{rev.group(1)}")
                    print(f"{name_part_one},{name_part_two}{path}")

                    
if __name__ == '__main__':
    run()