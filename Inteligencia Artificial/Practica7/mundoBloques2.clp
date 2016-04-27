(deftemplate goal
    (slot move)
    (slot on-top-of))

;; Mueve un cubo sobre otro
(defrule move-directly
		;; Esta es la parte de las precondiciones

	;; Debemos tener como precondicion querer mover el bloque1 encima del bloque2
	?goal <- (goal (move ?block1) (on-top-of ?block2))

	;; Para eso, necesitamos que los 2 sean bloques
	(block ?block1)
    (block ?block2)

    ;; Como precondicion debemos tener un stack que tenga el bloque 1 y 2 en el tope, respectivamente
	?stack1 <- (stack ?block1 $?rest1)
	?stack2 <- (stack ?block2 $?rest2)
	=>
		;; Esto es lo que se ejecutara/hara si se cumplen todas las precondiciones

	;;	Olvidamos la antigua meta, y los 2 stacks (que van a ser modificados)
	(retract ?goal ?stack1 ?stack2)

	;; Agregamos como nuevo stack al que esta conformado por el resto del stack1
	;; (Quitamos al bloque 1 del tope del stack1)
	(assert (stack $?rest1)

	;; Agregamos como nuevo stack al que tiene en el tope al bloque 1, luego al bloque 2 y el resto2
	;; (Pusimos al bloque2 en el tope del stack que tenia como tope al bloque 2)
			(stack ?block1 ?block2 $?rest2))
	(printout t ?block1 " moved on top of " ?block2 crlf)
)

;; Este lo cambie porque senti que asi estabamos definiendo los stacks xD
;; Igual y funciona como lo teniamos definido antes, pero ya no lo probe
(deffacts initial-state
    (block A) (block B)
    (block C) (block D)
    (block E) (block F)
	(stack A B C)
	(stack D E F)
	(goal (move C) (on-top-of E))
)