import os
import re
import csv

ignore_list = ["Obsoleto","OBSOLETO","obsoleto","OBSOLETOS","Obsoletos","obsoletos"]
utf_replace ={"á":"a","é":"e","í":"i","ó":"o","ú":"u","ü":"u",}
    #replace dicts

plan_type_dict = {
    "AG&":"Arreglo General","DSP&":"Despiece","DE&":"Diagrama Electrico","PID&":"Diagrama de Instrumentacion","ASM&":"Ensamble",
    "VLV&":"Valvula","DMP&":"Compuerta Automatica",
    "VEM&":"Ventilador", "FIB&":"Fan Inlet Box","NS&":"Silenciador","XPJ&":"Junta de Expansion","FIN&":"Cuello de Succion",
    "CE&":"Campana de extraccion","HOD&":"Campana","BOX&":"Cubierta","STR&":"Armaduras","MD&":"Modulos Campana","CHW&":"Cortina Hawaiana",
    "PLT&":"Plataforma","PDG&":"Paso de Gato","PL&":"Plano de placas de acero",
    "STW&":"Escalera Marina","ESC&":"Escotilla",
    "IBX&":"Entrada de colector","HPR&":"Tolva", 
    "TMP&":"Plantilla", 
    "BTW&":"Bota aguas","WTT&":"Bota aguas",
    "SPT&":"Soporte","OMG&":"Soporte tipo Omega",
    "MC&":"Componente Mecanico",
    "S2R&":"Transicion","YEE&":"Yee","RED&":"Reduccion",
    "TRAP&":"Trampa de Dren",
    "FIL&":"Filtro",
    "SPC&":"Matachispas",  
    "ELB&":"Codo","CXN&":"Conexion","DTS&":"Archivo de Detalle","BRD&":"Brida",
    "CHR&":"Charola","CHN&":"Canal tipo U","PLM&":"Deflector","DFL&":"Deflector",
    "LMC&":"Lista de Materiales y componentes", 
    "ANX&":"Anexo","DOC&":"Documento","COM&":"Comunicado", "MINT&":"Minuta", "REPO&":"Reporte",
    "SPEC&":"Documento de especificacion", "PRJ&":"Cronograma de actividades", "CAT&":"Catalogo de conceptos",
    "LMAT&": "Lista de materiales", 
    "MCAL&":"Memoria de calculo", "MSTR&":"Memoria de calculo estructural",
    "REF&" :"Archivo de referencia ",
}
able_extensions = {
    "pdf&":"Documento PDF","xlsx&":"Documento de Excel",
}
ending_extension=(
    "pdf","xlsx",# "xls",# "docx",# "doc",
)
deleted_extensions=(
    "log","bak",
)

def run(): 
    #Replace function
    def replace_fn(file, bd_dict):
        for i in bd_dict.items():
            file = file.replace(*i)
        return file  
    path = './'
    #Field names
    file_name_column ="Nombre de Archivo"
    project_num_column = "Numero de proyecto"
    plan_column = "Plano"
    plan_type_column = "Tipo de plano"
    rev_column = "Revision"
    description_column ="Descripcion"
    extension_column = "Extension"
    location_column =" Ubicacion"
    
    #Regex structure
    #Regex groups: G1:Project, G2:Plan type G3:Plan number G4: Rev G5:File description G6: extension
    regex = re.compile(r'(PFI\d\d\w\d{1,3}).*- ?([\w]{1,5}[^0-9])([\d]{1,5}).*?(R[\d]{1,3}).*- ?(.*)\.(\w{1,5})')
    #Creating - Replaciing CSV file
    with open("Lista de archivos.csv","w", newline='') as file:
        fieldnames=[file_name_column,project_num_column,plan_column,plan_type_column
                    ,rev_column,description_column,extension_column,location_column]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
    #Writting header
        writer.writeheader()
    #Looking for files
        for root,dirs, files in os.walk(path, topdown=True):
    #removing "obsolet" dirs
            [dirs.remove(d) for d in list(dirs) if d in ignore_list]
    #For all files in path, look for matches
            for f in files:
                result = re.match(regex,f)
    #if the files starts with some string and ends with some extension then list it
                if f.startswith('PFI') and f.endswith(ending_extension):

                    file_name = str(f'{result.group(1)}-{result.group(2)}{result.group(3)}{result.group(4)}-{result.group(5)}')
    #Replacing utf characters
                    file_name =replace_fn(file_name, utf_replace)
                    plan_type = replace_fn(str(f'{result.group(2)}&'), plan_type_dict)
                    file_extension = replace_fn(str(f'{result.group(6)}&'), able_extensions)
                    file_description = replace_fn(str(result.group(5)), utf_replace)
                    root = replace_fn(root, utf_replace)
    #writing csv file
                    writer.writerow({file_name_column: file_name,project_num_column:result.group(1)
                                    ,plan_column:f'{result.group(2)}{result.group(3)}'
                                    ,plan_type_column:plan_type,rev_column:result.group(4)
                                    ,description_column:file_description,extension_column:file_extension
                                    ,location_column:root})
    #Deleting plot.log files
                if f.endswith(deleted_extensions):
                    log_location= str(f'{root}/{f}')
                    os.remove(log_location)
                    print(f'Archivo {f} eliminado de {root}')
#main
if __name__ == '__main__':
    run()