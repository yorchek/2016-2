/* Ejercicio1 */

/* Predicados auxiliares */
/* Regresa las palabras */

w1(X) :- X = word(astante, a,s,t,a,n,t,e).
w2(X) :- X = word(astoria, a,s,t,o,r,i,a).
w3(X) :- X = word(baratto, b,a,r,a,t,t,o).
w4(X) :- X = word(cobalto, c,o,b,a,l,t,o).
w5(X) :- X = word(pistola, p,i,s,t,o,l,a).
w6(X) :- X = word(statale, s,t,a,t,a,l,e).

/* Predicados auxiliares */
/* Regresa los posibles cruces de palabras */
/* ej. 2_4 la letra 2 de W1 se cruza con la letra 4 de W2 */

cross2_2(W1,W2) :- w1(W1),w2(W2).
cross2_4(W1,W2) :- w3(W1),w1(W2); w3(W1),w4(W2); w6(W1),w5(W2); w4(W1),w2(W2).
cross2_6(W1,W2) :- w5(W1),w2(W2); w6(W1),w1(W2); w6(W1),w3(W2); w6(W1),w4(W2).
cross4_4(W1,W2) :- w1(W1),w3(W2); w1(W1),w4(W2); w3(W1),w4(W2); w5(W1),w6(W2).
cross4_6(W1,W2) :- w5(W1),w1(W2); w5(W1),w3(W2); w5(W1),w4(W2).
cross6_6(W1,W2) :- w5(W1),w6(W2); w1(W1),w3(W2); w1(W1),w4(W2); w3(W1),w4(W2).

/* Hechos auxiliares */
/* Define como se deben cruzar las palabras verticales con las horizontales */

cross(V1,V2,V3,H1,H2,H3) :- cross2_2(H1,V1), cross2_4(V2,H1), cross2_6(V3,H1),
	cross2_6(H3,V1), cross2_4(H2,V1).


/* Ejercicio2 */
 
/* Predicado auxiliar para llevar un contador de los posibles valores */
/* Regresa true si el valor es igual al acarreo, */
/* regresa false en otro caso */

cantex_a(C,[H|Tail],V) :- V is C+H; cantex_a(+(C,H),Tail,V); cantex_a(C, Tail, V).

/* Predicado que recibe una Lista y un valor */
/* regresa true si el valor se puede generar con los elementos de la lista */
/* regresa false en otro caso */
cantex(L,V) :- cantex_a(0,L,V).


/* Ejercicio3 */

/* Hechos auxiliares */
/* Regresa los colores que pueden ser vecinos */

color_vecinos(azul,rojo).
color_vecinos(azul,amarillo).
color_vecinos(azul,verde).
color_vecinos(rojo,amarillo).
color_vecinos(rojo,verde).
color_vecinos(amarillo,verde).

/* Predicado auxiliar */
/* A partir de los vecinos asignados los colorea */

vecinos(X,Y) :- color_vecinos(X,Y).

/* Predicado auxiliar */
/* Construye la figura */

color_figura(R1,R2,R3,R4,R5,R6) :- vecinos(R1,R2), vecinos(R1,R3), vecinos(R1,R4), vecinos(R1,R5),
 vecinos(R2,R3), vecinos(R3,R5), vecinos(R4,R5), vecinos(R4,R6).

/* Predicado que colorea una figura de 6 lados */

colorea(Reg1,Reg2,Reg3,Reg4,Reg5,Reg6) :- color_figura(Reg1,Reg2,Reg3,Reg4,Reg5,Reg6).