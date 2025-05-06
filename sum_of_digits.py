# Suma de dígitos
# Por: toko0715

# Declaramos la función con 2 variables que serán inicializadas: "pos" y "sum".
# Estas variables irán cambiando su valor a medida que se ejecuta la función recursiva,
# así que comenzarán siendo 0.

def sum_of_digits(n, pos = 0, sum = 0, first_time = True):
    
    # Si el número ingresado es 0, definitivamente la suma es 0. Si el numero no es entero, lanzamos un error.
    if not isinstance(n, int):
        raise ValueError("Do not enter a number that is not an integer")
    if n == 0:
        return 0

    # Al ingresar por primera vez a la función, validamos que sea efectivamente la primera llamada.
    # Luego verificamos si el número ingresado es positivo (mayor que 0). Si no lo es, lo multiplicamos por -1 para
    # convertirlo en positivo.
    # 155 -> len("155") -> int(3) -> 3 = número de dígitos
    # Trabajamos con índices, así que restamos 1 para trabajar con el último dígito.
    if first_time == True:
        if n < 0:
            n = n * -1
        pos = len(str(n)) - 1
    
    # Sumamos el valor actual de "sum" con el dígito correspondiente del número ingresado (ejem: 155),
    # convirtiendo primero el número a string (ejem: "155"), para luego acceder a su posición [pos] (ejem: 2),
    # obteniendo así el dígito en esa posición (ejem: "5").
    # Como es el primer ingreso a la función, será el último dígito.
    # Luego, convertimos ese carácter a entero (ejem: int("5")) y lo sumamos a "sum".
    sum = sum + int(str(n)[pos])
    
    # En este punto ya tenemos una suma. Validamos si esta tiene un valor mayor o igual a 1.
    # En caso afirmativo, retornaremos la suma si "pos" llega a 0, o sea, al primer dígito del número.
    # Recordar que si la suma es 0 es porque el número ingresado fue 0, lo cual ya validamos al inicio.
    # Al retornar, comenzaremos a devolver el valor de la suma de función en función hasta salir de todas.

    if pos == 0 and sum >= 1:
        return sum
    
    # Finalmente, si la condición anterior no se cumple, significa que aún hay dígitos por procesar,
    # es decir, una posición anterior existe. Entonces, ingresamos de nuevo a la función
    # pero esta vez con una posición anterior y con el valor de "firs_time" como False.

    return sum_of_digits(n, pos - 1, sum, False)

# FIN DEL ALGORITMO


# Casos de prueba:

# Caso 1:
# Numero: 155
print(sum_of_digits(155) == 11)

# Caso 2:
# Numero: 0
print(sum_of_digits(0) == 0)

# Caso 3:
# Numero: 0000000000
print(sum_of_digits(0000000000) == 0)

# Caso 4:
# Numero: 1000
print(sum_of_digits(1000) == 1)

# Caso 5:
# Numero: -120
print(sum_of_digits(-120) == 3)

# Caso 6:
# Numero: -0
print(sum_of_digits(-0) == 0)

# Caso 7:
# Numero: 0.5 or -0.5
#Error: print(sum_of_digits(0.5)) == ValueError: Do not enter a number that is not an integer


