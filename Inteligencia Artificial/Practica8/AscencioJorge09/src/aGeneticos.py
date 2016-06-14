import random

mutation_chance = 0.2
class Individuo(object):

	fitness = 0
	cromosoma = []

	"""docstring for Individuo"""
	def __init__(self, cromosoma):
		super(Individuo, self).__init__()
		self.cromosoma = cromosoma

	def __str__(self):
		return '(Fitness: '+str(self.fitness)+', cromosoma: '+str(self.cromosoma)+')'

	def mutacion(self):
		"""
			Metodo para mutacion de un individuo.
		"""
		for i in xrange(0,8):
			mutacion =  random.random()
			if mutacion >= mutation_chance:
				self.cromosoma[i] = (self.cromosoma[i]+1) % 8
				if self.cromosoma[i] == 0:
					self.cromosoma[i] = 8

num = 50
largo = 8

def individuo(min, max):
    """
        Crea un individuo
    """
    return Individuo(cromosoma = [random.randint(min, max) for i in range(largo)])

class Reinas(object):

	poblacion = []
	peorVal = 0
	optimoEncontrado = False

	"""docstring for Reinas"""
	def __init__(self, poblacion):
		super(Reinas, self).__init__()
		self.poblacion = poblacion

	def crearPoblacion(self):
		"""
			Crea una poblacion nueva de individuos
		"""
		self.poblacion = [individuo(1,8) for i in range(num)]

	def mejorOp(self):
		"""
			Regresa el mejor individuo de la poblacion (mayor fitness)
		"""
		mop = Individuo(cromosoma = [])
		mejorVal = 0
		for individuo in self.poblacion:
			if individuo.fitness > mejorVal:
				mop.cromosoma = individuo.cromosoma[0::]
				mop.fitness = individuo.fitness
				mejorVal = individuo.fitness
		return mop

	def peor(self):
		"""
			Regresa el mayor numero de conflictos de la poblacion
		"""
		for individuo in self.poblacion:
			#print self.peorVal
			conflictos = calcularConflictos(individuo)
			#print individuo.cromosoma, conflictos
			if conflictos > self.peorVal:
				self.peorVal = conflictos

	def asignarFitness(self):
		"""
			Asigna el fitness a cada individuo de la poblacion
		"""
		for individuo in self.poblacion:
			individuo.fitness = calcularFitness(self.peorVal, individuo)

	def haySolucion(self):
		for individuo in self.poblacion:
			if calcularConflictos(individuo) == 0:
				self.optimoEncontrado = True

	def seleccionRuleta(self):
		return random.choice(self.poblacion)


def calcularConflictos(individuo):
	"""
		Metodo que calcula el numero de ataques de cada reina
		regresa la suma de los ataques de todas las reinas.
	"""
	conflictos = 0

	# Auxiliar para saber si ya ataco en vertical
	verticales = [0,0,0,0,0,0,0,0]

	# Primero sumamps los ataques en vertical
	for i in xrange(0,8):
		for j in xrange(i+1,8):
			# Si ya enfrento en vertical ya no hay que seguir checando
			if individuo.cromosoma[j] == individuo.cromosoma[i] and verticales[i] == 0:
				#print 'Se enfrentan', individuo.cromosoma[i], individuo.cromosoma[j]
				verticales[i] = 1
				conflictos += 1
				break

	# Auxiliar para saber si ya ataco en diagonal
	diagonales = [0,0,0,0,0,0,0,0]
	# Auxiliar para saber si ya ataco en diagonal invertida
	diagonalesInv = [0,0,0,0,0,0,0,0]

	# Sumamos los ataques en diagonal
	for i in xrange(0,8):
		valor = individuo.cromosoma[i]
		for j in xrange(1,8-i):
			# Si ya enfrento en diagonal y diagonal invertida ya no hay que seguir checando
			if diagonales[i] == 1 and diagonalesInv[i] == 1:
				break
			if individuo.cromosoma[i+j] == valor + j and diagonales[i] == 0:
				#print 'Se enfrentan', individuo.cromosoma[i], individuo.cromosoma[i+j]
				diagonales[i] = 1
				conflictos += 1
			elif individuo.cromosoma[i+j] == valor - j and diagonalesInv[i] == 0:
				#print 'Se enfrentan', individuo.cromosoma[i], individuo.cromosoma[i+j]
				diagonalesInv[i] = 1
				conflictos += 1
	individuo.conflictos = conflictos
	return conflictos
  
def calcularFitness(peorVal, individuo):
    """
        Calcula el fitness de un individuo concreto.
        fitness = max(#enfrentamientos(poblacion)) - #enfrentamientos(individuo)
    """
    return peorVal - calcularConflictos(individuo)

def pinta(individuo):
	"""
        Metodo para dibujar un individuo concreto.
    """
	print 'Fitness:', individuo.fitness
	valores = individuo.cromosoma[::] 
	for i in xrange(0,8):
		linea = ''
		for j in xrange(0,8):
			valores[j] -= 1
			if valores[j] == 0:
				linea += ' Q '
			else:
				linea += ' _ '
		print linea

def recombinacion(individuo1, individuo2):
	"""
        Metodo para recombinar dos individuos.
        Regresa un individuo producto de la recombinacion.
    """
	num = random.randint(2,6)
	cromosoma = individuo1.cromosoma[0:num]
	for i in xrange(num,8):
		cromosoma.append(individuo2.cromosoma[i])
	return Individuo(cromosoma = cromosoma)

######### Main #########

poblacion = Reinas(poblacion = [])
poblacion.crearPoblacion()
poblacion.peor()
poblacion.haySolucion()

limiteGeneraciones = 1001
generacion = 1


while generacion < limiteGeneraciones:
	poblacion.asignarFitness()
	poblacion.haySolucion()
	# Verificamos si ya hay solucion, si hay salimos del ciclo
	if poblacion.optimoEncontrado == True:
		break
	nuevaPoblacion = []
	mop = poblacion.mejorOp()
	mop.mutacion()
	nuevaPoblacion.append(mop)
	if generacion % 50 == 0:
		print 'Mejor opcion generacion', generacion, ':'
		print mop
	for i in xrange(0,50):
		individuo1 = poblacion.seleccionRuleta()
		individuo2 = poblacion.seleccionRuleta()
		hijo = recombinacion(individuo1, individuo2)
		hijo.mutacion()
		nuevaPoblacion.append(hijo)
	poblacion = Reinas(poblacion = nuevaPoblacion)
	poblacion.peor()
	generacion += 1
print ''
if poblacion.optimoEncontrado:
	print 'Se encontro el optimo en la generacion', generacion
	mop = poblacion.mejorOp()
	print mop
	pinta(mop)
else:
	print 'La mejor opcion es'
	print poblacion.mejorOp()