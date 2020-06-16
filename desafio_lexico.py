import re

# Autores
# Ítalo Martins Tomaz Rocha RA: 082170012
# Milena Ferreira de Paula RA: 082170022

pascal_keys=""
pascal_code =""


with open("pascal-keys.txt","r") as pkeys:
    pascal_keys = pkeys.read().split()

 
with open("p1.pas","r") as pkeys:
    pascal_code = pkeys.read().lower()
    

lexemas=[]

integerPattern =  r"^[0-9]$"
floatPattern =  r"^[0-9].[0-9]$" 
operatorPattern = r"^(:=|:|\+|\-|\*)$"


for token in pascal_code.replace(";",'').split():
    if token in pascal_keys:
       lexemas.append([token,"key word"])
    elif re.match(floatPattern, token):
       lexemas.append([token,"float"])
    elif re.match(integerPattern, token):
       lexemas.append([token,"int"])
    elif re.match(operatorPattern,token):
       lexemas.append([token,"operator"])
    else:
        lexemas.append([token,"unknow"])


print(lexemas)

# with open("tokens.txt","w") as lexemas_file:
#     lexemas_file.write(str(lexemas))

# 1. ler arquivo
# 2. quebrar em tokens
# 3. usar regexp para verificar o tipo de token

# palavras reservadas - keywords
# float
# int
# variáveis -> regexp
# operações (+, -, *, ^, =, :=)

# Lex - Parser >>> WEB Scraping

# TODO: Terminar...



