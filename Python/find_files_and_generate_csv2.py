import os
import re
import csv

ignore_list = ["Obsoleto","OBSOLETO","obsoleto","OBSOLETOS","Obsoletos","obsoletos"]
utf_replace ={"á":"a","é":"e","í":"i","ó":"o","ú":"u","ü":"u",}
    #replace dicts

plan_type_dict = {
    "AGS":"Aguascalientes",
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
    regex = re.compile(r'(\w*)\_\w*\-\w*\_\w*\_\d*.\d{1,4}\_\w*\_\d*')
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
                if f.endswith(ending_extension):
                    file_name = str(f'{result.group(1)}')
                    
    #Replacing utf characters
                    file_name =replace_fn(file_name, utf_replace)
                    print(file_name)
                    # plan_type = replace_fn(str(f'{result.group(2)}&'), plan_type_dict)
                    # file_extension = replace_fn(str(f'{result.group(6)}&'), able_extensions)
                    # file_description = replace_fn(str(result.group(5)), utf_replace)
                    # root = replace_fn(root, utf_replace)
    #writing csv file
                    # writer.writerow({file_name_column: file_name,project_num_column:result.group(1)
                    #                 ,plan_column:f'{result.group(2)}{result.group(3)}'
                    #                 ,plan_type_column:plan_type,rev_column:result.group(4)
                    #                 ,description_column:file_description,extension_column:file_extension
                    #                 ,location_column:root})
    #Deleting plot.log files
                # if f.endswith(deleted_extensions):
                #     log_location= str(f'{root}/{f}')
                #     os.remove(log_location)
                #     print(f'Archivo {f} eliminado de {root}')
#main
if __name__ == '__main__':
    run()