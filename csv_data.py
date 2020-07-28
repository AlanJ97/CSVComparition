#Importando librerías
import pandas
import numpy as np
#DEFINIENDO LOS HEADERS DE LAS COLUMNAS
colnames = ['emails']
colnamesGeneral = ['nempl','employee_name','email1','email2']

#ABRIENDO LOS ARCHIVOS NECESARIOS
dataTodo = pandas.read_csv('todos_data.csv', names=colnames)
dataEnviado = pandas.read_csv('enviados.csv', names=colnames)
dataGeneral = pandas.read_csv('cfdi_emails.csv', names=colnamesGeneral)

#TRANSFORMANDO A LISTAS
emails_todos = dataTodo.emails.tolist()
emails_enviados = dataEnviado.emails.tolist()
emails_general_nemp = dataGeneral.nempl.tolist()
emails_general_employee_name = dataGeneral.employee_name.tolist()
emails_general_email1 = dataGeneral.email1.tolist()
emails_general_email2 = dataGeneral.email2.tolist()

#IMPRIMIENDO LAS LISTAS PARA VER SI TRAE LA INFORMACIOŃ
#print(emails_todos)
#print(emails_enviados)
#print (emails_general)

#DEFINIENDO LAS LISTAS A LLENAR CON LOS DATOS REQUERIDOS
emails_no_enviados  = []
Data_general_no_enviada = [[],[],[],[]]

#RECORRIENDO LAS LISTAS PARA COMPARAR
for i in range(len(emails_enviados)):
    pass
    #print("ENVIADOS :" , emails_enviados[i])

for i in range(len(emails_todos)):
    pass
    #print("TODOS:" , emails_todos[i]) 

for i in range(len(emails_todos)):
    if emails_todos[i] in emails_enviados:
        #print ("COINCIDENCIA")
       pass
    else:
       # print ("NO COINCIDEN")
        emails_no_enviados.append(emails_todos[i])

for i in range(len(emails_no_enviados) ):
    pass
    #print(emails_no_enviados[i])

#Este contador mide el numero de filas que habra en la lista para el for siguiente
contador = 0
for i in range(len(emails_general_email2)):
    if emails_general_email2[i] in emails_no_enviados:
        #print(emails_general_nemp[i])
        Data_general_no_enviada[0].append(emails_general_nemp[i])
        #print(emails_general_employee_name[i])
        Data_general_no_enviada[1].append(emails_general_employee_name[i])
        #print(emails_general_email1[i])
        Data_general_no_enviada[2].append(emails_general_email1[i])
        #print(emails_general_email2[i])
        Data_general_no_enviada[3].append(emails_general_email2[i])
        contador += 1

for i in range(contador):
    pass
    #print(Data_general_no_enviada[0][i], " ",Data_general_no_enviada[1][i], " ", Data_general_no_enviada[2][i], " ", Data_general_no_enviada[3][i] )
    """ print(Data_general_no_enviada[0][i])
    print(Data_general_no_enviada[1][i])
    print(Data_general_no_enviada[2][i])
    print(Data_general_no_enviada[3][i]) """

#TRANSPONEMOS LA MATRIZ, PORQUE SALE VOLTEADA
a_transponer = np.array(Data_general_no_enviada)
b_transpuesta = a.transpose()

print(b_transpuesta)

#CONVERTIMOS A CSV LA MATRIZ TRANSPUESTA
df = pandas.DataFrame(b_transpuesta)
df.to_csv('list.csv', index=False)