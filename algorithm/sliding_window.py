# El algoritmo de ventana deslizante se utiliza para encontrar subcadenas o para problemas de máximos y mínimos.
#
# Utiliza dos punteros como límites de la ventana deslizable o segmento que va a recorrer, y utiliza una 
# colección counter(dict) para ir manteniendo el estado actual de la búsqueda, y un contador como 
# condición de corte, el cual se actualiza cada vez que cambia una clave de la colección counter(dict).
#
# Sliding windows code template is most used in substring match or maximum/minimum problems.
# It uses two-pointer as boundary of sliding window to traverse, and use a counter(dict) maintain current state,
# and a count as condition checker, update it when trigger some key changes.
#
# Tiempo:  O(n)
# Espacio: O(k) donde k es el tamaño del conjunto p, k = len(set(p))
from collections import Counter


# s - target sequence, p - pattern or restrict sequence
# s - es la secuencia o cadena en la que se está buscando p, p - patrón (esquema) o restricciones de la secuencia
def sliding_window_template_with_examples(s, p):
    # initialize the hash map here
    # inicializa la tabla hash
    # counter is used to record current state, could use defaultdict in some situation, for example, no p restrict
    # counter se usa para indicar el estado actual, en algunos casos se podría utilizar defaultdict en vez de counter
    # por ejemplo si no hubiera restricciones p
    counter = Counter(p)

    # two pointers, boundary of sliding window
    # los dos punteros que se usan para los límites de la ventana o segmento
    start, end = 0, 0
    # condition checker, update it when trigger some key changes, init value depend on your situation
    # condicion de corte, se actualiza cada vez que cambia alguna clave, el valor inicial depende del caso
    count = 0
    # result, return int(such as max or min) or list(such as all index)
    # resultado, se devuelve un entero (en caso de máximo o mínimo) o una lista (con todos los índices)
    res = 0

    # loop the source string from begin to end
    # recorrer la cadena s de principio a fin
    while end < len(s):
        counter[s[end]] += 1
        # update count based on some condition
        # actualiza el contador según alguna condición
        if counter[s[end]] > 1:
            count += 1
        end += 1

        # count condition here
        # condición del contador
        while count > 0:
            '''
            update res here if finding minimum
            acá actualizamos res si estamos buscando un mínimo 
            '''

            # increase start to make it invalid or valid again
            # avanzamos el puntero start para hacerlo inválido o válido nuevamente
            counter[s[start]] -= 1
            # update count based on some condition
            if counter[s[start]] > 0:
                count -= 1
            start += 1

        '''
        update res here if finding maximum
        acá actualizamos res si estamos buscando un máximo
        '''
        res = max(res, end - start)

    return res


# para mayores referencias dirigirse a 
# https://leetcode.com/problems/minimum-window-substring/discuss/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems
# ejemplo
# https://www.techiedelight.com/?id=YUS7
