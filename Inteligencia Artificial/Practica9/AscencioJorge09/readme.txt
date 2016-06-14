309043511
Ascencio Espíndola Jorge Eduardo

Observaciones:

Cuando se tiene solo las dos entradas [0,0,0] y [1,1,1]
va a ser muy díficil que la red aprenda adecuadamente ya que no tiene
muchos valores por lo que no clasificara bien
Si se tiene un conjunto de entrenamiento con cerca del 70% 
de todos los valores es más fácil que la red aprenda, o bien 
si se tiene un conjunto de entrenamiento con una buena cantidad de 
combinaciones es más fácil que la red pueda clasificar
Si se mete todas las entradas tampoco es recomendable ya que 
tendra un sobre entrenamiento y no podrá clasificar nuevas entradas adecuadamente.

Cómo funciona?

Ingresar a modo interprete con python -i rNeuronal.py
el programa tiene los conjuntos de entrenamiento para and y or
se llaman entrenamiento(And|Or)i con i = 1...5
para que la red aprenda se usa neurona.entrenar(conjuntoDeEntrenamiento)
o con entrena(conjuntoDeEntrenamiento)
también tiene el conjunto con todos los valores llamado prueba
para evaluar todas las entradas de prueba puedes usar la funcion evalua()