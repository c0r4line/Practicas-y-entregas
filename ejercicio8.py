nombre1=''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Facundo', 'FEDERICO', 'FEDERICO', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Jonathan', 'Jorge', 'JOSE', 'JUAN', 'Juan', 'Juan', 'Julian', 'Julieta', 'LAUTARO', 'Leonel', 'LUIS', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'NICOLÁS', 'Noelia', 'Pablo', 'Priscila', 'TOMAS', 'Tomás', 'Ulises', 'Yanina' '''
nombre2=''' 'Agustin', 'AGUSTIN', 'Agustín', 'Ailen', 'Alfredo', 'Amalia', 'Ariana', 'Bautista', 'Braian', 'Carla', 'CESAR', 'Daniel', 'Diego', 'ELIANA', 'Facundo', 'Facundo', 'Facundo', 'Facundo', 'Federico', 'Federico', 'Flavia', 'Francisco', 'Germán', 'Guido', 'GUSTAVO', 'Hilario', 'Ignacio', 'IVAN', 'Jimmy', 'Joaquín', 'Jose', 'Josue', 'JUAN', 'Juan', 'Laura', 'LAURA', 'Lautaro', 'Lautaro', 'Ludmila', 'Marcos', 'Marcos', 'MARIANELA', 'MARTIN', 'MATEO', 'Mateo', 'Matias' 'MAURO', 'Maximiliano', 'NESTOR', 'Nicolas', 'Pedro', 'Ramiro', 'Sofía', 'Tobias', 'Tomás', 'Tomás', 'Ulises', 'Yanina' '''
notas1='''81,60,72,24,15,91,12,70,29,42,16,3,35,67,10,57,11,69,12,77,13,86,48,65,51,41,87,43,10,87,91,15,44,85,73,37,42,95,18,7,74, 60,9,65,93,63,74'''
notas2='''30,95,28,84,84,43,66,51,4,11,58,10,13,34,96,71,86,37,64,13,8,87,14,14,49,27,55,69,77,59,57,40,96,24,30,73,95,19,47,15,31,39,15,74,33,57,10'''


nom1= nombre1.replace("'"," ")
nom2= nombre2.replace("'"," ")
nom1= nom1.lower().split(',')
nom2= nom2.lower().split(',')

nombres= [nombre for nombre in nom1 if nombre in nom2]
print('Los nombres que se encuentran en ambas listas son: ')
print(nombres)


not1= notas1.split(',')
not2= notas2.split(',')
diccionario= {}

for x in range (len(nom1)):
    diccionario[nom1[x]]= int(not1[x])+ int(not2[x])

print(f'       Nombre          Eval1            Eval2            Total')


for pos in range(len(nom1)):
    print('%2s' % pos,' ', nom1[pos].ljust(11),'%8s'  % not1[pos],' %15s' % not2[pos],' %16s ' %  diccionario[nom1[pos]])



