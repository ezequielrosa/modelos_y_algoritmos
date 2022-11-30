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

	1.	Como resultado vamos a devolver la subcadena que haya quedado dentro de la ventana cuando esta fué más grande
	2.	La ventana crece mientras esté compuesta por hasta p cantidad de caracteres distintos
	3.	Cada caracter distinto va a ser un elemento del conjunto, una llave clave del contador counter(dict)
	4.	Utilizamos dos punteros auxiliares para registrar el momento y tamaño máximo de la ventana
	5.	Cuando la cantidad de caracteres en la ventana es superior a p mantenemos su tamaño y seguimos avanzando
	6.	Cada vez que la cantidad de caracteres que componen la cadena cambia verificamos si se vuelve a cumplir la condición p
	7.	El proceso no termina hasta que la ventana no haya llegado al final de la cadena
	
'''


from collections import Counter


def sliding_window_template_with_examples(s, p):
    # inicializar la tabla hash
    # counter se usa para indicar el estado actual, en algunos casos se podría utilizar defaultdict en vez de counter
    # por ejemplo si no hubiera restricciones p
    # en este caso necesitamos llevar un conjunto con hasta p + 1 cantidad de elementos
    counter = Counter(p)

    # los dos punteros que indican los extremos de la ventana deslizante
    start, end = 0, 0
    # los dos punteros que indican desde y hasta donde fue más grande la ventana
    # es decir la ventana más grande que solo tuvo p cantidad de caracteres
    desde, hasta = 0, 0
    # condicion de corte, se actualiza cada vez que cambia alguna clave, el valor inicial depende del caso
    # en nuestro caso la cantidad de caracteres distintos que hay en la ventana
    # mientras sea menor o igual a p ampliamos la ventana
    count = 0
    # resultado, se devuelve un entero (en caso de máximo o mínimo) o una lista (con todos los índices)
    r = 0

    # recorrer la cadena s de principio a fin
    while end < len(s):
	# incrementamos el contador del caracter actual en la colección counter
        counter[s[end]] += 1

	'''
	# actualiza el contador según alguna condición
        if counter[s[end]] > 1:
            count += 1
        end += 1
	'''
	
        # condición del contador
        while len(counter) > p:
            '''
            acá actualizamos res si estamos buscando un mínimo 
            '''
	    # si hay más de p caracteres distintos mantenemos el tamaño de la ventana
            # avanzamos el puntero start para hacerlo inválido o válido nuevamente
	    # restamos la cantidad del caracter que hay en start porque ya no pertenece a la ventana
            counter[s[start]] -= 1
            # update count based on some condition
            if counter[s[start]] == 0:
                del counter[s[start]]
            start += 1
        '''
        acá actualizamos res si estamos buscando un máximo
        '''

	if hasta - desde < end - start
	    hasta = end
	    desde = start
	
	end += 1
	'''
        res = max(res, end - start)
	'''
    return s[desde:hasta + 1]

# para mayores referencias dirigirse a leetcode
# https://leetcode.com/problems/minimum-window-substring/discuss/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems
