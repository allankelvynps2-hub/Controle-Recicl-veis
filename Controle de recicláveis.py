# Sistema de Coleta de Materiais Reciclaveis
from datetime  import datetime

data_entrada = datetime.today()

materiais = {
   "20 01 01 - Papel e papelão": 10.0,
   "20 01 02 - Vidro": 5.0,
   "20 01 36 - Eletronicos fora de uso": 2.0,
   "20 01 39 - Plasticos": 8.0,
   "20 01 40 - Metais": 3.0,
}

total = 0

print("SISTEMA DE COLETA DE RECICLAGEM")
print("Data de Entrada:", data_entrada)
print()

for material, peso in materiais.items():
   print(material,"-", peso, "kg")
   total += peso

   print("------------------------------")
   print("total coletado:",total,"kg")

