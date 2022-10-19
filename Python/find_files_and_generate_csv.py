import os
import re
import csv

ignore_list = ["Obsoleto","OBSOLETO","obsoleto","OBSOLETOS","Obsoletos","obsoletos"]
utf_replace ={
        "á":"a","é":"e","í":"i","ó":"o","ú":"u","ü":"u",
    }
    #replace dicts
plan_type_dict = {
    "AG&":"Arreglo General",
    "VLV&":"Valvula",
    "BTW&":"Bota aguas",
    "SPT&":"Soporte",
    "DSP&":"Despiece",
    "ESC&":"Escotilla",
    "FIN&":"Cuello de Succion",
    "S2R&":"Transicion",
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
    "SPC&":"Matachispas",
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
    "CE&":"Campana de extraccion",
    "CHN&":"Canal tipo U",
    "LMC&":"Lista de Materiales y componentes",
    "ANX&":"Anexo",
    "PMP&":"Progama de actividades",
    "DOC&":"Documento",
    "SPE&":"Especifiacion",
    "DMP&":"Compuerta Automatica",
    "DFL&":"Deflector",
    "LMAT&": "Lista de materiales",
    "MCAL&":"Memoria de calculo",
    "MSTR&":"Memoria de calculo estructural",
    "COM&":"Comunicado",
    "MINT&":"Minuta",
    "REPO&":"Reporte",
    "PRJ&":"Cronograma de actividades",
    "CAT&":"Catalogo de conceptos",
    "SPEC&":"Documento de especificacion",
    "FIL&":"Filtro",
    "PL&":"Plano de placas de acero",
    "PLM&":"Deflector",
    "IBX&":"Entrada de colector"
}
able_extensions = {
    "pdf&":"Documento PDF",
    "xlsx&":"Documento de Excel",
}
ending_extension=(
    "pdf",
    "xlsx",
    # "xls",
    # "docx",
    # "doc",
)

def run(): 
    path = './'
    #Column names
    name_files ="Nombre de Archivo"
    project_num = "Numero de proyecto"
    plan = "Plano"
    plan_type = "Tipo de plano"
    rev = "Revision"
    description ="Descripcion"
    extension = "Extension"
    location =" Ubicacion"
    
    #Regex structure
    regex = re.compile(r'(PFI\d\d\w\d{1,3}).*- ?([\w]{1,5}[^0-9])([\d]{1,5}).*?(R[\d]{1,3}).*- ?(.*)\.(\w{1,5})')
    #Creating - Replaciing CSV file
    with open("Lista de archivos.csv","w", newline='') as file:
        fieldnames=[name_files,project_num,plan,plan_type,rev,description,extension,location]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for root,dirs, files in os.walk(path, topdown=True):
            #removing "obsolet" dirs
            [dirs.remove(d) for d in list(dirs) if d in ignore_list]
            for f in files:
                result = re.match(regex,f)
                #if the files starts with some string and ends with some extension then list it
                if f.startswith('PFI') and f.endswith(ending_extension):
                    plan_replace = str(f'{result.group(2)}&')
                    extension_replace = str(f'{result.group(6)}&')
                    file_description = str(result.group(5))
                    for i in plan_type_dict.items():
                        plan_replace = plan_replace.replace(*i)
                    for i in able_extensions.items():
                        extension_replace = extension_replace.replace(*i)
                    
                    file_name = str(f'{result.group(1)}-{result.group(2)}{result.group(3)}{result.group(4)}-{result.group(5)}')
                    
                    for i in utf_replace.items():
                        file_name = file_name.replace(*i)
                        file_description = file_description.replace(*i)
                        f = f.replace(*i)
                        root = root.replace(*i)
                    writer.writerow({name_files: file_name,project_num:result.group(1),plan:f'{result.group(2)}{result.group(3)}',plan_type:plan_replace,rev:result.group(4),description:file_description,extension:extension_replace,location:root})

if __name__ == '__main__':
    run()