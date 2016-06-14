import random

largo = 8 #La longitud del material genetico de cada individuo
num = 50 #La cantidad de individuos que habra en la poblacion
pressure = 3 #Cuantos individuos se seleccionan para reproduccion. Necesariamente mayor que 2
mutation_chance = 0.2 #La probabilidad de que un individuo mute
limiteDeGeneraciones = 1000
peorVal = 0
  
def individuo(min, max):
    """
        Crea un individuo
    """
    return[random.randint(min, max) for i in range(largo)]
  
def crearPoblacion():
    """
        Crea una poblacion nueva de individuos
    """
    return [individuo(1,9) for i in range(num)]

def calcularConflictos(individuo):
	terminado = False
	conflictos = 0

	verticales = [0,0,0,0,0,0,0,0]

	for i in individuo:
		verticales[i-1] += 1

	# print verticales
	for i in verticales:
		if i > 0:
			conflictos += (i - 1)

	for i in xrange(0,8):
		valor = individuo[i]
		for j in xrange(1,8-i):
			if individuo[i+j] == valor + j:
				# print valor, individuo[i+j], '=', valor + j
				conflictos += 1
			if individuo[i+j] == valor - j:
				# print valor, j, individuo[i+j], '=', valor - j
				conflictos += 1
	return conflictos

def peor(poblacion):
	peor = 0
	for individuo in poblacion:
		conflictos = calcularConflictos(individuo)
		print conflictos, peor
		if conflictos > peor:
			peor = conflictos
	return peor
  
def calcularFitness(individuo):
    """
        Calcula el fitness de un individuo concreto.
    """
    return peorVal - calcularConflictos(individuo)
  
def mejorOp(poblacion):
	mop = []
	mejorVal = 0
	for individuo in poblacion:
		if mejorVal < calcularFitness(individuo):
			mop = individuo[0::]
	return mop

def selection_and_reproduction(poblacion):
    """
        Puntua todos los elementos de la poblacion (poblacion) y se queda con los mejores
        guardandolos dentro de 'selected'.
        Despues mezcla el material genetico de los elegidos para crear nuevos individuos y
        llenar la poblacion (guardando tambien una copia de los individuos seleccionados sin
        modificar).
        Por ultimo muta a los individuos.
    """
    puntuados = [ (calcularFitness(i), i) for i in poblacion] #Calcula el fitness de cada individuo, y lo guarda en pares ordenados de la forma (5 , [1,2,1,1,4,1,8,9,4,1])
    puntuados = [i[1] for i in sorted(puntuados)] #Ordena los pares ordenados y se queda solo con el array de valores
    poblacion = puntuados
  
  
  
    selected =  puntuados[(len(puntuados)-pressure):] #Esta linea selecciona los 'n' individuos del final, donde n viene dado por 'pressure'
  
  
  
    #Se mezcla el material genetico para crear nuevos individuos
    for i in range(len(poblacion)-pressure):
        punto = random.randint(1,largo-1) #Se elige un punto para hacer el intercambio
        padre = random.sample(selected, 2) #Se eligen dos padres
          
        poblacion[i][:punto] = padre[0][:punto] #Se mezcla el material genetico de los padres en cada nuevo individuo
        poblacion[i][punto:] = padre[1][punto:]
  
    return poblacion #El array 'poblacion' tiene ahora una nueva poblacion de individuos, que se devuelven
  
def mutation(poblacion):
    """
        Se mutan los individuos al azar. Sin la mutacion de nuevos genes nunca podria
        alcanzarse la solucion.
    """
    for i in range(len(poblacion)-pressure):
        if random.random() <= mutation_chance: #Cada individuo de la poblacion (menos los padres) tienen una probabilidad de mutar
            punto = random.randint(1,largo-1) #Se elgie un punto al azar
            nuevo_valor = random.randint(1,9) #y un nuevo valor para este punto
  
            #Es importante mirar que el nuevo valor no sea igual al viejo
            while nuevo_valor == poblacion[i][punto]:
                nuevo_valor = random.randint(1,9)
  
            #Se aplica la mutacion
            poblacion[i][punto] = nuevo_valor
  
    return poblacion

#############

poblacion = crearPoblacion() # Inicializamos una poblacion

generacion = 0

poblacion2 = [[4,3,6,2,5,8,3,1], [7,5,2,4,6,8,3,1]]

peorVal = peor(poblacion2)

def pinta(individuo):
	for i in individuo:
		linea = ''
		for j in xrange(1,9):
			if j == i:
				linea += ' Q '
			else:
				linea += ' _ '
		print linea

for individuo in poblacion2:
	pinta(individuo)
	con = calcularConflictos(individuo)
	print 'conflictos =', con
	fitness = calcularFitness(individuo)
	print 'fitness', fitness