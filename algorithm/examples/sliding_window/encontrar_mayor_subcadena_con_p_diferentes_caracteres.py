'''

	EJEMPLO DE CASO DE USO DEL ALGORITMO DE VENTANA DESLIZANTE
	subcadena más larga que contiene p cantidad de caracteres distintos

	-----------------------------------

	Problema:	Dada una cadena s encontrar la subcadena más larga que contiene p cantidad de caracteres distintos.
	Entrada:	Dada una string s y un número positivo p.
	Salida: 	Buscar la subcadena r más larga dentro de la cadena s que contiene p cantidad de caracteres distintos. 
			Si p es mayor que el número total de caracteres distintos en la string, r devuelve la string completa.

	El problema difiere del problema de encontrar la subsecuencia más larga con cantidad p caracteres distintos. 
	A diferencia de las subsecuencias, subcadenas se requiere que ocupen posiciones consecutivas dentro de la string original.

	Por ejemplo, considerando la string ‘abcbdbdbbdcdabd’

	Para p = 2, r sería ‘bdbdbbd’
	Para p = 3, r sería ‘bcbdbdbbdcd’
	Para p = 5, r sería ‘abcbdbdbbdcdabd’

	-----------------------------------

	El algoritmo de ventana deslizante se utiliza para encontrar subcadenas o para problemas de máximos y mínimos.

	Utiliza dos punteros como límites de una ventana deslizable
	Utiliza una colección counter(dict) como conjunto para ir manteniendo el estado actual de la búsqueda 
	Utiliza un contador como condición de éxito, el cual se actualiza cada vez que cambia una clave de la colección counter(dict)
	Además puede cumplir con un patrón p o condición que se debe respetar

	Tiempo: 	O(n), el tiempo de ejecución es del orden de n porque se recorre toda la cadena	
	Espacio:	O(k) donde k es el tamaño del conjunto p, k = len(set(p)), el espacio depende del patrón p que se debe respetar

	-----------------------------------

	SOLUCION

	1.	Vamos a devolver la subcadena que haya quedado dentro de la ventana cuando esta fué más grande
	2.	La ventana crece mientras esté compuesta por hasta p cantidad de caracteres distintos
	3.	Cada caracter distinto va a ser un elemento del conjunto, una llave clave del contador counter(dict)
	4.	Utilizamos dos punteros auxiliares para registrar el momento del tamaño máximo de la ventana
	5.	Cuando la cantidad de caracteres en la ventana es superior a p la achicamos
	6.	Cada vez que la cantidad de caracteres que componen la cadena cambia verificamos si se vuelve a cumplir la condición p
	7.	El proceso no termina hasta que la ventana no haya llegado al final de la cadena
	
'''

from collections import Counter

def encontrar_mayor_subcadena_con_p_diferentes_caracteres(s, p):
	# s es la cadena de entrada (string)
	# p es el patrón que condiciona la búsqueda en este caso un entero cantidad
	# contador es una colección que sirve de conjunto y contador
	contador = Counter()
	# vent_inicio es el puntero límite inferior de la ventana
	# vent_fin es el puntero límite superior de la ventana
	vent_inicio, vent_fin = 0, 0
	# result_desde es el puntero inferior que indica dónde la ventana fué máxima
	# result_hasta es el puntero superior que indica dónde la ventana fué máxima
	result_desde, result_hasta = 0, 0
	# recorrer con la ventana deslizante toda la cadena s
	while vent_fin < len(s):
		# incrementar en el contador la cantidad del caracter actual
		contador[s[vent_fin]] += 1
		# si en el contador hay más de p caracteres distintos achicar la ventana
		while len(contador) > p:
			# quitar el caracter del inicio de la ventana
			contador[s[vent_inicio]] -= 1
			# quitar el caracter del conjunto si ya no pertenece a la ventana
			if contador[s[vent_inicio]] == 0 : del contador[s[vent_inicio]]
			# achicar la ventana avanzando el puntero inferior
			vent_inicio += 1
		# en este punto la ventana tiene p o menos caracteres distintos
		# verificamos si este nuevo tamaño de la ventana es el mayor
		if result_hasta - result_desde < vent_fin - vent_inicio:
			result_hasta = vent_fin
			result_desde = vent_inicio
		# incrementamos el tamaño de la ventana avanzando el límite superior
		vent_fin += 1
	# devolvemos la subcadena resultante
	return s[result_desde:result_hasta + 1]

# para probarlo y experimentar
# https://techiedelight.com/compiler/?~find_max_substring_with_n_different_chars

# para mayores referencias dirigirse a
# https://www.techiedelight.com/es/sliding-window-problems/
# https://leetcode.com/problems/minimum-window-substring/discuss/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems
