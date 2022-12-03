'''
	EJEMPLO DE CASO DE USO DEL ALGORITMO DE VENTANA DESLIZANTE
	todas las subcadenas de una cadena que son una permutación de otra cadena
	-----------------------------------
	Problema:	Encontrar todas las subcadenas de una cadena que contiene todos los caracteres de otra cadena. 
			En otras palabras, buscar todas las subcadenas de la primera cadena que sean anagramas de la segunda cadena.
			Tenga en cuenta que el problema se dirige específicamente subcadenas contíguas (es decir, ocupan posiciones consecutivas) 
			e inherentemente mantienen el orden de los elementos.
	Entrada:	Dada una string s y otra string p.
	Salida: 	Buscar el conjunto result más larga dentro de la cadena s que contiene p cantidad de caracteres distintos. 
			Si p es mayor que el número total de caracteres distintos en la string, r devuelve la string completa.
	El problema difiere del problema de encontrar la subsecuencia más larga con cantidad p caracteres distintos. 
	A diferencia de las subsecuencias, subcadenas se requiere que ocupen posiciones consecutivas dentro de la string original.

	Por ejemplo, considerando la cadena s = 'XYYZXZYZXXYZ'
	Para una cadena patrón p = 'XYZ'
	Anagrama sería 'YZX' presente en el índice 2
	Anagrama sería 'XZY' presente en el índice 4
	Anagrama sería 'YZX' presente en el índice 6
	Anagrama sería 'XYZ' presente en el índice 9
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

def encontrar_anagramas(s, p):
    conjunto_p = Counter(p)
    conjunto_ventana = Counter()
    result = {}
    fin = 0
    while fin < len(s):
        conjunto_ventana[s[fin]] += 1
        if sum(conjunto_ventana.values()) == len(p):
            if conjunto_ventana == conjunto_p:
                result[fin-len(p)+1] = s[fin-len(p)+1:fin+1]
            conjunto_ventana[s[fin-len(p)+1]] -= 1
            if conjunto_ventana[s[fin-len(p)+1]] == 0: del conjunto_ventana[s[fin-len(p)+1]]
        fin += 1
    return result

# para probarlo y experimentar
# https://techiedelight.com/compiler/?~find_max_substring_with_n_different_chars

# para mayores referencias dirigirse a
# https://www.techiedelight.com/es/sliding-window-problems/
# https://leetcode.com/problems/minimum-window-substring/discuss/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems
