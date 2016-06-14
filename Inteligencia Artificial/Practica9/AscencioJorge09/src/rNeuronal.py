# -*- coding: utf-8 -*-

# Autor := Jorge Eduardo Ascencio Espíndola

class Neurona(object):
    ALPHA = 0.80
    pesos = []
    salida = 0

    # Metodo que nos da el valor del error
    def calcula_error(self, salida, salida_deseada):
        return  salida_deseada - salida

    # Metodo que calcula el nuevo peso de la arista de la neurona
    # w: peso actual, x: valor, e: error
    def calcula_peso_nuevo(self, w, x, e):
        print w, '+', self.ALPHA, '*', x, '*', e, '=', w + self.ALPHA * x * e
        return w + self.ALPHA * x * e

    # Metodo funcion de activacion, decide si una neurona se activa o no dadas las entradas
    # regresa 1 si la suma es mayor que 0, regresa 0 en otro caso
    def funcion_activacion(self, entradas):
        suma = 0
        for x in xrange(0, 3):
            suma = suma + entradas[x]*self.pesos[x]

        suma = suma + 1*self.pesos[3]

        if suma > 0: return 1
        else : return 0

    # Metodo para entrenar la neurona dado un conjunto de entrenamiento
    def entrenar(self, conj_entrenamiento):
        count = 0
        entrenada = 0
        # entrena hasta que el error no cambie
        while(entrenada < len(conj_entrenamiento)):
            count += 1
            entrenada = 0
            # itera sobre todas las entradas del conjunto de entrenamiento
            for x in xrange(0, len(conj_entrenamiento)):
                entradas = conj_entrenamiento[x]['entradas']
                salida_deseada = conj_entrenamiento[x]['salida_deseada']
                res = self.funcion_activacion(entradas)
                print entradas, ' ', salida_deseada, '=', res

                # si ya evalua bien no hace nada
                if res == salida_deseada:
                    print 'Bien!'
                    entrenada = entrenada + 1
                else:
                    # si no evalua bien actualiza los pesos
                    err = self.calcula_error(res, salida_deseada)
                    print 'El error es ' + str(err)
                    for p in xrange(0,3):
                        self.pesos[p] = self.calcula_peso_nuevo(self.pesos[p], entradas[p], err)
                    self.pesos[3] = self.calcula_peso_nuevo(self.pesos[3], 1, err)
                    print 'Nuevos pesos ' + str(self.pesos)
        print 'Se entreno con '+ str(count) + ' iteraciones'

    # Metodo para consultar alguna entrada
    def hacer_consulta(self,entradas):
        return self.funcion_activacion(entradas)

    """docstring for Neurona"""
    def __init__(self):
        super(Neurona, self).__init__()
        self.pesos = [0.1,0.4,0.2,0.5]

neurona = Neurona()

entrenamientoAnd1 = [
    {
        'entradas': [0,0,0],
        'salida_deseada': 0
    },
    {
        'entradas': [1,1,1],
        'salida_deseada': 1
    }
]

entrenamientoAnd2 = [
    {
        'entradas': [0,0,0],
        'salida_deseada': 0
    },
    {
        'entradas': [0,0,1],
        'salida_deseada': 0
    },
    {
        'entradas': [1,1,1],
        'salida_deseada': 1
    }
]

entrenamientoAnd3 = [
    {
        'entradas': [0,0,0],
        'salida_deseada': 0
    },
    {
        'entradas': [0,1,1],
        'salida_deseada': 0
    },
    {
        'entradas': [1,1,1],
        'salida_deseada': 1
    },
    {
        'entradas': [1,1,0],
        'salida_deseada': 0
    }
]

entrenamientoAnd4 = [
    {
        'entradas': [0,0,0],
        'salida_deseada': 0
    },
    {
        'entradas': [0,1,1],
        'salida_deseada': 0
    },
    {
        'entradas': [1,1,1],
        'salida_deseada': 1
    },
    {
        'entradas': [1,0,1],
        'salida_deseada': 0
    },
    {
        'entradas': [1,1,0],
        'salida_deseada': 0
    }
]

entrenamientoAnd5 = [
    {
        'entradas': [0,0,0],
        'salida_deseada': 0
    },
    {
        'entradas': [0,0,1],
        'salida_deseada': 0
    },
    {
        'entradas': [0,1,1],
        'salida_deseada': 0
    },
    {
        'entradas': [1,1,1],
        'salida_deseada': 1
    },
    {
        'entradas': [1,0,1],
        'salida_deseada': 0
    },
    {
        'entradas': [1,1,0],
        'salida_deseada': 0
    }
]

entrenamientoOr1 = [
    {
        'entradas': [0,0,0],
        'salida_deseada': 0
    },
    {
        'entradas': [1,1,1],
        'salida_deseada': 1
    }
]

entrenamientoOr2 = [
    {
        'entradas': [0,0,0],
        'salida_deseada': 0
    },
    {
        'entradas': [0,0,1],
        'salida_deseada': 1
    },
    {
        'entradas': [0,1,0],
        'salida_deseada': 1
    },
]

entrenamientoOr3 = [
    {
        'entradas': [0,0,0],
        'salida_deseada': 0
    },
    {
        'entradas': [0,0,1],
        'salida_deseada': 1
    },
    {
        'entradas': [1,0,0],
        'salida_deseada': 1
    },
    {
        'entradas': [1,0,1],
        'salida_deseada': 1
    },
]

entrenamientoOr4 = [
    {
        'entradas': [0,0,0],
        'salida_deseada': 0
    },
    {
        'entradas': [0,0,1],
        'salida_deseada': 1
    },
    {
        'entradas': [0,1,0],
        'salida_deseada': 1
    },
    {
        'entradas': [1,0,0],
        'salida_deseada': 1
    },
    {
        'entradas': [1,1,0],
        'salida_deseada': 1
    }
]

entrenamientoOr5 = [
    {
        'entradas': [0,0,0],
        'salida_deseada': 0
    },
    {
        'entradas': [0,0,1],
        'salida_deseada': 1
    },
    {
        'entradas': [0,1,0],
        'salida_deseada': 1
    },
    {
        'entradas': [1,0,0],
        'salida_deseada': 1
    },
    {
        'entradas': [1,0,1],
        'salida_deseada': 1
    },
    {
        'entradas': [1,1,0],
        'salida_deseada': 1
    }
]

def entrena(conj):
    print 'Entrenando la neurona con', conj
    neurona.entrenar(conj)

prueba = [('[0,0,0]', [0,0,0]), ('[0,0,1]', [0,0,1]), ('[0,1,0]', [0,1,0]), 
             ('[0,1,1]', [0,1,1]), ('[1,0,0]', [1,0,0]), ('[1,0,1]', [1,0,1]), 
             ('[1,1,0]', [1,1,0]), ('[1,1,1]', [1,1,1])]

def evalua():
    for entrada in prueba:
        print 'Evaluando '+ entrada[0] + ' = '+ str(neurona.hacer_consulta(entrada[1]))